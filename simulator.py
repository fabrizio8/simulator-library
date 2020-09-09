from random import randint

class Alphabet:
    data = []
    def __init__(self, *args):
        self.alphabet = [*args]
    def gen_rand_string(self, length):
        return [self.alphabet[c] for c in [randint(0,length-1) for _ in range(length)]] 

