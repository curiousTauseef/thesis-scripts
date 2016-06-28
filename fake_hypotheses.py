import argparse
import distance
import random
import time
from utils import read_unigrams, read_hypotheses
from collections import defaultdict

def shuffled(line):
    line = lines[0].strip().split()
    random.shuffle(line)
    return ' '.join(line) + '\n'

def substituted(line): 
    line = lines[0].strip().split()
    n = len(line)//3 #substitute roughly one third of words
    for position, word in random.sample(list(enumerate(line)), n):
        line[position] = substitute(word)
    return ' '.join(line) + '\n'

def substitute(word):
    global unigrams
    similar = [word for distance, word in sorted(distance.ifast_comp(word, unigrams))][1:]
    return word if not similar else random.choice(similar)

def substitute_words(hypo): 
    for index, lines in hypo.items():
        line = lines[0].strip().split()
        n = len(line)//3 #substitute roughly one third of words
        for position, word in random.sample(list(enumerate(line)), n):
            line[position] = substitute(word)
        hypo[index].append(' '.join(line) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    args = parser.parse_args()

    time_before = time.time()
    unigrams = read_unigrams('unigrams')
    hypo = read_hypotheses(args.input)
    add_shuffled(hypo)
    substitute_words(hypo)
    write_hypotheses(args.input, hypo)
    time_after = time.time()
    print("Elapsed time: {0}".format(time_after-time_before))
