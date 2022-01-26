class BasicWord:

    def __init__(self, word, subwords):

        self.word = word
        self.subwords = subwords


    def has_subword(self, word):
        return word in self.subwords

    def get_word_count(self):
        return len(self.subwords)

