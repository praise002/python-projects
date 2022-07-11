"""
intro-message
"""
import sys
import time
import random
from multiple_choice_question import quiz


def intro_message():
    print("Welcome to the simple quiz game!\nYou have only 1 chance.")
    time.sleep(1)
    return True


def check_answer(question, ans, score):
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct answer. Your score is {score + 1}")   #work on the random
        return True
    else:
        print("Wrong answer!")
        return False


def print_dict():
    item = list(quiz.items())
    random.shuffle(item)
    for question_id, question in quiz.items():
        for key, value in question.items():
            print(f"{key}: {value}")


intro = intro_message()
while True:
    score = 0
    chances = 1
    for question in quiz:
        for i in range(chances):
            print(quiz[question]["question"])
            answer = input("Please put the alphabet of the answer\n(To move to the next question, type 'skip' " 
                       "to exit type 'exit': ")
            if answer.lower() == "skip":
                break
            if answer.lower() == "exit":
                print("Your final score is ", score)
                sys.exit()
            check = check_answer(question, answer, score)
            if check:
                score = score + 1
                break
    break

print(f"Your final score is {score}\n")
time.sleep(1)
print("Want to know the correct answer. Please check below!")
time.sleep(1)
print_dict()


