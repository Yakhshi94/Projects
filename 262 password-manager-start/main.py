import json
import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# JSON
# Write
# json.dump()
#
# Read
# json.load()
#
# Update
# json.update()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    alphabets = ['a', ' b', ' c', ' d', ' e', ' f', ' g', ' h', ' i', ' j', ' k', ' l', ' m', ' n', ' o', ' p', ' q',
                 ' r',
                 ' s', ' t', ' u', ' v', ' w', ' x', ' y', ' z', ' a', ' b', ' c', ' d', ' e', ' f', ' g', ' h', ' i',
                 ' j',
                 ' k', ' l', ' m', ' n', ' o', ' p', ' q', ' r', ' s', ' t', ' u', ' v', ' w', ' x', ' y', ' z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '*']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(alphabets) for _ in range(nr_letters)]
    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]
    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    random.shuffle(password_list)

    password = ''.join(password_list)
    # for char in password_list:
    #     password += char
    password_entry.delete(0, END)
    password_entry.insert(0, password.replace(" ", ""))
    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': username,
            'password': password
        }
    }
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please make sure you filled the fields")
    else:
        is_ok = messagebox.askokcancel(website, "is it ok to save the data")
        if is_ok:
            try:
                with open('data.json') as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('data.json', mode='w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # update old data with new data
                data.update(new_data)

                with open('data.json', mode='w') as data_file:
                    # save new data to json file
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as user_data:
            data = json.load(user_data)
    except FileNotFoundError:
        messagebox.showerror(title='File Not Found', message='Json File Does not Exist')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(website, f"Email: {email} \n Password: {password}")
        else:
            messagebox.showinfo(website, "Sorry, Website Has No Details")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=20, padx=20)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=2)
website_entry = Entry(width=28, highlightthickness=0, fg='blue')
website_entry.grid(column=1, row=2, pady=5, padx=0, ipady=3)
website_entry.focus()

search_btn = Button(text='Search', command=find_password)
search_btn.grid(column=2, row=2)

username_label = Label(text='Email/Username:')
username_label.grid(column=0, row=3)
username_entry = Entry(width=40)
username_entry.grid(column=1, row=3, columnspan=2, pady=5, ipady=3)
username_entry.insert(0, "yakhshi@mail.ru")

password_label = Label(text='Password Generate:')
password_label.grid(column=0, row=4)
password_entry = Entry(width=28, highlightthickness=0, fg='blue')
password_entry.grid(column=1, row=4, pady=5, padx=0, ipady=3)

generate_btn = Button(text='Generate', command=generate_password)
generate_btn.grid(column=2, row=4)

add_btn = Button(text="Add", width=36, command=save_data)
add_btn.grid(column=1, row=5, columnspan=2, pady=10)

mainloop()
