import random

def split(filename, treshold):
    treshold = max(treshold, 1-treshold)
    with open(filename, 'r') as f:
        with open(filename + '_train', 'w') as train, open(filename + '_test', 'w') as test:
            for line in f:
                if random.random() > treshold:
                    test.write(line)
                else:
                    train.write(line)

if __name__ == '__main__':
    split('text', 0.8)

