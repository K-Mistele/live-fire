import numpy as np
import random as rm

class markov_generator():
    default_text_samples = [open("text_samples/caffeine_effects.txt", encoding="utf8").read(),
                open("text_samples/MLK_I_have_a_dream.txt", encoding="utf8").read()]

    def __init__(self, data=default_text_samples, word_limit=200):
        # split text samples into individual words
        self.word_limit = word_limit
        self.corpus_data = [corpus.split() for corpus in data]
        self.word_dict = {}
        self.generate_dictionary(self.corpus_data)

    def make_word_pairs(self, corpus):
        # generate pairs of words
        for i in range(0, len(corpus)-1):
            yield(corpus[i], corpus[i+1])

    def generate_dictionary(self, corpus_data):
        for corpus in corpus_data:
            pairs = self.make_word_pairs(corpus)

            for word1, word2 in pairs:
                if word1 in self.word_dict.keys():
                    self.word_dict[word1].append(word2)
                else:
                    self.word_dict[word1] = [word2]

    def get_first_word(self):
        first_word = np.random.choice(list(self.word_dict.keys()))
        # force first word to be an uppercase word
        while first_word.islower():
            first_word = np.random.choice(list(self.word_dict.keys()))
        return first_word

    def generate_chain(self):
        self.get_first_word(self.word_dict)
        # begin creating the word chain
        chain = [self.get_first_word(self.word_dict)]
        # pick a random number of words to have in the chain (roughyl)
        n_words = rm.randint(15,self.word_limit)

        # generate the word chain to approximate length
        for i in range(0, n_words):
            chain.append(np.random.choice(self.word_dict[chain[-1]]))

        # force the chain to end on a punctuation mark, even if it exceeds the max length
        while chain[-1][-1] not in [".", "!", "?"]:
            chain.append(np.random.choice(self.word_dict[chain[-1]]))
         # return the completed chain
        return " ".join(chain)

    def print_chain(self, chain):
        print(chain)