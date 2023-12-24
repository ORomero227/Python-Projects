from tkinter import *

miles_in_km = 1.609


def calculate():
    miles = float(miles_input.get())
    kilometers = round(miles * miles_in_km, 2)
    kilometers_qty["text"] = kilometers


window = Tk()
window.title("Miles to Kilometers Converter")
window.geometry("300x150")
window.config(padx=30, pady=25)

miles_input = Entry()
miles_input.config(width=10)
miles_input.grid(column=1, row=0)

miles_title = Label()
miles_title.config(text="Mile", font=("Arial", 12), padx=10)
miles_title.grid(row=0, column=3)

equal_label = Label()
equal_label.config(text="is equal to", font=("Arial", 12))
equal_label.grid(row=1, column=0)

kilometers_qty = Label(text="0", font=("Arial", 12))
kilometers_qty.config(pady=10)
kilometers_qty.grid(row=1, column=1)

kilometers_title = Label(text="Km", font=("Arial", 12), )
kilometers_title.config(padx=10)
kilometers_title.grid(row=1, column=3)

calculate_button = Button(text="Calculate")
calculate_button.config(command=calculate)
calculate_button.grid(row=2, column=1)


window.mainloop()
