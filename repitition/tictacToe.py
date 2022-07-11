"""
tic tac toe board
[
    [-, -, -],
    [-, -, -],
    [-, -, -]
]

user_input--> 1-9
check if user input is already taken
add it to the board
check if user won: checking rows, columns and diagonals
toggle between users upon successful moves
"""

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]


def print_board(board):
    for row in board:
        for col in row:  #inner loop
            print(col, end=" ")
        print()


def is_moves_left(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                return True  #if there are moves to play
            else:
                return False  #if there are no moves left to play


def evaluate(board):
    """checking for rows"""
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == "x":
                return 10
            if board[row][0] == "o":
                return -10

    """Checking for column"""
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == "x":
                return 10
            if board[0][col] == "o":
                return -10

    """checking fo diagonal"""
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] == "x":
            return 10
        if board[0][0] == "o":
            return -10

    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] == "x":
            return 10
        if board[0][2] == "o":
            return -10
    return 0  #a tie


def minimax(board, depth, isMaximizing):
    score = evaluate(board)
    if score == -10:  #if minimizer has won d game
        return score

    if is_moves_left(board) == False:  #no more moves to play
        return 0

    if isMaximizing:  #maximizer turn
        best = -1000
        #traverse all cells
        for i in range(3):
            for j in range(3):
                #check if cell is empty
                if board[i][j] == "_":
                    #make the move
                    board[i][j] = "x"
                    #call minimax recursively and chose d max value
                    best = max(best, minimax(board, depth + 1, not isMaximizing))
                    #undo d move
                    board[i][j] = "_"
        return best

    else:  #minimizer move
        best = 1000
        # traverse all cells
        for i in range(3):
            for j in range(3):
                # check if cell is empty
                if board[i][j] == "_":
                    # make the move
                    board[i][j] = "o"
                    # call minimax recursively and chose d min value
                    best = min(best, minimax(board, depth + 1, not isMaximizing))
                    # undo d move
                    board[i][j] = "_"
        return best

"""This will return d best possible move for d player"""


def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)
    #traverse all cells, evaluate minimax fn for all empty cells
    #and return d cell with optimal value
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                #make d move
                board[i][j] = "x"
                #compute evaluation fn for dis move
                move_val = minimax(board, 0, False)
                #undo d move
                board[i][j] = "_"
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    print("The value of the best move is:", best_val)
    print()
    return best_move

