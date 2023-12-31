import random
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("data/french_words.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/words_to_learn.csv.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

card = {}


def next_card():
    global card, flip_timer
    card = random.choice(to_learn)
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=card['French'])
    canvas.itemconfig(background_image, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(background_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=card['English'])


def is_known():
    to_learn.remove(card)
    data_to_learn = pandas.DataFrame(to_learn)
    data_to_learn.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# width = window.winfo_screenwidth()
# winfo_screenheight()
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
background_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=1, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, borderwidth=0, command=next_card)
unknown_button.grid(row=1, column=1)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, borderwidth=0, command=is_known)
known_button.grid(row=1, column=2)

next_card()

window.mainloop()
