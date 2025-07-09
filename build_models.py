4#to train and pickle classifiers
from pyexpat import features
import random
import os
from custom_chunker import ConsecutiveNPChunker
import features

from nltk.corpus import conll2002 as conll
training = conll.chunked_sents("ned.train")[:100]

test_nl_NER = ConsecutiveNPChunker(features.test_features, training)

import pickle
output = open("test_features.pickle", "wb")
pickle.dump(test_nl_NER, output)
output.close()

if __name__ == "__main__":
    #Commence Operation: Command Line Interface
    all_feature_maps = [m for m in dir(features) if m[:2] != '__']
    algorithms = ["NaiveBayes", "DecisionTree", "IIS", "GIS"]
    model_weapon = None
    
    # Choose your own adventure section
    print("\nHi there weary trav'ler, I, Bartholomeus of the Classifiers Burrough, heard you want to work with my classifiers.")
    print("You seem like you would want to train a model...\n")
    print("\tref\tFeature Map function")

    #print all the possible feature maps
    for i, fm in enumerate(all_feature_maps):
        print(f"\t{i}\t{fm}")
    feature_map = all_feature_maps[int(input("What features might you want on your Model-weapon to slay this Training Monster with? [one of ref]: -> "))]

    print(f"\nAt last, you chose \"{feature_map}\", a {random.choice(['fine', 'great', '...', 'distinguished', 'marvelous', 'bold'])} choice.")

    print()
    print("The default algorithm on the sword meant for slaying the training beast is a hilt by the name of 'NaiveBayes'.")
    changealg = input("Though I'd recommend 'NaiveBayes' to anyone, I can respect a fighter willing to wield another algorithm.\n\nDo you want to switch to another algorithm? [y|n] -> ")
    if changealg.lower() == 'y':
        print("\tref\tAlgorithms")
        for i, alg in enumerate(algorithms):
            print(f"\t{i}\t{alg}")

        algnum = input("What algorithm might you want wield your sword with to slay this Training Monster with? [one of ref]: -> ")

        while len(algnum) != 1 or int(algnum) >= len(algorithms) or int(algnum) < 0:
            print("\nThat's not an existing algorithm! Please try again.")
            algnum = input("What algorithm might you want wield your sword with to slay this Training Monster with? [one of ref]: -> ")
        
        algorithm = algorithms[int(algnum)]

        print("Please wait until the ovens of Moria have smithed your weapon...")
        model_weapon = ConsecutiveNPChunker(features.test_features, training, algorithm)
    else:
        model_weapon = ConsecutiveNPChunker(features.test_features, training)

    picklename = input("\nWhat do you want to call your pickle? (Be sure it doesn't already exist)-> ")

    # PICKLING 
    training = conll.chunked_sents("ned.train")

    # Make the models directory
    if 'models' not in os.listdir():
        os.mkdir('./pickle-jar')

    output = open(f"./pickle-jar/{picklename}.pickle", "wb")
    pickle.dump(model_weapon, output)
    output.close()

    print("Model has been succesfully pickled! Go slay that dragon!")