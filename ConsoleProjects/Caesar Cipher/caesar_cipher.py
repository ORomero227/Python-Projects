'''This is Caesar Cipher Program'''
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, text, shift_number):
    '''Main Function'''
    end_text = ""
    if direction.lower() == "decode":
        shift_number *= -1
    for char in text:
        if char in alphabet:
            letter_index = alphabet.index(char)
            new_letter_index = letter_index + shift_number
            end_text += alphabet[new_letter_index]
        else:
            end_text += char

    print(f"The {direction} text is {end_text}")


print(art.logo)

should_continue = True

while should_continue:

    option = input("Type 'encode' to encrypt, type 'decode to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(option, message, shift)

    restart = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if restart.lower() == "no":
        should_continue = False
        print("Goodbye")
