__author__ = 'kafuinutakor'

import json
from textmining import simple_tokenize_remove_stopwords as tokenize
import simplejson
import sys
sys.path.append('../')
from text_cleaner.text_cleaner import TextCleaner


class TermFreq:
    def __init__(self):
        """
        tracks the frequency distribution
        """
        self.freq = {}
        self.text_cleaner = TextCleaner()

    def indexer(self, document):
        """
        tokenizes a document and moves term to frequency distribution
        """
        # clean and tokenize the incoming text
        tokens = set(tokenize(self.text_cleaner.clean((document))))
        for token in tokens:
            self.freq[token] = self.freq.get(token, 0) + 1

    def dump(self, filename):
        """
        dumps the computed freq to disk as a JSON string
        """
        with open(filename, 'w') as outfile:
            json.dump(self.freq, outfile)

    @staticmethod
    def load(filename):
        """
        static method to load a previously computed freq from disk and use in analyses, etc.
        """
        with open(filename, 'r') as infile:
            data = simplejson.loads(infile.read())
        return data