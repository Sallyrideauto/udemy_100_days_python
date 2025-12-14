from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip

FONT = ("Departure Mono", 10, "normal")
DEFAULT_EMAIL = "angela@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = (
        [choice(letters) for _ in range(nr_letters)]
        + [choice(symbols) for _ in range(nr_symbols)]
        + [choice(numbers) for _ in range(nr_numbers)]
    )
    shuffle(password_list)

    password = "".join(password_list)
    input_pw.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site_name = input_site.get()
    user_email = input_user_id.get()
    user_pw = input_pw.get()

    if site_name == "" or user_pw =="":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=site_name, message=f"These are the details entered: \nEmail: {user_email} \nPassword:: {user_pw} \nIs it OK to save?")
        if is_ok:
            # save information in txt file
            with open("data.txt", "a") as data:
                data.write(f"{site_name} | {user_email} | {user_pw}\n")

                # initialize entries
                input_site.delete(0, END)
                if user_email != DEFAULT_EMAIL:
                    input_user_id.delete(0, END)
                    input_user_id.insert(0, DEFAULT_EMAIL)
                input_pw.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
locker_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(column=1, row=0)

# Site information area
site_label = Label(text="Website:", font=FONT)
site_label.grid(column=0, row=1)
input_site = Entry(width=38, font=FONT)
input_site.grid(column=1, row=1, columnspan=2)
input_site.focus()

# User email area
user_id_label = Label(text="Email/Username:", font=FONT)
user_id_label.grid(column=0, row=2)
input_user_id = Entry(width=38, font=FONT)
input_user_id.grid(column=1, row=2, columnspan=2)
input_user_id.insert(0, DEFAULT_EMAIL)

# User pw area
pw_label = Label(text="Password:", font=FONT)
pw_label.grid(column=0, row=3)
input_pw = Entry(width=21, font=FONT)
input_pw.grid(column=1, row=3)
make_pw_button = Button(text="Generate Password", command=generate_password, width=13, font=FONT)
make_pw_button.grid(column=2, row=3)

add_info_button = Button(text="Add", command=save, width=36, font=FONT)
add_info_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
