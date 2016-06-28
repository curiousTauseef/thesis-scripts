import argparse
import distance
import random
import time
from utils import read_unigrams, read_hypotheses
from collections import defaultdict

def generate_mock_hypotheses(hypo): 
    for index, lines in hypo.items():
        line = lines[0].strip().split()
        for position, word in random.sample(list(enumerate(line)), n):
            line[position] = substitute(word)
        hypo[index].append(' '.join(line) + '\n')

def shuffle(line):
    line = line.strip().split()
    random.shuffle(line)
    return ' '.join(line) + '\n'

def remove_words(line, percentage=0.3):
    line = line.strip().split()
    n = int(len(line)*(1-percentage))
    return ' '.join([word for index, word in sorted(random.sample(list(enumerate(line)), n))])

def substitute_words(line, percentage=0.3): 
    line = line.strip().split()
    n = int(len(line)*percentage)
    for position, word in random.sample(list(enumerate(line)), n):
        line[position] = substitute(word)
    return ' '.join(line) + '\n'

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
