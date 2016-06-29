import argparse
import random

def sample(filename, size):
    with open(filename, 'r') as f, open(filename + '_sample', 'w') as out:
        for line in random.sample(f.readlines(), size):
            out.write(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    parser.add_argument('-s', '--size', help='number of lines in the sample', type=int, default=1000)
    args = parser.parse_args()
    sample(args.input, args.size)
