from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FRENCH_WORDS = "data/french_words.csv"


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
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=CARD_FRONT)
canvas.grid(row=0, column=0, columnspan=2)

language_label_text = canvas.create_text(400, 150, text="Français", font=("Ariel", 40, "italic"))

word_text = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))

# Buttons
wrong_button = Button(image=WRONG_BUTTON_IMG, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_button = Button(image=RIGHT_BUTTON_IMG, highlightthickness=0)
right_button.grid(row=1, column=1)



window.mainloop()
