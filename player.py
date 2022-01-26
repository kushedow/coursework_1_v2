class Player:

    def __init__(self, name):
        self.name = name
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def get_word_count(self):
        return  len(self.words)

    def was_used(self, word):
        return word in self.words


