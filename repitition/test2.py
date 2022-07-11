import random

from questions import quiz

for question in quiz:
    print(question)

    # print(quiz[question].get("question"))
    # print(quiz[question]['question'])
#     print(quiz[question]['answer'])
# for question_id, question_answer in quiz.items():
#     for key in question_answer:
#         print(key + ':', question_answer[key])

for question_id, question in quiz.items():
    # for key, value in question.items():
        res = key, val = random.choice(list(question.items()))
        print(res)

        # print(f"{key}: {value}")
#
# for question_id, question in quiz.items():
#     print(question)


def players(player, opponent):
    player1 = input("Name: ")
    player2 = input("Name: ")
    players = []
    players.append(player1)
    players.append(player2)
    for player in players:
        if player == player1:
            pass
        if player == player2:
            pass


for i in range(1):
    print(i)

