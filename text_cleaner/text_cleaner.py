__author__ = "kafuinutakor"

import unicodedata


class TextCleaner:
    """handles and cleans text to avoid character encoding errors
    """
    def __init__(self):
        pass

    def normalize_text(self, text):
        if not text:
            return ""
        if isinstance(text, unicode):
            # if the input is unicode, then normalize to flatten characters
            return unicodedata.normalize("NFD", text).encode("ascii", "ignore")
        elif isinstance(text, str):
            # if it"s a string, cast as unicode prior to flattening
            text = unicode(text, "utf-8", "ignore")
            return unicodedata.normalize("NFD", text).encode("ascii", "ignore")

    def clean(self, text):
        """main cleaning method; clean spaces, lower case and normalize chars
        """
        text = " ".join([i.lower() for i in text.split()])
        return self.normalize_text(text)
