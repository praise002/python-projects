"""
Start with an intro message
Create a fn to check answer with params = question, ans, attempts, score
create a fn to print the dictionary
"""
import sys

from questions import quiz


def intro_message():
    """
    Intoduces user to the quiz rules, and takes an input from user to start the quiz.
    Returns true regardless of any key pressed
    """

    print("Welcome to this fun superhero quiz! \nAre you ready to test your knowledge about superhero?")
    print("There are a total of 11 questions, you can skip a question by typing 'skip'")
    print("Press any key to start the fun!")
    input()
    return True   #will start the game


def check_answer(question, ans, attempts, score):
    """
    Takes the arguments and confirms if the ans provided by the user is correct.
    Converts all answers to lowercase to make sure the quiz is not case sensitive
    """
    if quiz[question]["answer"].lower() == ans.lower():
        print(f"Correct answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer: \nYou have {attempts - 1} left! Try again...")
        return False


def print_dict():
    for question_id, question in quiz.items():
        for key, value in question.items():
            print(f"{key}: {value}")


intro = intro_message()
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter answer (To move to the next question, type 'skip', to exit type 'exit'): ")
            if answer.lower() == "skip":
                break
            if answer.lower() == "exit":
                print(f"Your final score is {score}.")
                sys.exit()
            check = check_answer(question, answer, attempts, score)
            if check:
                score = score + 1
                break
            attempts = attempts - 1
    break


print(f"Your final score is {score}!\n")
print("Want to know the correct answers? Please see them below!\n")
print_dict()
print("Thanks for playing!")

