from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
               'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Random letters
    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    random_choices = random_letters + random_symbols + random_numbers

    # Shuffle list
    shuffle(random_choices)

    # Create the password
    password = "".join(random_choices)

    password_input.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website_name) == 0 or len(password) == 0:
        messagebox.showwarning(title="Missing fields", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \n\nEmail:{email} "
                                                                   f"\nPassword:{password} \n\nIs it ok to save?")
        if is_ok:

            messagebox.showinfo(title="Confirmation", message="Password Saved!")

            with open("data.txt", "a") as data:
                data.write(f"{website_name} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ------------- Canvas ------------------
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# ----------- Labels ---------------------
website_lbl = Label(text="Website:")
website_lbl.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0)

password_lbl = Label(text="Password:")
password_lbl.grid(row=3, column=0)

# --------- Entries ---------------------
website_input = Entry(width=53)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2)

email_input = Entry(width=53)
email_input.insert(END, "example@gmail.com")
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=34)
password_input.grid(row=3, column=1)

# --------- Buttons -------------------------
generate_password_btn = Button(text="Generate Password", command=generate_password)
generate_password_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=45, command=save)
add_btn.grid(row=4, column=1, columnspan=2)


window.mainloop()
