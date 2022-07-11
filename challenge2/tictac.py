import random
import sys
import time

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def print_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print()


print_board(board)


def space_is_free(position):
    if board[position] == " ":  #board[key]
        return True
    else:
        return False


# print(space_is_free(1))


def check_win():
    #checking rows
    if board[1] == board[2] and board[1] == board[3] and board[1] != " ":
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != " ":
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != " ":
        return True
    #checking columns
    elif board[1] == board[4] and board[1] == board[7] and board[1] != " ":
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != " ":
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != " ":
        return True
    #checking diagonals
    elif board[1] == board[5] and board[1] == board[9] and board[1] != " ":
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] != " ":
        return True
    else:
        return False


def check_whichmarkwon(mark):
    #checking rows
    if board[1] == board[2] and board[1] == board[3] and board[1] != mark:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != mark:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != mark:
        return True
    #checking columns
    elif board[1] == board[4] and board[1] == board[7] and board[1] != mark:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != mark:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != mark:
        return True
    #checking diagonals
    elif board[1] == board[5] and board[1] == board[9] and board[1] != mark:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] != mark:
        return True
    else:
        return False


def check_draw():
    for key in board:
        if board[key] == " ":
            return False

    return True


def insert_letter(letter, position):
    if space_is_free(position):
        board[position] = letter  #board[1]=x
        print_board(board)  #show d board to the users
        if check_win():
            if letter == "X":
                print("Bot wins")
                sys.exit()
            elif letter == "O":
                print("Player wins!")
                sys.exit()
        if check_draw():
            print("Draw")
            sys.exit()

    else:
        print("Can't insert there. Position is filled!")
        position = int(input("Enter new position: "))
        insert_letter(letter, position)  #recursively call it

    # if letter == "X":
    #     letter = "O"
    # else:
    #     letter = "X"

    # time.sleep(1)


player = "O"
bot = "X"


def player_move():
    position = int(input("Enter the position for 'O': "))
    insert_letter(player, position)


def computer_move():
    # position = int(input("Enter the position for 'X': "))
    # position = random.randint(1, 9)
    # insert_letter(bot, position)
    # print(f"Bot entered position {position}")
    best_score = -1000
    best_move = 0
    for key in board:
        if board[key] == " ":
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = " "
            if score > best_score:
                best_score = score
                best_move = key
    insert_letter(bot, best_move)
    return


def minimax(board, depth, isMaximazing):
    if check_whichmarkwon(bot):
        return 100
    elif check_whichmarkwon(player):
        return -100
    elif check_draw():
        return 0

    if isMaximazing:
        best_score = -1000
        for key in board:
            if board[key] == " ":
                board[key] = bot
                score = minimax(board, 0, False)
                board[key] = " "
                if score > best_score:
                    best_score = score
        return best_score
    else:  #minimizing
        best_score = -1000
        for key in board:
            if board[key] == " ":
                board[key] = bot
                score = minimax(board, depth + 1, True)  #depth can be 0
                board[key] = " "
                if score < best_score:
                    best_score = score
        return best_score


while not check_win():
    computer_move()
    time.sleep(2)
    player_move()


# insert_letter("X", 1)
# insert_letter("O", 1)