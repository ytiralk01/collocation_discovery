__author__ = 'kafuinutakor'

import unicodedata


class TextCleaner:
    def __init__(self):
        pass

    def flatten_char(self, text):
        if not text:
            return ''
        if isinstance(text, unicode):
            # if the input is unicode, then normalize to flatten characters
            flat_text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore')
        elif isinstance(text, str):
            # if it's a string, cast as unicode prior to flattening
            text = unicode(text, 'utf-8', 'ignore')
            # flatten characters
            flat_text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore')
        else:
            flat_text = text
        return flat_text

    def clean(self, document):
        """
        main cleaning method; removes excess white space, flattens char encoding, and normalizes all text to lower case
        """
        document = ' '.join([i.lower() for i in document.split()])
        return self.flatten_char(document)  # return flattened char text
