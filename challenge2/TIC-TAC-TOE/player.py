import math
import random


class Player:  #for basis of inheritance
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super(RandomComputerPlayer, self).__init__(letter)

    def get_move(self, game):  #get a random valid spot for our next move
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super(HumanPlayer, self).__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:  #while not false
            square = input(self.letter + "\"s turn. Input (0-9): " )
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True  #if its a value
            except ValueError:
                print("Invalid square. Try again.")
        return val
