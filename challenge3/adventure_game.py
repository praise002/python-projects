answer = input("Would you like to play?(y/n) ")

if answer.lower().strip() == "yes" or "y":
    answer = input("You have reached a crossroads, would you like to move left or right ").lower().strip()
    if answer == "left":
        answer = input("You encounter a monster, would you like to run or attack. ")
        if answer == "attack":
            print("That was not the greatest idea, you lost!")
        else:
            print("Good choice, you made it away safely!")

            answer = input("You see a car and a plane. Which would you like to take?(car/plane) ")
            if answer == "plane":
                print("Unfortunately you do not know how to fly...Game over.")
            else:
                print("You won!")

    elif answer == "right":
        print("You walk aimlessly to the right and fall on a patch of ice."
              "You injured your leg and cannot continue. Game over!")
    else:
        print("Invalid choice. You lost!")
else:
    print("That's too bad!")