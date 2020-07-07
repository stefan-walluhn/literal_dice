import random


class LiteralDice(object):
    def __init__(self, word):
        self.word = word

    def shuffle(self):
        l = list(self.word)
        random.shuffle(l)
        return ''.join(l)
