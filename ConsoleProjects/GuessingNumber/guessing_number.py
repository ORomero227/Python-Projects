# pylint: disable = line-too-long, invalid-name
'''Guessing Number Game Program'''
import random
import os


WELCOME_MESSAGE = "\nWelcome to the Number Guessing Game\nI'm thinking of a number between 1 to 100.\n"
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5
random_number = random.randint(1, 100)


def clear():
    '''Clear the console'''
    os.system("cls")


def game():
    '''Main Function'''
    print(WELCOME_MESSAGE)

    game_difficulty = input(
        "Choose a difficulty, type 'easy' or 'hard': ").lower()

    remaining_attempts = 0
    if game_difficulty == "easy":
        remaining_attempts = EASY_ATTEMPTS
    else:
        remaining_attempts = HARD_ATTEMPTS

    is_game_over = False

    while not is_game_over:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Enter a valid number!")
            continue

        if guess > random_number:
            print("\nToo high")
        elif guess < random_number:
            print("\nToo lower")
        else:
            print(f"\nYou've got it the answer was {random_number} 🎉")
            is_game_over = True

        remaining_attempts -= 1

        if remaining_attempts == 0:
            print("\nYou've run out of guesses, you lose")
            print(f"The number was {random_number}")
            is_game_over = True

        if remaining_attempts != 0 and not is_game_over:
            print(
                f"You've {remaining_attempts} attempts remaining to guess the number.\n")


while input("Do you want to play? Type 'y' or 'n': ") == "y":
    clear()
    game()
