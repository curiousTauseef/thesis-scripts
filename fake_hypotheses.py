import argparse
import distance
import random
import time
from utils import write_hypotheses, read_unigrams, read_hypotheses

def append_mocks(hypotheses): 
    for index, lines in hypotheses.items():
        line = lines[0].strip().split()
        hypotheses[index].extend((reduce(mock) for mock in (substitute_words(line), shuffle(line), remove_words(line))))

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
    similar = [word for distance, word in sorted(distance.ifast_comp(word, unigrams)) if distance > 0]
    return word if not similar else random.choice(similar)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    args = parser.parse_args()

    unigrams = read_unigrams('unigrams')
    hypotheses = read_hypotheses(args.input)
    append_mocks(hypotheses)
    write_hypotheses(args.input, hypotheses)
