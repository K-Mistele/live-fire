import numpy as np
import random as rm
from random_markov_generator import r_markov_generator
from probabilistic_markov_generator import p_markov_generator
from os import listdir

# get speeches from text files. these will be the data for the markov chains
trump = open("text_samples/trump_speeches.txt", encoding="utf8").read()
francis = open("text_samples/francis_speeches.txt", encoding="utf8").read()
caffeine = open("text_samples/caffeine_effects.txt", encoding="utf8").read()
MLK = open("text_samples/MLK_I_have_a_dream.txt", encoding="utf8").read()
#NOTE: need more Francis text. right now there's a lot more trump in it than francis.
# list of any data resources that you want to add. can add/remove to tune the bot.
print("Available files:")
print("****************")
# display available files
available_files = listdir("text_samples")
available_texts = []
for file in available_files:
    if ".txt" in file:
        available_texts.append(file[:-4])
print("\n".join(available_texts))
print("****************")
chosen_files = []

# let use choose which files to import
while True:
    m_file = input("Which file would you like to import?")
    if m_file in available_texts:
        chosen_files.append(m_file)
        another = input("Would you like to import another file?")
        if "yes" in another or another in "yes":
            continue
        else:
            break
    else:
        print("File not available.")
        continue
# import user-selected maps:
data = []
for item in chosen_files:
    data.append(open(f"text_samples/{item}.txt", encoding="utf8").read())
    print(f"Imported {item}.txt")




#create a new generator with trump and francis data files as args
generator = p_markov_generator(data)
#generate and print the data string
print("*********************************************")
print("Speech bot says:")
generator.print_chain(generator.generate_chain())

# His finest moment?
# Faso. They look at the result of the next year. With the pressure to
# tell you proud of every single last time deported Mexican Government is
# very well, you have a fortune for the first of it, and I was murdered plenty.
#TODO:
# option in-terminal to select what resources you want (see seeker-of-the-sword code)
# create a global library class and json storage.
    # will need methods to load and incorporate new text files into it
    # methods to get info from other sources too: reddit etc.

# way to integrate with reddit bots:
    # need a way to harvest text from subreddits, store
    # need a way to then load in and analyze that text, possible use global library?
    # have text be able to be sent to the reddit bot; like an importable service
    # resources and chains then must be usable by reddit bots.
# integration with twitter?