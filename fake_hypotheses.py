import argparse
import random
from collections import defaultdict

def add_shuffled(hypo):
    for index, lines in hypo.items(): 
        line = lines[0].strip().split()
        random.shuffle(line)
        hypo[index].append(' '.join(line) + '\n')

def read_file(filename):
    hypo = defaultdict(list)
    with open(filename, 'r') as f:
        for index, line in enumerate(f):
            hypo[index+1].append(line)
    return hypo

def write_to_file(filename, hypo):
    with open(filename + '_hypotheses', 'w') as out:
        for index in sorted(hypo):
            lines = hypo[index]
            for line in lines:
                out.write("{0} {1}".format(index, line))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    args = parser.parse_args()

    hypo = read_file(args.input)
    add_shuffled(hypo)
    write_to_file(args.input, hypo)
