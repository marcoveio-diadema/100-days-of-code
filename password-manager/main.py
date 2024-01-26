from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ("arial", 14, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
def generate_password():
    # generate random password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)
    password = "".join(password_list)

    # insert the generated password into the entry
    password_entry.insert(0, password)

    # copy text in order to paste is straight
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # grab data from widgets and appends it into senhas.txt
    website = entry_website.get()
    username = entry_username.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    # check if any empty input
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing fields", message="You've left one or more fields empty, please redo it")
    else:
        try:
            with open("senhas.json", "r") as file:
                # read old data
                data = json.load(file)

        except FileNotFoundError:
            with open("senhas.json", "w") as file:
                # update old data with new data
                json.dump(new_data, file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)

            with open("senhas.json", "w") as file:
                # save updated data
                json.dump(data, file, indent=4)

        finally:
            # delete previous data and add a focus
            entry_website.delete(0, END)
            password_entry.delete(0, END)
            entry_website.focus()


# ---------------------- SEARCH FUNCTION ------------------------------ #
def search():
    website_name = entry_website.get()
    try:
        with open("senhas.json", "r") as file:
            # read data in file
            passwords_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No password found for this website.")
    else:
        if website_name in passwords_data:
            username_data = passwords_data[website_name]["email"]
            password_data = passwords_data[website_name]["password"]
            messagebox.showinfo(title=website_name, message=f"Email: {username_data} \nPassword: {password_data}")
        else:
            messagebox.showinfo(title="Error", message=f"No password found for {website_name}.")


# ---------------------------- UI SETUP ------------------------------- #
# create window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create the canvas image
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# website label and entry
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

entry_website = Entry(width=20)
entry_website.grid(column=1, row=1, columnspan=1)
entry_website.focus()

# search button
search_button = Button(text="Search", width=13, command=search)
search_button.grid(column=2, row=1)


# mail/username label and entry
username_label = Label(text="Email/Username:", font=FONT)
username_label.grid(column=0, row=2)

entry_username = Entry(width=38)
entry_username.grid(column=1, row=2, columnspan=2)
entry_username.insert(0, string="marcusfreitas1989@gmail.com")

# password label and button
password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

# add button

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
