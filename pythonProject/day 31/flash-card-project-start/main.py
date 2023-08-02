import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
random_card = {}

try :
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else :
    to_learn = data.to_dict(orient="records")


def next_card():
    global random_card,flip_timer
    window.after_cancel(flip_timer)
    random_card = random.choice(to_learn)
    french_word = random_card["French"]
    canvas_1.itemconfig(title_text,text="French",fill="Black")
    canvas_1.itemconfig(word_text,text=french_word,fill="Black")
    canvas_1.itemconfig(canvas_image,image=front_image)
    window.after(3000,flip_card)


def flip_card():
    canvas_1.itemconfig(title_text,text="English",fill="White")
    canvas_1.itemconfig(word_text,text=random_card["English"],fill="white")
    canvas_1.itemconfig(canvas_image,image=back_image)

def is_known():
    to_learn.remove(random_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer = window.after(3000,func=flip_card)

# extracting the images
w_image = PhotoImage(file="/Users/hardik/PycharmProjects/pythonProject/day 31/flash-card-project-start/images/wrong.png")
r_image = PhotoImage(file="/Users/hardik/PycharmProjects/pythonProject/day 31/flash-card-project-start/images/right.png")
front_image = PhotoImage(file="/Users/hardik/PycharmProjects/pythonProject/day 31/flash-card-project-start/images/card_front.png")
back_image = PhotoImage(file="/Users/hardik/PycharmProjects/pythonProject/day 31/flash-card-project-start/images/card_back.png")


# canvas 1
canvas_1 = Canvas(height=526,width=800,highlightthickness=0,bg=BACKGROUND_COLOR)
canvas_image = canvas_1.create_image(400,263,image=front_image)
title_text = canvas_1.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
word_text = canvas_1.create_text(400,263,text="Word",font=("Ariel",60,"bold"))
canvas_1.grid(row=0,column=0,columnspan=2)

# button 1
button_1 = Button(image=w_image,highlightthickness=0,command=next_card)
button_1.grid(row=1,column=0)

#button 2
button_2 = Button(image=r_image,highlightthickness=0,command=is_known)
button_2.grid(row=1,column=1)

next_card()

window.mainloop()


