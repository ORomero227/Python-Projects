'''My Rock, Paper Scissors game'''
import random

print("Welcome to Rock,Paper,Scissors Game\n")
print("[0] - Rock\n[1] - Paper\n[2] - Scissors\n")

choices = ["Rock", "Paper", "Scissors"]

cpu_choice = random.choice(choices)

game_over = False
user_score = 0
cpu_score = 0

while not game_over:
    number = int(input("What is your choice: "))

    user_choice = choices[number]

    print(f"\nYou chose: {user_choice}")
    print(f"CPU chose {cpu_choice}\n")

    if user_choice == "Rock" and cpu_choice == "Scissors":
        user_score += 1
    elif user_choice == "Scissors" and cpu_choice == "Rock":
        cpu_score += 1
    elif user_choice == "Scissors" and cpu_choice == "Paper":
        user_score += 1
    elif user_choice == "Paper" and cpu_choice == "Scissors":
        cpu_score += 1
    elif user_choice == "Paper" and cpu_choice == "Rock":
        user_score += 1
    elif user_choice == "Rock" and cpu_choice == "Paper":
        cpu_score += 1
    else:
        print("Draw\n")

    print(f"Score: You:{user_score} | CPU: {cpu_score}\n")

    if user_score == 3:
        print("You WIN")
        game_over = True
    elif cpu_score == 3:
        print("CPU WIN")
        game_over = True
