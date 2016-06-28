import argparse
import distance
import random
import time
from utils import read_unigrams, read_hypotheses
from collections import defaultdict

def append_mock_hypotheses(hypo): 
    for index, lines in hypo.items():
        line = lines[0].strip().split()
        hypo[index].append(' '.join(line) + '\n')

def shuffle(line):
    return random.sample(line, len(line))

def remove_words(line, probability=0.3):
    return [word if random.random() > probability else '' for word in line]

def substitute_words(line, fraction=0.3): 
    return [word if random.random() > probability else substitute(word) for word in line]

def substitute(word):
    global unigrams
    similar = [word for distance, word in sorted(distance.ifast_comp(word, unigrams))][1:]
    return word if not similar else random.choice(similar)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    args = parser.parse_args()

    time_before = time.time()
    unigrams = read_unigrams('unigrams')
    hypo = read_hypotheses(args.input)
    generate_mock_hypotheses(hypo)
    write_hypotheses(args.input, hypo)
    time_after = time.time()
    print("Elapsed time: {0}".format(time_after-time_before))
