#requires Python >= 3.5
import re
import glob
import concraft
import os
import argparse

def strip(line, eos):
    line.rstrip()
    if eos:
        return re.sub(r'|'.join(map(re.escape, ['<s> ', ' </s>'])), '', line)
    else:
        return line

def add_eos(line):
    return "<s> {} </s>".format(line) 

def tag(line, function, eos):
    line = strip(line, eos)
    tagged = function(line)
    return add_eos(tagged) if eos else tagged

def tag_recursively(directory, function, eos): 
    for filename in glob.iglob(os.path.join(args.input, '**/acoustic_hypotheses.txt'), recursive=True):
        print(filename)
        with open(filename, 'r') as f:
            lines = [tag(line, function, eos) for line in f]
        with open(filename, 'w') as out:
            out.write('\n'.join(lines) + '\n')

def tag_nbest(infile, outfile, function): 
    with open(infile, 'r') as f, open(outfile, 'w') as out:
        for line in f:
            index, text = line.split("\t")
            out.write(index, tag(text, function, eos))

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
    parser.add_argument('-f' '--file', help='type of the file, use c for corpora, f for single file, and n for nbest file', type=str, choces='cfh', default='f')
    parser.set_defaults(eos=False)
    parser.set_defaults(recursive=False)
    args = parser.parse_args()
    with concraft.Server() as server:
        client = concraft.Client(server.get_port())
        function = {'l': client.to_lemmas, 't': client.to_pos_tags, 'p': client.to_pos, 'g': client.to_gnc}[args.tokens]
        if args.type == c:
            tag_recursively(args.input, function , args.eos)
        elif args.type == n:
            tag_nbest(args.input, args.output, function)
        else:
            tag_file(args.input, args.output, function, args.eos)
