from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import json


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

    if len(password_input.get()) != 0:
        password_input.delete(0, END)

    password_input.insert(END, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        "password": password
    }}

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Missing fields", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ------------------------ FIND PASSWORD ------------------------------------ #
def find_password():
    website = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Not Found", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showwarning(title="Password Manager", message=f"No details for {website} exists.")


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
website_input = Entry(width=34)
website_input.focus()
website_input.grid(row=1, column=1)

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

search_btn = Button(text="Search", width=15, command=find_password)
search_btn.grid(row=1, column=2)

window.mainloop()
