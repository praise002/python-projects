class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        """
        if d word doesnt exist inside d child we have to create a node for it
        the root node is left empty we only give it children
        """
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                pointer.children[letter] = Node()  #create a new node for d child
            pointer = pointer.children[letter]  #it exists, its pointing to a node
        pointer.endOfWord = True

    def search(self, word):
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]
        #Check end of word
        if pointer.endOfWord:
            return True
        else:
            return False

    def start_with(self, prefix):
        pointer = self.root
        for letter in prefix:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]
        return True  #prefix exists


obj = Trie()
obj.insert("apple")
p = obj.search("apple")
p1 = obj.start_with("app")
print(p)
print(p1)






