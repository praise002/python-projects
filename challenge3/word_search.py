class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def add_word(self, word):
        current = self  #root node
        for letter in word:
            if letter not in current.children:  #character does not exist
                current.children[letter] = Node()
            #already exist
            current = current.children[letter]
        current.endOfWord = True


class Solution:
    def find_words(self, board, words):
        root = Node()

        for letter in words:
            root.add_word(letter)

        rows, cols = len(board), len(board[0])
        result, visited = set(), set()

        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited \
                    or board[r][c] not in node.children:
                """
                if r & c is length of row, col
                if r, c is visited
                if board[r][c] not in children
                """
                return   #break
            #else
            visited.add((r, c))
            node = node.children[board[r][c]]  #update d node after visiting it
            word = word + board[r][c]
            if node.endOfWord:  #if false
                result.add(word)

            dfs(r - 1, c, node, word)  #call it recursively
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            visited.remove((r, c))  #done visiting

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(result)


board = [
    ["o", "a", "a", "n"],
    ["e", "t", "a", "e"],
    ["i", "h", "k", "r"],
    ["i", "f", "l", "v"]
]

words = ["earth", "pea", "eat", "rain"]