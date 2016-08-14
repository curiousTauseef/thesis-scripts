import argparse
from collections import defaultdict
from distance import levenshtein
import itertools
import math
import numpy as np
import operator
import random
from srilm import LM

def read_nbest_list(filename):
    nbest = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            index, text = line.split("\t")
            nbest[int(index)].append(text)
    return nbest

def read_logprobs(filename):
    with open(filename, 'r') as f:
        return [float(line) for line in f]

def wer(reference, hypothesis):
    distance = levenshtein(reference.strip().split(), hypothesis.strip().split()) 
    return distance/len(reference.split())

def log_hypothesis(debug, best_hypothesis, best_hypothesis_plain, scores, werr, reference):
    (best_text, best_logprob) = best_hypothesis
    if debug == 2:
        for hypothesis, logprob in scores:
            print("{0}: {1}".format(hypothesis.strip(), logprob))
    if debug > 0:
        print("TRUE: {0}\nBEST: {1}\nPROB: {2}\nWERR: {3}\n\n".format(reference, best_hypothesis_plain, best_logprob, werr))

def log(wer, linspace=None):
    if not linspace is None:
        werr = [wer[0]- w for w in wer] 
        for a, w in zip(linspace, werr):
            print("{0:.2f} {1}".format(a, w))
    else:
        print("Total WERR: {}".format(wer))

def find_best_hypothesis(scores):
    return max(list(enumerate(scores)), key=lambda x : x[1][1]) 

def log_linear_interpolate(lms, ams, alpha):
    return [alpha*lm + (1-alpha)*am for lm, am in zip(lms, ams)]

def calculate_wer(args, alpha=1):
    plain_nbest = read_nbest_list(args.plain)
    nbest = read_nbest_list(args.nbest)
    lm_logprobs = iter(read_logprobs(args.lm_prob))
    if args.am:
        am_logprobs = iter(read_logprobs(args.am_prob))
    else:
        am_logprobs = itertools.repeat(0) #God help me 
    total_wer = 0
    for index in nbest:
        reference = plain_nbest[index][0].strip()
        next(lm_logprobs)
        next(am_logprobs)
        hypotheses = nbest[index][1:]
        lms = [next(lm_logprobs) for h in hypotheses]
        ams = [next(am_logprobs) for h in hypotheses]
        probs = log_linear_interpolate(lms, ams, alpha)
        scores = list(zip(hypotheses, probs))
        best_index, best_hypothesis = find_best_hypothesis(scores)
        best_hypothesis_plain = plain_nbest[index][best_index+1].strip()
        current_wer = wer(reference, best_hypothesis_plain)
        total_wer += current_wer
        log_hypothesis(args.debug, best_hypothesis, best_hypothesis_plain, scores, current_wer, reference)
    return 100*(total_wer/len(nbest))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('lm_prob', help='path to the language model probabilities', type=str)
    parser.add_argument('nbest', help='path to the nbest list', type=str)
    parser.add_argument('-a', '--am_prob', help='path to the acoustic probabilities', type=str, default='out')
    parser.add_argument('-d', '--debug', help='debug level', type=int, default=0, choices=[0, 1, 2])
    parser.add_argument('-p', '--plain', help='plain text n-best file', type=str, default='data/test/nbest_plain')
    parser.add_argument('--am', dest='am', action='store_true')
    parser.add_argument('--no-am', dest='am', action='store_false')
    parser.set_defaults(am=False)
    args = parser.parse_args()
    if args.am:
        linspace = np.arange(0, 1, 0.05)
        wer = [calculate_wer(args, alpha) for alpha in linspace]
        log(wer, linspace)
    else:
        log(calculate_wer(args))
