#!/usr/bin/env python
import argparse

#KEEP_TOP_WORDS = 10


def cleanse_word(word):
    """
    Clean word using defined rules
    :param word:
    :return:
    """
    # find regex for word1
    return word.lower().strip(',').strip('.').strip('\'').strip('"').strip('*').strip('?').strip('!').strip(';').\
        strip(':')


class WordCounter(object):
    """Word counting object, counts total words and top 10 occurring words"""

    def __init__(self, file_path, keep_top_words):
        self.top_words = list()
        self.total_words = 0
        self.file_path = file_path
        self.word_freq = dict()
        self.keep_top_words = keep_top_words
        self._count_words()

    def _count_words(self):
        with open(self.file_path, 'r') as f:
            for word in f.read().split():
                word = cleanse_word(word)
                self.word_freq.setdefault(word, 0)
                self.word_freq[word] += 1
                self.total_words += 1
                self._insert_to_top(word)

    def _insert_to_top(self, word):
        if self.top_words:
            for index, item in enumerate(self.top_words):
                if self.word_freq[item] <= self.word_freq[word]:
                    if word in self.top_words:
                        del self.top_words[self.top_words.index(word)]
                    self.top_words.insert(index, word)
                    del self.top_words[self.keep_top_words:]
                    break
                elif len(self.top_words) < self.keep_top_words and word not in self.top_words:
                    # Case where top 10 not full and word not in top 10 already
                    self.top_words.append(word)
        else:
            self.top_words.append(word)

    def display_top_words(self):
        for word in self.top_words:
            print(word, self.word_freq[word])





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Word counting program, counts frequency of words in a file.')
    parser.add_argument("file_path")
    parser.add_argument("keep_top_words")

    args = parser.parse_args()
    if 'file_path' in args:
        file_path = True
    file_path = args.file_path
    keep_top_words = int(args.keep_top_words)

    wc = WordCounter(file_path , keep_top_words)
    print("Top {KEEP_TOP_WORDS} Words:")
    wc.display_top_words()
    print("Total Words: {}".format(wc.total_words))
