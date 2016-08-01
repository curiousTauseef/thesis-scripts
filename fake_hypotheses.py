import argparse
import distance
import numpy as np
import random
import time
from collections import defaultdict

def append_mocks(hypotheses): 
    for index, lines in hypotheses.items():
        line = lines[0].strip().split()
        for probability in np.arange(0.2, 1, 0.1):
            hypotheses[index].append(reduce(substitute_words(line, probability)))

def reduce(mock):
    return ' '.join(filter(None, mock)) + '\n'

def substitute_words(line, probability): 
    return [word if random.random() > probability else substitute(word) for word in line]

def substitute(word):
    global unigrams
    similar_words = [unigram for distance, unigram in sorted(distance.ifast_comp(word, unigrams)) if distance <= 2]
    return word if not similar_words else random.choice(similar_words)

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

def read_unigrams(filename, treshold=5000):
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
