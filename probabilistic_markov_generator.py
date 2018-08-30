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
                    self.word_dict[word1]["words"].append(word2)
                #else, create a new key/value pair
                else:
                    self.word_dict[word1] = {"words":[word2],
                                             "probabilities":[]}

        # go through each list of words and remove duplicates, create probabilities
        for first_word, following in self.word_dict.items():
            #TODO: code for probability sorting
            if len(following["words"]) > 1:
                following["probabilities"] = []
                new_words = []
                for word in following["words"]:
                    if word not in new_words:
                        # calculate probability (i.e. prevelance) of each word in the list
                        probability = following["words"].count(word)/len(following["words"])
                        # add this to corresponding probability list
                        following["probabilities"].append(probability)
                        # add the word to new words IF IT HAS NOT ALREADY BEEN ADDED
                        new_words.append(word)
                # use new_words as the old words list. This makes it so that words and probabilities match up without redundancy.
                following["words"] = new_words
            else:
                following["probabilities"] = [1]

