"""
Number guesser
Sourced from: https://hackr.io/blog/python-projects
"""

import random

attempts_list = []

def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score. It's all yours.")
    else:
        print(f"The current high score is {min(attempts_list)}.")

def start_game():
    print("Number guesser game!")
    random_number = int(random.randint(1,10))

    player_name = input("What is your name? ")
    wanna_play = input(f'Hi {player_name}, do you want to play? (y/n) ')
    attempts = 0

    while wanna_play.lower() == 'y':
        guess = input("Pick a number between 1 and 10 (inclusive). ")

        if int(guess) == random_number:
            print("You got it!")
            attempts += 1
            attempts_list.append(attempts)
            print(f"Number of attempts: {attempts}")
            
            # reset scores
            attempts = 0
            show_score()
            random_number = int(random.randint(1,10))

            play_again = input("Would you like to play again? (y/n) ")
            if play_again.lower() == "n":
                print("Game over")
                break
        elif int(guess) > random_number:
            print("It's lower")
            attempts += 1
        elif int(guess) < random_number:
            print("It's higher")
            attempts += 1
    else:
        print("Ok bye.")

if __name__ == '__main__':
    start_game()
    