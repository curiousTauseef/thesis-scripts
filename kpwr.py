#requires Python >= 3.5
import xml.etree.ElementTree
import glob
import re

def parse(filename):
    root = xml.etree.ElementTree.parse(filename).getroot()
    for sentence in root.findall("sentence"):
        out = [token.find("orth").text for token in sentence.findall("tok")]
        if len(out) > 4:
            print(' '.join(out)))

path = '.'
for filename in glob.iglob(path + '/**/*.xml', recursive=True):
    parse(filename)
