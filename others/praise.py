"""Happy Birthday"""

import time


def happy_birthday(name):
    name = name.title()
    for i in range(2):
        print("Happy Birthday to you.")
        time.sleep(1)
    print(f"Happy Birthday to {name}!")
    time.sleep(1)
    print("Happy Birthday to you.")
    time.sleep(1)
    for i in range(3):
        print("Hip Hip Hooray!")


happy_birthday("praise")