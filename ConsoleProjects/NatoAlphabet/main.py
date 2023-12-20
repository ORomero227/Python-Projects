import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {rows.letter: rows.code for (index, rows) in data.iterrows()}

user_word = input("Enter a single word ex.House: ")

result = [alphabet[char] for char in user_word.upper()]

print(result)
