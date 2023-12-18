PLACEHOLDER = "[name]"

# Gets the list of the invited names
with open("./Input/Names/invited_names.txt") as names_file:
    list_of_names = names_file.readlines()

# Gets the letter template and write the new one
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_template = letter_file.read()
    for name in list_of_names:
        striped_name = name.strip()
        new_letter = letter_template.replace(PLACEHOLDER, striped_name)
        with open(f"./Output/ReadyToSend/letter_for_{striped_name}.txt", "w") as letter:
            letter.write(new_letter)
