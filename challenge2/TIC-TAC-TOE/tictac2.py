board = [" " for _ in range(9)]
# print(board)
# for row in [board[i*3:(i+1)*3] for i in range(3)]:
#     print(row)
    # print("| " + "| ".join(row) + "| ")

# for row in [board[0:3] for i in range(3)]:
    # print(row)
    # print("| " + "| ".join(row) + "| ")


def print_board(board):
    for row in [board[0:3] for i in range(3)]:
        # print(row)
        print("| " + "| ".join(row) + "| ")


print_board(board)


def empty_space(board):
    if board == " ":
        return True
    else:
        return False


def check_win():
    if board[0:3] in range(1):
        return True