def test_features(sentence, i, history):
    """Chunker features designed to test the Chunker class for correctness 
        - the POS tag of the word
        - the entire history of IOB tags so far
            formatted as a tuple because it needs to be hashable
    """ 
    word, pos = sentence[i]
    return { 
        "pos": pos,
        "whole history": tuple(history)
        
            }



def history(sentence, i, history):
    history = tuple(history)
    return history
 
def pos(sentence, i , history):
 word, pos = sentence[i]
 return pos 

            

def no_hist(sentence, i, history):
    """Chunker features designed to test the Chunker class for correctness 
        - the POS tag of the word
        - the entire history of IOB tags so far
            formatted as a tuple because it needs to be hashable
    """ 
    word, pos = sentence[i]
    return { 
        "pos": pos
            }

def features_compleet(sentence, i, history):
    pos = pos(sentence, i, history)
    history =  history(sentence, i, history)
    word = sentence[i]
    prev_cap_letter = Prev_Cap_let(sentence, i, history)
    Cap_letter = Cap_let(sentence, i, history)
    prev_word = Prev_word(sentence, i, history)
    prev_pos = Prev_POS(sentence, i, history)
    next_word = Next_Word(sentence, i, history)
    next_pos = Next_POS(sentence, i, history)
    HelewoordCap = Cap_Word(sentence, i, history)
    numberinword = Numb_Word(sentence, i, history)
    return{ pos, history, word, prev_cap_letter, Cap_letter, prev_word, prev_pos, next_word, next_pos, HelewoordCap, numberinword

    }

def features_vorige(sentence,i , history):
    pos = pos(sentence, i, history)
    history =  history(sentence, i, history)
    prev_word = Prev_word(sentence, i, history)
    prev_pos = Prev_POS(sentence, i, history)
    return {pos, history, prev_word, prev_pos}

def features_volgende(sentence,i , history):
    next_word = Next_Word(sentence, i, history)
    next_pos = Next_POS(sentence, i, history)
    pos = pos(sentence, i, history)
    history =  history(sentence, i, history)
    return{pos, history, next_word, next_pos}







def Prev_Cap_let(sentence, i, history):
    
    #Returns if the first letter of the previous word is a capital letter or not, thisfunction returns a boolean.    
    if i > 0:
     if sentence[i].isupper():
        return True        
    else:
        return False  


def Cap_let(sentence, i, history):
    """
    Returns if the first letter of a word is a capital letter or not, this
    function returns a boolean.
    """
    
    if sentence[i].isupper():
        return True
    else:
        return False

    
def Prev_word(sentence, i, history):
    """
    Returns the previous word
    """
    if i > 0:
        return sentence[i - 1]
    else:
        return None
    

def Prev_POS(sentence, i, history):
    """
    Returns the previous POS tag
    """
    if i > 0:
        word, pos = sentence[i - 1]
        return pos
    else:
        return None

def Next_Word(sentence, i, history):
    """
    Returns the next word
    """
    if i < len(sentence):   
        return sentence[i + 1]
    else:
        return None

def Next_POS(sentence, i, history):
    """
    Returns the next POS tag
    """
    if i < len(sentence):   
        word, pos = sentence[i + 1]
        return pos
    else:
        return None
    
def Cap_Word(sentence, i, history):
    """
    Returns a boolean, gives True when a word is capitalized. Otherwise false
    """
    if sentence[i] == sentence[i].upper():  
        return True
    else:
        return False
    
def Numb_Word(sentence, i, history):
    """
    Returns a boolean, gives True when a word contains a number, otherwise
    it returns False.
    """
    woordje = sentence[i]
    
    for char in woordje:
        if char.isdigit():
            return True
        else:
            return False