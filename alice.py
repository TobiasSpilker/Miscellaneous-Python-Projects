import re
from nltk.corpus import gutenberg


def Myfunction():  
    """
    Takes all the instances of the word 'Alice' and prints the frequencies
    of the words following this in order. It will do this for the 5 most
    common words.
    """
    words = []

    for w in gutenberg.words("carroll-alice.txt"):
        words.append(w)

    words = [w.lower() for w in words if re.search(r'\w', w)]
    
    i = 0
    lijst = []
    for w in words:
        i += 1
        if (w == "alice"):
            lijst.append(words[i + 1])

    k = 0
    biebje = {}
    for w in lijst:
        for a in lijst:
            if w == a:
                k += 1
        biebje[w] = k
        k = 0  

    sortedbieb = sorted(biebje.items(), key=lambda x:x[1])
    sortdict = dict(sortedbieb)

    sortedlist = []
    for x in sortdict.keys():
        sortedlist.append(x + ' ' + str(sortdict[x]))
    
    
    finall =  sortedlist[-5:]
    
    
    for x in reversed(finall):
        print(x)