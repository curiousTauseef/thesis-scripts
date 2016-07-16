import re
import glob
import concraft
import os
import argparse


def tag_line(line, function, eos):
    if eos:
        line = re.sub(r'|'.join(map(re.escape, ['<s> ', ' </s>'])), '', line)
    mapped = function(line).encode('UTF-8')
    return "<s> {} </s>\n".format(mapped) if eos else mapped + '\n'

def parse_file_recursively(directory, eos): 
    for filename in glob.iglob(os.path.join(args.input, '**/acoustic_hypotheses.txt'), recursive=True):
        with open(filename, 'r') as f:
            lines = (line.rstrip() for line in f)
        for line in lines:

def parse_file_nonrecursively(infile, outfile, eos): 
    with open(infile, 'r') as f, open(outfile, 'w') as out:
        for line in f:
            out.write(tag_line(line, function, eos)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    parser.add_argument('-o', '--output', help='path to the output file', type=str)
    parser.add_argument('-t', '--tokens', help='type of the output tokens, use p for raw POS, t for POS with tags and l for lemmas (default)', type=str, choices='gplt', default='l')
    parser.add_argument('--eos', dest='eos', action='store_true')
    parser.add_argument('--no-eos', dest='eos', action='store_false')
    parser.add_argument('--recursive', dest='eos', action='store_true')
    parser.add_argument('--not-recursive', dest='eos', action='store_false')
    parser.set_defaults(feature=True)
    args = parser.parse_args()
    function = mapping[args.tokens]
    with concraft.Server() as server:
        client = concraft.Client(server.get_port())
        mapping = {'l': client.to_lemmas, 't': client.to_pos_tags, 'p': client.to_pos, 'g': client.to_gnc}
        if args.recursive:

            for line in lines:
                        with open(filename, "w") as f:
                            f.write('\n'.join(altered_lines) + '\n')
