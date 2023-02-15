from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

#------ Functionality --------
words_dict = {}
try:
    words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_words = pandas.read_csv("data/french_words.csv")
    words_dict = original_words.to_dict(orient="records")
else:
    #words_df = pandas.DataFrame(words)
    words_dict = words.to_dict(orient='records')
    print(words_dict)

#Generate random word
print(words_dict)
current_card = {}
def next_word():

    #current_card = random.choice(words_dict)
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_dict)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(text_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

#Flip card function
def flip_card():
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(text_word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=back_card_image)

#Save
def remove_word():
    print(current_card)
    words_dict.remove(current_card)
    global words_to_learn
    to_learn = words_dict
    words_to_learn = pandas.DataFrame(to_learn).to_csv("data/words_to_learn.csv", index=False)






#------ UI SETUP ---------

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

#Flash-Card
front_card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 278, image=front_card_image)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
text_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)





next_word()



#Buttons
right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_word)
right_button.config(padx=50)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=wrong_image, highlightthickness=0,command=next_word)
right_button.config(padx=50)
right_button.grid(row=1, column=1)

window.mainloop()

















