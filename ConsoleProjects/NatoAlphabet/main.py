import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {rows.letter: rows.code for (index, rows) in data.iterrows()}


def generate_phonetic():
    user_word = input("Enter a single word: ")
    try:
        result = [alphabet[char] for char in user_word.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(result)


generate_phonetic()
