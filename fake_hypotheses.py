import argparse
import distance
import random
import time
from collections import defaultdict

def append_mocks(hypotheses): 
    for index, lines in hypotheses.items():
        line = lines[0].strip().split()
        hypotheses[index].extend((reduce(mock) for mock in (substitute_words(line, 0.1), substitute_words(line, 0.3), substitute_words(line, 0.5), substitute_words(line, 0.7), substitute_words(line, 0.7))))

def reduce(mock):
    return ' '.join(mock) + '\n'

def shuffle(line):
    return random.sample(line, len(line))

def remove_words(line, probability=0.3):
    return [word for word in line if random.random() > probability]

def substitute_words(line, probability=0.3): 
    return [word if random.random() > probability else substitute(word) for word in line]

def substitute(word):
    global unigrams
    similar = [word for distance, word in sorted(distance.ifast_comp(word, unigrams))]
    return word if not similar else random.choice(similar)

def write_hypotheses(filename, hypo):
    with open(filename + '_hypotheses', 'w') as out:
        for index in sorted(hypo):
            for line in hypo[index]:
                out.write("{0}\t{1}".format(index, line))

def read_hypotheses(filename):
    hypo = defaultdict(list)
    with open(filename, 'r') as f:
        for index, line in enumerate(f):
            hypo[index+1].append(line)
    return hypo

def read_unigrams(filename, treshold=1000):
    with open(filename, 'r') as f:
        unigrams = [line.split()[0] for line in f if int(line.split()[1]) > treshold]
    return unigrams

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    parser.add_argument('-u', '--unigrams', help='path to the input file', type=str, default='data/full/unigrams')
    args = parser.parse_args()

    unigrams = read_unigrams(args.unigrams)
    hypotheses = read_hypotheses(args.input)
    append_mocks(hypotheses)
    write_hypotheses(args.input, hypotheses)
