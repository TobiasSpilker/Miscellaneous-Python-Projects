# -*- coding: utf-8 -*-
"""
Created on Tue May  3 21:35:23 2022

@author: Tobias
"""

def split(word):
    return [char for char in word]

def nth_char(getal, tekst):  
    
    if (getal < len(tekst)):
        char_lijst = split(tekst)
        return char_lijst[getal]
    else:
        return None
    
def nth_word(getal, tekst):
     
    if (getal < len(tekst.split())):
        woord_lijst = tekst.split()
        return woord_lijst[getal]
    else:
        return None

def nth_of_mth(char_index, word_index, text):
    
    if (word_index < len(text.split())):
        woordje = nth_word(word_index, text)
        
        if(char_index < len(woordje)):
            karaktertje = nth_char(char_index, woordje)  
            print('Character ' + str(char_index) + ' of word ' + str(word_index) + ' is ' + str(karaktertje))
            
        else:
            print('Oops!')
        
    else:
        print('Oops!')