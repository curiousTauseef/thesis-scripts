import concraft
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='path to the input file', type=str)
    parser.add_argument('output', help='path to the output file', type=str)
    parser.add_argument('-t', '--tokens', help='type of the output tokens, use p for raw POS, t for POS with tags and l for lemmas (default)', type=str, choices='gplt', default='l')
    args = parser.parse_args()
    with concraft.Server() as server:
        client = concraft.Client(server.get_port())
        mapping = {'l': client.to_lemmas, 't': client.to_pos_tags, 'p': client.to_pos, 'g': client.to_gnc}
        with open(args.input, 'r') as infile, open(args.output, 'w') as out:
            for line in infile:
                out.write(mapping[args.tokens](line).encode('UTF-8') + "\n")
