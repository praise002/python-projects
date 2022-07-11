import random

from questions import quiz

# item = list(quiz.items())
# print(item)
#
#
# for question_id, question in quiz.items():
#     for key, value in question.items():
#         item = list(question.items())
#         random.shuffle(item)
#         # print(item)
#         print(f"{key}: {value}")


d = {
    "Roll 1": "Tyson",
    "Roll 2": "Rock",
    "Roll 3": "John",
    "Roll 4": "Christopher",
    "Roll 5": "Brock"
}

item = list(d.items())
print(item)
random.shuffle(item)
for key, value in item:  #randomize key and value
    print(f"{key}: {value}")

item = list(d.keys())
print(item)
random.shuffle(item)
for key in item:  #randomize keys
    print(f"{key}")

item = list(d.values())
print(item)
random.shuffle(item)
for value in item:  #randomize keys
    print(value)

myList = ["apple", "banana", "cherry"]
print(random.sample(myList, k=3))  #the k is to specify the num of items we want to randomize
print(random.choices([1, 2, 3, 4], k=2))

# for key, value in random.sample(list(d.items()), k=len(d)):
#     print(f"{key}: {value}")
#
# for question_id, question in quiz.items():
#     for key, value in random.sample(list(question.items()), k=len(question)):
#         print(f"{key}: {value}")

"""Multiplayer game using list"""
#variables
round_number = 0
player_list = ["BOB", "ALEX"]
score_list = [0, 0]
gameIsOn = True

#make a game loop
while gameIsOn:
    round_number += 1
    print("\nROUND: ", round_number)
    if round_number % 2:
        #PLAYER 2 TURN
        print(player_list[1], "GETS TO PLAY")  #show player turnf
        input("Press a key: ")  #waiting for a command
        score_list[1] += 1  #Adding scores
        print(f"""
SCORES:
{player_list[0]}: {score_list[0]}
{player_list[1]}: {score_list[1]}""")  #printing out scores

        for item in score_list:  #loop through the scor list
            if item >= 5:
                print(player_list[1], "WINS")
                gameIsOn = False
                break

    else:
        #PLAYER 1 TURN
        print(player_list[0], "GETS TO PLAY")
        input("Press a key: ")
        score_list[0] += 1
        print(f"""
SCORES:
{player_list[0]}: {score_list[0]}
{player_list[1]}: {score_list[1]}""")

        for item in score_list:  #loop through the scor list
            if item >= 5:
                print(player_list[0], "WINS")
                gameIsOn = False
                break
#can add game is over would you like to play again by using a fn








