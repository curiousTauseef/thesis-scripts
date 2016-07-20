import argparse
import random

def split(filename, treshold):
    treshold = max(treshold, 1-treshold)
    with open(filename, 'r') as infile:
        with open(filename + '_train', 'w') as train, open(filename + '_validate', 'w') as test:
            for line in infile:
                if random.random() > treshold:
                    test.write(line)
                else:
                    train.write(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    parser.add_argument('-t', '--treshold', help='between 0 and 1, the training set will always be the bigger one, i.e. 0.2 and 0.8 are equivalent', type=float, default=0.8)
    args = parser.parse_args()
    split(args.input, args.treshold)
