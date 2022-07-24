from msilib.schema import TextStyle
from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, sample
from turtle import color
from numpy import size
import pyperclip
import json


#  PASSWORD GENERATOR  
def create_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
     'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
     'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    c_list = [char for char in sample(letters, randint(5, 6))]
    s_list = [symb for symb in sample(symbols, randint(2, 3))]
    n_list = [num for num in sample(numbers, randint(2, 3))]
    password_list = c_list + s_list + n_list
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

#  SAVE PASSWORD 
def save_password():
    site = (web_entry.get()).capitalize()
    username = username_entry.get()
    password = password_entry.get()
    new_entry = {
        site: {
            "username": username,
            "password": password,
        },
    }
    if len(site) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Error",
            message="Please don't leave any fields empty"
        )
    else:
        try:
            # check is the file exist
            with open("db.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            # create it if not
            with open("db.json", "w") as file:
                json.dump(new_entry, file, indent=4)
        else:
            # update or add new entry
            data.update(new_entry)
            with open("db.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            # clear all the GUI fields
            web_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)


# SEARCH PASSWORD
def search():
    web= (web_entry.get()).capitalize()
    try:
        with open("db.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(
            title="Error",
            message="There is no database found"
        )
    else:
        if data[web]:
            search_username = data[web]["username"]
            search_password = data[web]["password"]
            messagebox.showinfo(
                title=web,
                message=f"Username: {search_username} \nPassword: {search_password}"
            )
        else:
            messagebox.showerror(
                title="Error",
                message=f"No credentials for {web}"
            )


# GUI 
window = Tk()
window.title("Password container")
window.config(padx=50, pady=50, background="light blue")



# Labels
web_label = Label(text="Website:",background="light blue")
web_label.grid(column=0, row=1)
username_label = Label(text="Username:",background="light blue")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:",background="light blue")
password_label.grid(column=0, row=3)

# Entries
web_entry = Entry(width=60)
web_entry.grid(column=1, row=1, sticky="W")
web_entry.focus()
username_entry = Entry(width=40)
username_entry.grid(column=1, row=2, sticky="W")
password_entry = Entry(width=40)
password_entry.grid(column=1, row=3, sticky="W")

# Buttons
gen_button = Button(text="Generate Password", command=create_password, foreground="white", background="black")
gen_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=30, command=save_password, foreground="white", background="purple")
add_button.grid(column=1, row=4,  sticky="EW")
search_button = Button(text="Search", command=search, foreground="white", background="blue")
search_button.grid(column=2, row=4, sticky="EW")


window.mainloop()

