#### MODULE!! ####
import re

def prepare(text):
    text = re.sub(r"!\?\",.()<>", " ", text).split()
    print(text)
    return text
    pass


def ngram_table():
    """
    
    """
    pass

def read_ngrams():
    """
    
    """
    pass

def write_ngrams():
    """
    
    """
    pass

def cosine_similarity():
    """
    
    """
    pass