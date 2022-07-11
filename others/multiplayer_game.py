def player():
    score1 = 0
    score2 = 0
    players[player1] = score1
    players[player2] = score2
    print(players)


def check_answer(question, answer):
    question = input("What insect causes malaria? ")
    if answer.lower() == "mosquito":
        return "correct"
    else:
        return "lose"


def keep_trackOfScore(player, opponent, score):
    if check_answer(player, opponent):
        if player == "correct":
            score += 1
            players[player] = 1
            print(players)
        elif opponent == "correct":
            score += 1
            players[opponent] = 1
            print(players)
        else:
            score = 0
            print(players)


# def print_score(players, score):
#     if keep_trackOfScore(player1, player2, score):
#         print(players)


player1 = input("Name: ")
player2 = input("Name: ")
players = {}
player()
keep_trackOfScore(player1, player2, score= 0)
# print_score(players, score=0)  #not getting it