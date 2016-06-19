from srilm import LM
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path_to_lm', help='path to the language model file', type=str)
    args = parser.parse_args()
    lm = LM(args.path_to_lm)
    logprob = lm.total_logprob_strings(["ala", "ma", "kota"]) 
