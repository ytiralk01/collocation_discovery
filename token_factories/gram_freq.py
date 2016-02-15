__author__ = 'kafuinutakor'

import json
from nltk.util import ngrams
from textmining import simple_tokenize as gram_tokenize, stopwords
import simplejson
from text_cleaner.text_cleaner import TextCleaner


class GramFreq:
    """provides the utility for basic corpus analytics; also supports advanced collocation mining abilities
    """
    def __init__(self, n):
        """tracks the frequency distribution; n is the length of the desired grams to be computed and indexed
        """
        self.n = n
        self.freq = {}
        self.text_cleaner = TextCleaner()

    def index(self, document):
        """tokenizes a document, computes n-grams from that token stream and moves the computed n-grams to the freq
        """
        # clean and tokenize the incoming text
        tokens = filter(lambda x: x not in stopwords, gram_tokenize(self.text_cleaner.clean(document)))
        # create sequence of n-grams; n is argument
        grams = set([i for i in ngrams(tokens, self.n)])
        for gram in grams:
            self.freq[' '.join(gram)] = self.freq.get(' '.join(gram), 0) + 1

    def dump(self, filename):
        """dumps the computed freq dict to disk as a JSON string
        """
        with open(filename, 'w') as outfile:
            json.dump(self.freq, outfile)

    def load(self, filename):
        """loads a previously computed freq dict from disk and use in analyses, etc.
        """
        with open(filename, 'r') as infile:
            self.freq = simplejson.loads(infile.read())


