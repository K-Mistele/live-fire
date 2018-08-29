import numpy as np
import random as rm

# get speeches from text files. these will be the data for the markov chains
trump = open("text_samples/trump_speeches.txt", encoding="utf8").read()
francis = open("text_samples/francis_speeches.txt", encoding="utf8").read()
#NOTE: need more Francis text. right now there's a lot more trump in it than francis.
# list of any data resources that you want to add. can add/remove to tune the bot.
data = [francis, trump]

# split each text into a list of words
corpus_data =[corpus.split() for corpus in data]
# a dictionary for all word pairs
word_dict = {}

# function to return pairs of words
def make_word_pairs(corpus):
    # generate pairs of words form the text
    for i in range(0, len(corpus)-1):
        yield(corpus[i], corpus[i+1])

# for each corpus, update the word pair dictionary
for corpus in corpus_data:
    # store word pairs
    pairs = make_word_pairs(corpus)

    # fill dictionary with word pairings. if a word is paired with multiple others, a list is created.
    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

# select first word randomly from the word dictionary, make sure it is capitalized
first_word = np.random.choice(list(word_dict.keys()))
while first_word.islower():
    first_word = np.random.choice(list(word_dict.keys()))
# the beginning of the sentence word chain
chain = [first_word]
# the number of words in the sentence: randomly chosen
n_words = rm.randint(15,200)

# create the word chain to a good length
for i in range(1, n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

# and then make sure it ends with a punctuation mark.
while chain[-1][-1] != "." and chain[-1][-1] != "?" and chain[-1][-1] != "!":
    chain.append(np.random.choice(word_dict[chain[-1]]))


print(" ".join(chain))