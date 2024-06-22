BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random
timer = None
all_words = pd.read_csv("/Users/muhammadhamdazam/Documents/Python Programs/Day 31/flash-card-project-start/data/german_words.csv")


def generate_word(correct):
    canvas.itemconfig(language_text, text= "German", fill= "black")
    canvas.itemconfig(behind_image,image= card_front_image)
    random_index = random.randint(0,999)
    german_word = all_words[random_index == all_words.index].GERMAN[random_index]
    canvas.itemconfig(word_text, text= german_word.title(), fill= "black")
    window.after(3000, flip_card, random_index)

def flip_card(random_index):
    canvas.itemconfig(behind_image,image= card_back_image)
    canvas.itemconfig(language_text, text= "English", fill= "white")
    english_word = all_words[random_index == all_words.index].ENGLISH[random_index]
    canvas.itemconfig(word_text, text= english_word.title(), fill= "white")
    
def start():
    generate_word(False)
    start_button.grid_forget()

window = Tk()
window.title("Flashy")
window.config(bg= BACKGROUND_COLOR, highlightthickness=0, padx=50, pady=50)

start_button = Button(text="Start",font= ('Helvetica 15 bold'), command= start)
start_button.grid(row=1,column=1)

canvas = Canvas(width=800, height= 526, bg= BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="/Users/muhammadhamdazam/Documents/Python Programs/Day 31/flash-card-project-start/images/card_front.png")
card_back_image = PhotoImage(file="/Users/muhammadhamdazam/Documents/Python Programs/Day 31/flash-card-project-start/images/card_back.png")
behind_image = canvas.create_image(400, 263, image= card_front_image)
language_text = canvas.create_text(400, 150, text= "German", font=("Arial", 40, "italic"), fill= "black")
word_text = canvas.create_text(400, 263, text= "Word", font=("Arial", 60, "bold"), fill= "black")
canvas.grid(row=0, column=0, columnspan=3)

right_photo_image = PhotoImage(file="/Users/muhammadhamdazam/Documents/Python Programs/Day 31/flash-card-project-start/images/right.png")
right_button = Button(image= right_photo_image, highlightthickness=0, bd= 0, padx=50, pady=50, command= lambda:generate_word(True))
right_button.grid(row=1,column=2)

wrong_photo_image = PhotoImage(file="/Users/muhammadhamdazam/Documents/Python Programs/Day 31/flash-card-project-start/images/wrong.png")
wrong_button = Button(image= wrong_photo_image, highlightthickness=0, bg= BACKGROUND_COLOR, bd=0, padx=50, pady=50, command= lambda:generate_word(False))
wrong_button.grid(row=1, column=0)


window.mainloop()