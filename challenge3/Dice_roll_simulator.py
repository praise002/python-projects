import random

#range of d values of a dice
import time

min_val = 1
max_val = 6

roll_again = "yes"

while roll_again.lower() == "yes" or roll_again.lower() == "y":
    time.sleep(1)
    print("Rolling the dices...")
    time.sleep(1)

    # generating d first random integer from 1 to 6
    dice1 = random.randint(min_val, max_val)

    # generating d 2nd random integer from 1 to 6
    dice2 = random.randint(min_val, max_val)

    print(f"The values are:\nDice1: {dice1}\nDice2: {dice2}")

    if dice1 == dice2:
        print("You rolled a double!")
    elif dice1 != dice2:
        print("You won!")
    else:
        print("Keep trying!")

    #Asking d user ro roll d dice again
    roll_again = input("Roll the dices again?").lower()
print("Thanks for playing!")

        