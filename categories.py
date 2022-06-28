# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 20:11:50 2022

@author: Tobias
"""

if __name__ == "__main__":
    
    import nltk
    import sys
    from nltk.corpus import brown
    from collections import Counter
    
    for x in sys.argv[1:]:
        print(x, end=" ")
        
        #creates the lists:
        lijstje = [tag for (word, tag) in brown.tagged_words(tagset="universal") if word.lower() == x]
        myvar = set(lijstje)
   
        for x in myvar:
            i = 0
            for y in lijstje:
                if y==x: #checks of they match
                    i += 1
            print(x, i, end=" ")
            
        print()
    