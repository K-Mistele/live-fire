import numpy as np
import random as rm
from random_markov_generator import r_markov_generator as r_generator

class p_markov_generator(r_generator):

    # NOTE: ALL OTHER METHODS ARE BEING COPIED FROM r_generator
    def generate_dictionary(self, corpus_data):
        for corpus in corpus_data:
            pairs =self.make_word_pairs(corpus)

            for word1, word2 in pairs:
                # if word is already in dict, add second word to list
                if word1 in self.word_dict.keys():
                    #TODO: this is where to add a conditional about creating a probability
                    self.word_dict[word1].append(word2)
                #else, create a new key/value pair
                else:
                    self.word_dict[word1] = [word2]
