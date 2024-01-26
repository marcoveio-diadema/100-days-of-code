from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# get a random word from dictionary
current_card = {}
formatted_words = {}
try:
    # import csv file with pandas
    still_to_learn = pandas.read_csv("card-game/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("card-game/data/pt-fr.csv")
    formatted_words = original_data.to_dict(orient="records")
else:
    formatted_words = still_to_learn.to_dict(orient="records")


def random_word():

    global current_card, timer
    current_card = random.choice(formatted_words)
    window.after_cancel(timer)
    # display the language and words in use
    canvas.itemconfig(card_background, image=front_card)
    canvas.itemconfig(word, text=current_card['Portuguese'], fill="black")
    canvas.itemconfig(language, text="Português", fill="black")
    timer = window.after(5000, flip_card)


def flip_card():
    canvas.itemconfig(language, text="French", fill="white")
    canvas.itemconfig(word, text=current_card['French'], fill="white")
    canvas.itemconfig(card_background, image=back_card)


def random_word_know():
    formatted_words.remove(current_card)

    data = pandas.DataFrame(formatted_words)
    data.to_csv("card-game/data/words_to_learn.csv", index=False)

    random_word()


# create and configure window
window = Tk()
window.title("Aprenda português")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

timer = window.after(5000, flip_card)

# create canvas
canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, highlightthickness=0)
front_card = PhotoImage(file="card-game/images/card_front.png")
back_card = PhotoImage(file="card-game/images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_card)
language = canvas.create_text(400, 150, text="", font=("arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# create buttons
wrong_img = PhotoImage(file="card-game/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=random_word)
wrong_button.grid(column=0, row=1)

correct_img = PhotoImage(file="card-game/images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, borderwidth=0, command=random_word_know)
correct_button.grid(column=1, row=1)

random_word()


# keep it running
window.mainloop()



