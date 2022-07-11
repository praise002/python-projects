class Trie:
    def __init__(self):
        self.child = {}

    def insert_word(self, word):
        current =