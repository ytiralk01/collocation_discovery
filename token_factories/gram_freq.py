__author__ = 'kafuinutakor'

import json
from nltk.util import ngrams
from textmining import simple_tokenize as gram_tokenize, stopwords
import simplejson
import sys
sys.path.append('../')
from text_cleaner.text_cleaner import TextCleaner


class GramFreq:
    def __init__(self, n):
        """
        tracks the frequency distribution; n is the length of the desired grams to be computed and indexed
        """
        self.freq = {}
        self.n = n
        self.text_cleaner = TextCleaner()

    def indexer(self, document):
        """
        tokenizes a document, computes n-grams from that token stream and moves the computed n-grams to the freq
        """
        # clean and tokenize the incoming text
        # natural language tokenize and then filter out stop words
        tokens = filter(lambda x: x not in stopwords, gram_tokenize(self.text_cleaner.clean(document)))
        # create sequence of n-grams; n is argument
        grams = set([i for i in ngrams(tokens, self.n)])
        for gram in grams:
            self.freq[' '.join(gram)] = self.freq.get(' '.join(gram), 0) + 1

    def dump(self, filename):
        """
        dumps the computed freq dict to disk as a JSON string
        """
        with open(filename, 'w') as outfile:
            json.dump(self.freq, outfile)

    @staticmethod
    def load(filename):
        """
        static method to load a previously computed freq dict from disk and use in analyses, etc.
        """
        with open(filename, 'r') as infile:
            data = simplejson.loads(infile.read())
        return data

