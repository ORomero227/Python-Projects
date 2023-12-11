'''Main Program for Higher or Lower Game'''
import os
import random
import game_data

from art import logo as title_logo
from art import vs as vs_logo


def deal_option():
    '''Returns a random option from game_data to compare'''
    options = game_data.data
    option = random.choice(options)
    return option


def format_option(option):
    '''Returns the option formated'''
    name = option["name"]
    description = option["description"]
    country = option["country"]
    return f"{name}, a {description}, from {country}."


def clear():
    '''Clear the console'''
    return os.system("cls")


def play_game():
    '''Main Function'''
    # Selects the first options
    option_a = deal_option()
    option_b = deal_option()
    score = 0
    game_over = False

    while not game_over:
        clear()
        print(title_logo + "\n")

        print(f"Compare A: {format_option(option_a)}")

        print(vs_logo)

        print(f"Against B: {format_option(option_b)}")

        choice = input("Who has more followers? Type 'A' or 'B': ").upper()

        a_followers = option_a["follower_count"]
        b_followers = option_b["follower_count"]

        if (choice == "A" and a_followers > b_followers) or (choice == "B" and b_followers > a_followers):
            score += 1
        else:
            game_over = True

        option_a = option_b
        option_b = deal_option()

    if game_over:
        clear()
        print(title_logo)
        print(f"Sorry that's wrong. Final score: {score}")

        play_again = input(
            "Do you want to play again? Type 'Y' or 'N': ").upper()

        if play_again == "Y":
            clear()
            play_game()
        else:
            print("Good Bye!")


play_game()
