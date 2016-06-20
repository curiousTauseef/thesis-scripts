from srilm import LM
import argparse

if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument('path_to_lm', help='path to the language model file', type=str)
    #args = parser.parse_args()
    lm = LM('./text_plain_full_novocab.lm')
    with open('sentences') as sentences:
        for line in sentences:
            print("{0}: {1}".format(line.strip(), lm.total_logprob_strings(line.split())))

    context = [lm.vocab.intern(w) for w in ["panie", "szanowny"]]
    best_idx = None
    best_logprob = -1e100
    for i in xrange(lm.vocab.max_interned() + 1):
        logprob = lm.logprob(i, context)
        if logprob > best_logprob:
            best_idx = i
            best_logprob = logprob
    best_word = lm.vocab.extern(best_idx)
    print "Max prob continuation: %s (%s)" % (best_word, best_logprob)
