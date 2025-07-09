import pickle
import os
from nltk.corpus import conll2002 as conll

# print(os.listdir('./pickle-jar'))

trytoselectthemelol = input("Would you like to select the Pirate Theme for the evaluation? [y|n] -> ")
print("\nYou've selected the Pirate-Theme!\nArrrrrrrr Matey! Welcome Aboard!!\n")

print("Legends say there is a mighty treasure chest on the bottom of this reef...")
print("""When I was just a rascal on a ship called 'The Slobberknocker' I was part of a crew hunting down merchant-ships,
filled to the brim with gold, silver and whale-oil. They retaliated with heavy cannonfire, so we fed them to the fishes!
Sadly, all the treasures that were bestowed on that ship, also went down to Davy Jones' locker before we could plunder.
That brings us to ye! Help me with the name of that ship, I know where it lies.
""")

picklejar = os.listdir('./pickle-jar')
print("\tref\tPickled Model Name")
for i, model in enumerate(picklejar):
    print(f"\t{i}\t{model}")
modelnum = input("What model do you want to evaluate? [one of ref] -> ")

while len(modelnum) != 1 or int(modelnum) >= len(picklejar) or int(modelnum) < 0:
    print("\nThat's not an existing algorithm! Please try again.")
    modelnum = input("What model do you want to evaluate? [one of ref] -> ")

model = picklejar[int(modelnum)]
ner = pickle.load(open(f"./pickle-jar/{model}", "rb"))

testing = conll.chunked_sents("ned.testa")
print(ner.evaluate(testing))

print("\nYou did it laddie! You are to be rewarded One Million Golden Doubloons!!")
