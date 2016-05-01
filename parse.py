import concraft
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.add_argument("input", help="path to the input file", type=str)
    args = parser.add_argument("output", help="path to the output file", type=str)
    args = parser.add_argument("-t", "--tokens", help="type of the output tokens, use p for POS tags and l for lemmas (default)", type=str, choices='pl', default='l')
    parser.parse_args()
    server = concraft.Server()
    port = server.get_port()
    client = concraft.Client(port)
