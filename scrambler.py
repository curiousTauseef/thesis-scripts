import argparse
import random

def shuffle(line):
    return ' '.join(random.shuffle(line.split()))

def shuffle_file(filename):
    with open(filename, 'r') as infile:
        with open(filename + '_shuffled', 'w') as shuffled:
            for line in infile:
                shuffled.write(line)
                shuffled.write(shuffle(line))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    args = parser.parse_args()
    shuffle_file(args.input)
