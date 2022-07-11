

"""Ask question to payer and they reply with right answer
Each question has 3 attempts
If player fails to answer the question within 3 attempts then the game will move on to the next question
and the player will receive 0 points
If the player gets the right answer he gets 1 point
At the end of the game the total points scored by the player is displayed
At third attempt player should be given hint
Add exit to quit and show the final score and number of questions answered
"""
import sys

from questions import quiz


def check_answer(question, ans, attempts, score):
    """
    Takes the arguments and confirms if the ans provided by the user is correct
    make sure the quiz is not case sensitive
    """
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong answer! \nYou have {attempts - 1} attempts left. \nTry again...")
        return False


def print_dictionary():
    for question_id, question_answer in quiz.items():   #id1, 2, 3, question and answer with the key and value
        for key, value in question_answer.items():
            print(f"{key}: {value}")


def intro_message():

    """
    Introduces the player to the quiz and rules and takes an input from player to start the quiz
    Returns true regardless of any key pressed
    """
    print('Welcome to this fun superhero quiz. \nAre you ready to test your knowledge about superhero?')
    print("There are a total of 11 questions, you can skip a question anytime by typing 'skip'")
    input('Press any key to start playing: ')
    return True


intro = intro_message()
#this while loop will run until player has 0 attempts left
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])  #will print current iteration of the loop
            answer = input("Enter answer (To move to the next question type 'skip', to quit type 'q'): ")

            if answer.lower() == 'skip':
                break

            check = check_answer(question, answer, attempts, score)

            if check:
                score += 1
                break
            attempts -= 1
    break


print(f"Your final score is {score}!\n")
print("Want to know the correct answers? Please see them below!\n")
print_dictionary()
print('Thanks for playing')

# if answer.lower() == 'exit':
#     sys.exit()
# print(f"Your final score is {score}!\n")  #work on this tomorrow

# for question in quiz:
    # print(question)
    # print(quiz[question]['question'])
# for question_id, question_answer in quiz.items():
#     for key in question_answer:
#         print(key + ':', question_answer[key])

# for question_id, question in quiz.items():
#     for key, value in question.items():
#         print(f"{key}: {value}")

# for question_id, question in quiz.items():
#     print(question)



