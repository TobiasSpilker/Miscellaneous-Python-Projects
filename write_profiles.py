"""
Read a directory of multilingual files and save 
ngram frequency tables for later use
"""
import os

tijdelijk = os.listdir('./datafiles/training')

def make_profiles(filepath, n, maxsize):
    #loopt door de filenamen en splits encoding en land naam op
    training_names = []
    for i in filepath:
        temp = i.split('-')
        training_names.append(temp)
        
    #lijst de files
    