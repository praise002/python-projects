import time

from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  #3*3 board
        self.current_winner = None  #keep track of current winner

    def print_board(self):
        """
        After calculation:
            self.board[0:3]  1st row
            self.board[3:6] 2nd row
            self.board[6:9] 3rd row
            [0, 1, 2]
            [3, 4, 5]
            [6, 7, 8]
        """
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " | ")


    @staticmethod
    def print_board_nums():  #it tells what num corresponds to dat box
        """
        0|1|2
        j = 0,1,2
        (0*3, (0+1)*3) = (0,3)
        str(0,1,2) for i in range(0,3)
        (1*3, (1+1)*3) = (3,6)
        str(3,4,5) for i in range(3,6)
        (2*3, (2+1)*3) = (6,9)
        str(6,7,8) for i in range(6,8)"""
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " | ")

    def available_moves(self):
        #return []
        moves = []
        for (i, spot) in enumerate(self.board):  #i is index, spot is space
            if spot == " ":
                moves.append(i)
        return moves

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):  #to know d available squares remaining
        # return len(self.available_moves())  #or
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        """row, column, diagonal"""
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):  #column is 9spaces
            return True

        """check column"""
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):  #column is 9spaces
            return True

        """
        check diagonals
        winner left to right = [0, 4, 8]
        right to left = [2, 4, 6]
        combined = [0, 2, 4, 6, 8]
        """
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  #right to left diagonal
            if all([spot == letter for spot in diagonal2]):  # column is 9spaces
                return True
        """all the checks fail, no winner"""
        return False


def play(game, x_player, o_player, print_game):
    if print_game:
        game.print_board_nums()

    letter = "X"  #starting letter
    while game.empty_squares():  #stopping condition is wen no more empty square
        """get the move"""
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        """Make the move"""
        if game.make_move(square, letter):
            if print_game:
                print(letter, f"makes move to square {square}")
                game.print_board()
                print()

            if game.current_winner:
                if print_game:
                    print(letter, "wins!")
                return letter

            """after we make our move we need to alternate letters"""
            if letter == "X":
                letter = "O"
            else:
                letter = "X"
        #break
        time.sleep(1)
        """No one wins"""
    if print_game:
        print("It's a tie")


if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)

# dd = TicTacToe()
# dd.print_board()
# dd.print_board_nums()


