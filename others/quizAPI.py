import requests
import sys

url = "https://opentdb.com/api.php?amount=10&category=22&difficulty=easy&type=multiple"
response = requests.get(url, timeout=5)
data = response.json()
print(data)
# for result in data["results"]:
#     # print(result["question"])
#     print(result["question"])
#     # print(result["correct_answer"])    # print(result)
#     # print(result["incorrect_answers"])
#     # print(result.keys())
#
#     # for incorrect_answer in result["incorrect_answers"]:
#     #     print(incorrect_answer)
#     answer = input("Answer: ").lower()
#     score = 0
#     if result["correct_answer"].lower() == answer:
#         print("Correct")
#         score += 1
#         print(f"Your score is {score}")
#     else:
#         print("Wrong")
#         print(f"The answer is", result["correct_answer"])

# score = 0
# gameIsOn = True


def check_answer(question, ans, score):  #to check ques, ans and score
    if result['correct_answer'].isalnum() == ans.isalnum():
        print(f"Correct answer. Your score is {score + 1}")
        return True
    else:
        print("Wrong answer!")
        return False


while True:
    score = 0
    chance = 1  #so that break statement can shift to next question
    for result in data["results"]:

        for i in range(chance):
            print(result["question"])
            answer = input("Answer: ")

            if answer.lower() == "skip":
                break
            if answer.lower() == "exit":
                print("Your final score is ", score)
                sys.exit()
            check = check_answer(result["question"], result["correct_answer"], score)
            if check:
                score = score + 1
                break
    break


print(f"Your final score is {score}")

