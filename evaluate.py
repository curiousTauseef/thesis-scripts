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

def get_score_function(lm):
    def score_function(hypothesis):
        return lm.total_logprob_strings(hypothesis.strip().split())
    return score_function

def calculate_werr(reference, hypothesis):
    distance = levenshtein(reference.strip().split(), hypothesis.strip().split()) 
    return distance/len(reference.split())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('lm', help='path to the language model file', type=str)
    parser.add_argument('test', help='path to the test file', type=str)
    parser.add_argument('-d', '--debug', help='debug level', type=int, default=0, choices=[0, 1, 2])
    args = parser.parse_args()
    lm = LM(args.lm.encode('utf-8'))
    score = get_score_function(lm)
    nbest = read_nbest_list(args.test)
    werr_total = 0
    for index in nbest:
        reference = nbest[index][0].strip()
        hypotheses = nbest[index][1:]
        scores = [(hypothesis.strip(), score(hypothesis)) for hypothesis in hypotheses] 
        best_hypothesis, best_logprob = max(scores, key=operator.itemgetter(1))
        werr = calculate_werr(reference, best_hypothesis)
        werr_total += werr
        if args.debug == 2:
            for hypothesis, logprob in scores:
                print("{0}: {1}".format(hypothesis, logprob))
        if args.debug > 0:
            print("TRUE: {0}\nBEST: {1}\nPROB: {2}\nWERR: {3}\n\n".format(reference, best_hypothesis, best_logprob, werr))
    print("Total WERR: {}".format(100*(werr_total/len(nbest))))
