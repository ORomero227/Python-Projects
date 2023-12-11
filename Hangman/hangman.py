'''Hangman game program'''
import random
import hangman_arts
import hangman_words

stages = hangman_arts.stages
list_of_words = hangman_words.word_list

# Generate a random word
chosen_word = random.choice(list_of_words)

# Generate a blank list
display = []
chosen_word_length = len(chosen_word)
for _ in range(chosen_word_length):
    display += "_"

print(hangman_arts.logo)

# Check if the user won or lost
game_over = False
lives = 6
while not game_over:

    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    # Check if is the guessed letter in the word
    for position in range(chosen_word_length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")

    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win")
