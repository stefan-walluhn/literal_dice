import random


class LiteralDice(object):
    def __init__(self, word):
        self.word = word

    def shuffle(self):
        char_list = list(self.word)
        random.shuffle(char_list)
        return ''.join(char_list)
