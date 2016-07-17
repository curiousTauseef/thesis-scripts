import re
import glob
import concraft
import os
import argparse


def tag(line, function, eos):
    line.rstrip()
    if eos:
        line = re.sub(r'|'.join(map(re.escape, ['<s> ', ' </s>'])), '', line)
    mapped = function(line)
    return "<s> {} </s>\n".format(mapped) if eos else mapped + '\n'

def tag_recursively(directory, function, eos): 
    for filename in glob.iglob(os.path.join(args.input, '**/acoustic_hypotheses.txt'), recursive=True):
        print(filename)
        with open(filename, 'r') as f:
            lines = [tag(line, function, eos) for line in f]
        with open(filename, 'w') as out:
            out.write('\n'.join(lines) + '\n')

def tag_file(infile, outfile, function, eos): 
    with open(infile, 'r') as f, open(outfile, 'w') as out:
        for line in f:
            out.write(tag(line, function, eos))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    parser.add_argument('-o', '--output', help='path to the output file', type=str)
    parser.add_argument('-t', '--tokens', help='type of the output tokens, use p for raw POS, t for POS with tags and l for lemmas (default)', type=str, choices='gplt', default='l')
    parser.add_argument('--eos', dest='eos', action='store_true')
    parser.add_argument('--no-eos', dest='eos', action='store_false')
    parser.add_argument('--recursive', dest='recursive', action='store_true')
    parser.add_argument('--not-recursive', dest='recursive', action='store_false')
    parser.set_defaults(eos=False)
    parser.set_defaults(recursive=False)
    args = parser.parse_args()
    with concraft.Server() as server:
        client = concraft.Client(server.get_port())
        function = {'l': client.to_lemmas, 't': client.to_pos_tags, 'p': client.to_pos, 'g': client.to_gnc}[args.tokens]
        if args.recursive:
            tag_recursively(args.input, function , args.eos)
        else:
            tag_file(args.input, args.output, function, args.eos)
