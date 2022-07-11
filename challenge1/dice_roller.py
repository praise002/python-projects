import random
import time

while True:
    user = input("Enter 'v' to start rolling: ")
    if user.lower() == 'v':
        print('Rolling dice...')
        time.sleep(1)
        print(f"The value is ", random.randint(1, 7))
    repeat = input("Roll dice again? 'y' or 'n': ")
    if repeat.lower() == 'n':
        break
