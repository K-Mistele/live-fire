import numpy as np
import random as rm
from random_markov_generator import r_markov_generator
from probabilistic_markov_generator import p_markov_generator

# get speeches from text files. these will be the data for the markov chains
trump = open("text_samples/trump_speeches.txt", encoding="utf8").read()
francis = open("text_samples/francis_speeches.txt", encoding="utf8").read()
#NOTE: need more Francis text. right now there's a lot more trump in it than francis.
# list of any data resources that you want to add. can add/remove to tune the bot.
data = [trump, francis]

#create a new generator with trump and francis data files as args
generator = p_markov_generator([trump, francis])
#generate and print the data string
generator.print_chain(generator.generate_chain())

# His finest moment?
# Faso. They look at the result of the next year. With the pressure to
# tell you proud of every single last time deported Mexican Government is
# very well, you have a fortune for the first of it, and I was murdered plenty.