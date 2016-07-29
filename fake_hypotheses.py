import argparse
import distance
import random
import time
from collections import defaultdict

def append_mocks(hypotheses, n): 
    for index, lines in hypotheses.items():
        line = lines[0].strip().split()
        for i in range(n):
            deletion_probability = 0.25*i/n 
            insertion_probability = 0.25*i/n 
            substitution_probability = 0.5*i/n 
            line = delete_words(line, deletion_probability) 
            line = substitute_words(line, substitution_probability) 
            line = add_words(line, deletion_probability) 
            hypotheses[index].append(reduce(line))
        #hypotheses[index].extend((reduce(mock) for mock in (substitute_words(line, 0.1), substitute_words(line, 0.3), substitute_words(line, 0.5), substitute_words(line, 0.7), substitute_words(line, 0.7))))

def reduce(mock):
    return ' '.join(mock) + '\n'

def delete_words(line, probability):
    return [word for word in line if random.random() > probability]

def substitute_words(line, probability): 
    return [word if random.random() > probability else substitute(word) for word in line]

def insert_words(line, probability):
    return line

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
    append_mocks(hypotheses, 5)
    write_hypotheses(args.input, hypotheses)
