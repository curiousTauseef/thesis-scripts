import re
import concraft
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    parser.add_argument('output', help='path to the output file', type=str)
    parser.add_argument('-t', '--tokens', help='type of the output tokens, use p for raw POS, t for POS with tags and l for lemmas (default)', type=str, choices='gplt', default='l')
    parser.add_argument('--eos', dest='eos', action='store_true')
    parser.add_argument('--no-eos', dest='eos', action='store_false')
    parser.set_defaults(feature=True)
    args = parser.parse_args()
    with concraft.Server() as server:
        client = concraft.Client(server.get_port())
        mapping = {'l': client.to_lemmas, 't': client.to_pos_tags, 'p': client.to_pos, 'g': client.to_gnc}
        with open(args.input, 'r') as infile, open(args.output, 'w') as out:
            for line in infile:
                if args.eos:
                    line = re.sub(r'|'.join(map(re.escape, ['<s> ', ' </s>'])), '', line)
                mapped = mapping[args.tokens](line).encode('UTF-8')
                if args.eos:
                    mapped = '<s> ' + mapped + ' </s>'
                out.write(mapped + "\n")
