import os
import re
import signal
import socket
import subprocess
from retry import retry
from collections import OrderedDict
from utils import extract_gnc

PATH_TO_CONCRAFT = '~/.cabal/bin'

class Server:
    def __enter__(self):
        self.port = self.find_free_port()
        self.server = self.start_server()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        os.killpg(os.getpgid(self.server.pid), signal.SIGTERM)

    def find_free_port(self):
        sock = socket.socket()
        sock.bind(('', 0))
        port = sock.getsockname()[1]
        return port

    def start_server(self):
        command = "{0}/concraft-pl server {0}/model.gz --port {1}".format(PATH_TO_CONCRAFT, self.port)
        server = subprocess.Popen(command, shell=True, preexec_fn=os.setsid)
        return server
        
    def get_port(self):
        return self.port

class Client:
    def __init__(self, port):
        self.port = port

    @retry(subprocess.CalledProcessError, delay=10)
    def call_concraft(self, sentence):
        self.write_to_file(sentence)
        command = "{0}/concraft-pl client --port {1} < input".format(PATH_TO_CONCRAFT, self.port)
        return subprocess.check_output(command, shell=True).decode('utf-8')

    def to_lemmas(self, sentence):
        parsed = self.parse(self.call_concraft(sentence))
        return ' '.join([value[1] for value in parsed])

    def to_gnc(self, sentence):
        parsed = self.parse(self.call_concraft(sentence))
        return ' '.join([extract_gnc(value[2].split(':')) for value in parsed])

    def to_pos(self, sentence):
        parsed = self.parse(self.call_concraft(sentence))
        return ' '.join([value[2].split(':')[0] for value in parsed])

    def to_pos_tags(self, sentence):
        parsed = self.parse(self.call_concraft(sentence))
        return ' '.join([value[2] for value in parsed])

    def parse(self, concraft_output):
        parsed = []
        for line in concraft_output.split('\n'):
            if self.is_word(line):
                parsed.append([line.split()[0]])
            elif line:
                if len(parsed[-1]) == 1:
                    parsed[-1].extend((self.extract_lemma(line), self.extract_tags(line)))
        return parsed

    def extract_lemma(self, disamb):
        return disamb.split()[0].lower()

    def extract_tags(self, disamb):
        return disamb.split()[1].lower()

    def is_word(self, line):
        return line and not line.startswith('\t')

    def write_to_file(self, sentence):
        with open('input', 'w') as input:
            input.write(sentence)
