"""
backtracking steps:
1. pick empty
2. try all numbers
3. find one that works
4. repeat: go to next empty square
5. backtrack: as soon as we get to a point d solution can't be completed
"""

board = [
    [7, 0, 0, 4, 0, 0, 1, 2, 0],  #col0
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(board):
    find = find_empty(board)
    if not find:  # not empty, base case
        return True  # we have found d solution
    else:
        row, column = find

    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            if solve(board):
                return True
            board[row][column] = 0  #else part, reset

    return False


def valid(board, number, position):
    #check row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    #check column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    #check square box
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


def print_board(board):
    for i in range(len(board)):  #for row
        if i % 3 == 0 and i != 0:  #3%3, 6%3,
            print("------------------------")  #in 3rd row print horizontal line

        for j in range(len(board[0])):  #for column
            if j % 3 == 0 and j != 0:  #col3, 6
                print(" | ", end="")

            if j == 8:  #last line
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    # for i, row in enumerate(board):
    #     for j, val in enumerate(row):
    #         if val == 0:
    #             return (i, j)
    return None #if no blank squares


print_board(board)
solve(board)
print("\n")
print_board(board)






