import random
import time


def main():
    player_1 = 0
    player_1_wins = 0
    player_2 = 0
    player_2_wins = 0
    rounds = 1
    score = 0

    while rounds != 4:
        time.sleep(1)
        print("Round", rounds)
        player_1 = dice_roll()
        player_2 = dice_roll()
        print("Player 1 Roll:", player_1)
        time.sleep(1)
        print("Player 2 Roll:", player_2)

        if player_1 == player_2:
            print("Draw")
        elif player_1 > player_2:
            player_1_wins += 1
            print("Player 1 wins!")
        else:
            player_2_wins += 1
            print("Player 2 wins!")

        rounds = rounds + 1

    if player_1_wins == player_2_wins:
        print(f"Player1 score: {score} \nPlayer2 score: {score}")
    elif player_1_wins > player_2_wins:
        print(f"Player1 score: {score + 1}")
    else:
        print(f"Player 2 score: {score + 1}")


def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll

main()  #work on it