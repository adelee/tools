from tkinter import *
import pandas
import random

timer = None
word_pair = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

data_dict = data.to_dict(orient="records")


def word_generator():
    global word_pair, timer
    word_pair = random.choice(data_dict)
    canvas.itemconfig(card, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(translated_text, text=word_pair["French"], fill="black")
    timer = window.after(3000, word_translator)


def word_translator():
    window.after_cancel(timer)
    canvas.itemconfig(card, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(translated_text, text=word_pair["English"], fill="white")


def update_data():
    global data_dict
    data_dict.remove(word_pair)
    df = pandas.DataFrame(data_dict)
    df.to_csv("./data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
translated_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=lambda: [word_generator(), update_data()])
right_button.grid(column=1, row=1)
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=word_generator)
wrong_button.grid(column=0, row=1)

word_generator()

window.mainloop()
