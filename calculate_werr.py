import operator
import argparse
from distance import levenshtein
from collections import defaultdict
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

def calculate_werr(reference, hypothesis):
    distance = levenshtein(reference.strip().split(), hypothesis.strip().split()) 
    return distance/len(reference.split())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('output', help='path to the RNN language model output file', type=str)
    parser.add_argument('nbest', help='path to the nbest list', type=str)
    parser.add_argument('-d', '--debug', help='debug level', type=int, default=0, choices=[0, 1, 2])
    parser.add_argument('-p', '--plain', help='plain text n-best file', type=str, default='data/test/nbest_plain')
    args = parser.parse_args()
    plain_nbest = read_nbest_list(args.plain)
    nbest = read_nbest_list(args.nbest)
    logprobs = read_logprobs(args.output)
    werr_total = 0
    num_hypo = 9
    for index in nbest:
        reference = plain_nbest[index][0].strip()
        hypotheses = nbest[index][1:]
        scores = logprobs[(index-1)*num_hypo+1:(index)*num_hypo]
        scores = list(zip(hypotheses, scores))
        (best_index, (hypothesis, best_logprob)) = max(list(enumerate(scores)), key=lambda x : x[1][1])
        best_hypothesis = plain_nbest[index][best_index+1].strip()
        werr = calculate_werr(reference, plain_nbest[index][best_index+1])
        werr_total += werr
        if args.debug == 2:
            for hypothesis, logprob in scores:
                print("{0}: {1}".format(hypothesis.strip(), logprob))
        if args.debug > 0:
            print("TRUE: {0}\nBEST: {1}\nPROB: {2}\nWERR: {3}\n\n".format(reference, best_hypothesis, best_logprob, werr))
    print("Total WERR: {}".format(100*(werr_total/len(nbest))))
