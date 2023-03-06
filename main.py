from tkinter import *
import pandas
import random
import os

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- SETUP INITIAL DATA ------------------------------- #

try:
    words_to_learn_data = pandas.read_csv("data/words_to_learn.csv")
    df = pandas.DataFrame(words_to_learn_data)
    words_to_learn = df.values.tolist()
except FileNotFoundError:
    FRENCH_WORDS_DATA = pandas.read_csv("data/french_words.csv")
    df = pandas.DataFrame(FRENCH_WORDS_DATA)
    words_to_learn = df.values.tolist()
    print(words_to_learn)


# ---------------------------- SAVE WORDS TO LEARN ------------------------------- #
def save_progress():
    data = pandas.DataFrame(words_to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

# ---------------------------- DID YOU KNOW THE WORD ------------------------------- #


def knew_the_word():
    global current_card, words_to_learn
    try:
        words_to_learn.remove(current_card)
        show_next_card()
        save_progress()
    except:
        canvas.itemconfig(title_text, text="All done!", fill="black")
        canvas.itemconfig(word_text, text="You know all the words!!!", fill="black")
        right_button.destroy()
        wrong_button.destroy()
        if os.path.exists("data/words_to_learn.csv"):
            os.remove("data/words_to_learn.csv")
        else:
            print("The file does not exist")


def didnt_know_the_word():
    show_next_card()


# ---------------------------- SHOW NEXT WORD ------------------------------- #
current_card = {}


def show_next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    print(current_card)
    canvas.itemconfig(canvas_image, image=CARD_FRONT)
    canvas.itemconfig(title_text, text="Français", fill="black")
    canvas.itemconfig(word_text, text=current_card[0], fill="black")
    flip_timer = canvas.after(3000, flip_card)


def flip_card():
    global current_card
    print(current_card)
    canvas.itemconfig(canvas_image, image=CARD_BACK)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card[1], fill="white")


# ---------------------------- UI SETUP ------------------------------- #
# Main window config
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Image Constants
CARD_FRONT = PhotoImage(file="images/card_front.png")
CARD_BACK = PhotoImage(file="images/card_back.png")
RIGHT_BUTTON_IMG = PhotoImage(file="images/right.png")
WRONG_BUTTON_IMG = PhotoImage(file="images/wrong.png")

# Canvas setup
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=CARD_FRONT)
canvas.grid(row=0, column=0, columnspan=2)

title_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))

word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# Buttons
wrong_button = Button(image=WRONG_BUTTON_IMG, highlightthickness=0, borderwidth=0, width=97, height=97,
                      command=didnt_know_the_word)
wrong_button.grid(row=1, column=0)

right_button = Button(image=RIGHT_BUTTON_IMG, highlightthickness=0, borderwidth=0, width=97, height=97,
                      command=knew_the_word)
right_button.grid(row=1, column=1)

flip_timer = canvas.after(3000, flip_card)

show_next_card()

window.mainloop()
