import argparse
import random
from collections import defaultdict

def add_shuffled(hypo):
    for index, lines in hypo.items(): 
        line = lines[0].strip().split()
        random.shuffle(line)
        hypo[index].append(' '.join(line) + '\n')

def read_unigrams(filename):
    with open('unigrams', 'r') as uni:
        unigrams = [line.strip() for line in uni] 
    return unigrams

def substitute(word, unigrams):
    word_position = unigrams.index(word)
    lower_bound = max(0, word_position-5)
    upper_bound = min(len(unigrams), word_position-5)
    similar_words = unigrams[lower_bound:upper_bound]
    return random.choice(similar_words)

def substitute_words(hypo): 
    for index, lines in hypo.items():
        line = lines[0].strip().split()
        n = len(line)//3 #substitute roughly one third of words
        for position, word in random.sample(list(enumerate(line)), n):
            line[position] = substitute(word)
        hypo[index].append(' '.join(line) + '\n')

def read_hypotheses(filename):
    hypo = defaultdict(list)
    with open(filename, 'r') as f:
        for index, line in enumerate(f):
            hypo[index+1].append(line)
    return hypo

def write_hypotheses(filename, hypo):
    with open(filename + '_hypotheses', 'w') as out:
        for index in sorted(hypo):
            lines = hypo[index]
            for line in lines:
                out.write("{0} {1}".format(index, line))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    args = parser.parse_args()

    hypo = read_hypotheses(args.input)
    add_shuffled(hypo)
    substitute_words(hypo)
    write_hypotheses(args.input, hypo)

