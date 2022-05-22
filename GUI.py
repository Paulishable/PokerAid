from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.font
import main
from images import *

import math
from probability_calcs import *
from card_utilities import *
from hand_rating import *
import re

the_cards = []
all_possible_hands = []
a_hand = []
hash_list = []
the_hand = []
my_hand = [10, 11, 12, 13, 1]
card_images = []



def deal(the_hand):
    """deal the hand"""
    card_is_used = []
    for index in range(0, 54):
        the_cards.append(index)
        card_is_used.append(False)

    the_hand = []
    for i in range(1, 54):
        card_is_used[i] = False

    for _ in range(5):
        a_card = randint(1, 52)
        while card_is_used[a_card]:
            a_card = randint(1, 52)
            # print("Card is used - pick another.")
        the_hand.append(a_card)
        card_is_used[a_card] = True
    # print(sorted(the_hand))
    return sorted(the_hand)


def print_and_rate_it(current_hand):
    print("\n")
    for item in range(5):
        print(find_card_face_string(current_hand[item]) + " of " + find_card_suit(current_hand[item]))
    print("")
    print(rate_the_hand(current_hand))

def start_by_dealing():
    my_hand = deal(the_hand)
    print_and_rate_it(my_hand)

    the_face = str(find_card_value_int(my_hand[0]))
    if find_card_value_int(my_hand[0]) > 10 or find_card_value_int(my_hand[0]) == 1:
        the_face = find_card_face_string(my_hand[0])
    button_a.__setitem__("text", the_face + " of " + find_card_suit(my_hand[0]))

    the_face = str(find_card_value_int(my_hand[1]))
    if find_card_value_int(my_hand[1]) > 10 or find_card_value_int(my_hand[1]) == 1:
        the_face = find_card_face_string(my_hand[1])
    button_b.__setitem__("text", the_face + " of " + find_card_suit(my_hand[1]))

    the_face = str(find_card_value_int(my_hand[2]))
    if find_card_value_int(my_hand[2]) > 10 or find_card_value_int(my_hand[2]) == 1:
        the_face = find_card_face_string(my_hand[2])
    button_c.__setitem__("text", the_face + " of " + find_card_suit(my_hand[2]))

    the_face = str(find_card_value_int(my_hand[3]))
    if find_card_value_int(my_hand[3]) > 10 or find_card_value_int(my_hand[3]) == 1:
        the_face = find_card_face_string(my_hand[3])
    button_d.__setitem__("text", the_face + " of " + find_card_suit(my_hand[3]))

    the_face = str(find_card_value_int(my_hand[4]))
    if find_card_value_int(my_hand[4]) > 10 or find_card_value_int(my_hand[4]) == 1:
        the_face = find_card_face_string(my_hand[4])
    button_e.__setitem__("text", the_face + " of " + find_card_suit(my_hand[4]))

    button_e.__setitem__("image", card_images[find_card_value_int(my_hand[4])])


    feedback_text.__setitem__("text", rate_the_hand(my_hand))

    return my_hand


WIDTH = 1100
HEIGHT = 600
XPLACEMENT = 400
YPLACEMENT = 50

def resizeImage(img, newWidth, newHeight):
    oldWidth = img.width()
    oldHeight = img.height()
    newPhotoImage = PhotoImage(width=newWidth, height=newHeight)
    for x in range(newWidth):
        for y in range(newHeight):
            xOld = int(x*oldWidth/newWidth)
            yOld = int(y*oldHeight/newHeight)
            rgb = '#%02x%02x%02x' % img.get(xOld, yOld)
            newPhotoImage.put(rgb, (x, y))
    return newPhotoImage


def help_action():
    messagebox.showinfo("Help", f"""
Select one, two or three cards from a dealt hand to determine the odds of various winning poker hands
""")


def quit_action():
    exit(0)


root = Tk()

def load_images():
    """load all the card images into an array with id's corresponding to card numbers"""
    card_images.append(PhotoImage(file="cards/ace_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/2_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/3_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/4_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/5_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/6_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/7_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/8_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/9_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/10_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/jack_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/queen_of_clubs.png"))
    card_images.append(PhotoImage(file="cards/king_of_clubs.png"))
    # for i in range(1, 54):
    #     card_images[i] = resizeImage(card_images[i], 110, 150)



load_images()


helvetica_20 = ("Helvetica", 20, "bold")
comic_sans_20 = ("Comic Sans MS", 20, "bold")
comic_sans_10 = ("Comic Sans MS", 10, "bold")

root.title("Poker Hand Statistics")
root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, XPLACEMENT, YPLACEMENT))
root.minsize(780, 600)

answer_btn_style = ttk.Style()
answer_btn_style.theme_use('classic')
answer_btn_style.configure('AB.TButton', backgroun='#e6f2ff', foreground='black', borderwidth=1,
                           focusthickness=5,
                           focuscolor='gray', font=comic_sans_20, wraplength=100)
answer_btn_style.map('AB.TButton', background=[('active', 'gray71')])

help_btn_style = ttk.Style()
help_btn_style.theme_use('classic')
help_btn_style.configure('HB.TButton', backgroun='gray71', foreground='black', width=20,
                         borderwidth=1,
                         focusthickness=3,
                         focuscolor='green', font=comic_sans_10, wraplength=100)
help_btn_style.map('HB.TButton', background=[('active', 'gray71')])

quit_btn_style = ttk.Style()
quit_btn_style.theme_use('classic')
quit_btn_style.configure('QB.TButton', backgroun='#e6f2ff', foreground='black', width=20,
                         borderwidth=1,
                         focusthickness=3,
                         focuscolor='green', font=comic_sans_10, wraplength=100)
quit_btn_style.map('QB.TButton', background=[('active', 'red')])

main_frame = Frame(root, bd=5, bg="#80c1ff")
main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

myCanvas = Canvas(root, width=WIDTH, height=HEIGHT)
myCanvas.place(relx=0, rely=0, relheight=1, relwidth=1)

#background_image = PhotoImage(file="flag.png")
# background_image = resizeImage(background_image, 1200, 900)

#myCanvas.create_image(0, 0, anchor=NW, image=background_image)

club_image = PhotoImage(file="cards/3_of_hearts.png")
club_image = resizeImage(club_image, 110, 150)


question_frame = LabelFrame(text="", bg='gray71', font=helvetica_20, bd=5, relief=RAISED)
question_frame.place(relx=.025, rely=.05, relwidth=.6, relheight=.2, anchor=NW)

the_question = Label(question_frame,
                     text="Select one, two or three cards from a dealt hand to determine the odds of various winning poker hands. ", font=comic_sans_20, wraplength=400, bg='gray71')
the_question.place(relx=.5, rely=.05, relwidth=.8, relheight=.85, anchor=N)

answer_frame = LabelFrame(font=helvetica_20, bd=5, bg='gray71', fg='black', relief=RAISED)
answer_frame.place(relx=.025, rely=.28, relwidth=.6, relheight=.4, anchor=NW)

answer_a = str(find_card_value_int(my_hand[0])) + " of " + find_card_suit(my_hand[0])
answer_b = str(find_card_face_string(my_hand[1])) + " of " + find_card_suit(my_hand[1])
answer_c = str(find_card_face_string(my_hand[2])) + " of " + find_card_suit(my_hand[2])
answer_d = str(find_card_face_string(my_hand[3])) + " of " + find_card_suit(my_hand[3])
answer_e = str(find_card_face_string(my_hand[4])) + " of " + find_card_suit(my_hand[4])

score_frame = LabelFrame(font=helvetica_20, bg='gray71', bd=5, relief=RAISED)
score_frame.place(relx=.65, rely=.05, relwidth=.32, relheight=.75, anchor=NW)

rf_score = Label(score_frame, text="Royal Flush = " + "1 of 3000", anchor='center', width=10, font=comic_sans_20, bg='gray71')
rf_score.place(relx=.05, rely=.05, relwidth=.9, relheight=.1, anchor=NW)

sf_score = Label(score_frame, text="Straight Flush = " + "1 0f 40", anchor='center', width=10, font=comic_sans_20, bg='gray71')
sf_score.place(relx=.05, rely=.15, relwidth=.9, relheight=.1, anchor=NW)

four_score = Label(score_frame, text="4 of a Kind = " + "1 of 25", anchor='center', width=10, font=comic_sans_20, bg='gray71')
four_score.place(relx=.05, rely=.25, relwidth=.9, relheight=.1, anchor=NW)

fh_score = Label(score_frame, text="Full House = " + "1 of 20", anchor='center', width=10, font=comic_sans_20, bg='gray71')
fh_score.place(relx=.05, rely=.35, relwidth=.9, relheight=.1, anchor=NW)

flush_score = Label(score_frame, text="Flush = " + "1 of 15", anchor='center', width=10, font=comic_sans_20, bg='gray71')
flush_score.place(relx=.05, rely=.45, relwidth=.9, relheight=.1, anchor=NW)

straight_score = Label(score_frame, text="Straight = " + "1 of 12", anchor='center', width=10, font=comic_sans_20, bg='gray71')
straight_score.place(relx=.05, rely=.55, relwidth=.9, relheight=.1, anchor=NW)

three_score = Label(score_frame, text="3 of a Kind = " + "1 of 10", anchor='center', width=10, font=comic_sans_20, bg='gray71')
three_score.place(relx=.05, rely=.65, relwidth=.9, relheight=.1, anchor=NW)

two_pair_score = Label(score_frame, text="Two Pair = " + "1 of 7", anchor='center', width=10, font=comic_sans_20, bg='gray71')
two_pair_score.place(relx=.05, rely=.75, relwidth=.9, relheight=.1, anchor=NW)

a_pair_score = Label(score_frame, text="One Pair = " + "1 of 5", anchor='center', width=10, font=comic_sans_20, bg='gray71')
a_pair_score.place(relx=.05, rely=.85, relwidth=.9, relheight=.1, anchor=NW)

letter = "A"


def choice_made(the_choice):
    global letter
    if the_choice == "A":
        letter = "A"
        feedback_text.__setitem__("text", "You selected 'A'")
        button_a.__setitem__("text", "Right")
    elif the_choice == "B":
        letter = "B"
        feedback_text.__setitem__("text", "You selected 'B'")
        button_b.__setitem__("text", "Nope")
    elif the_choice == "C":
        letter = "C"
        feedback_text.__setitem__("text", "You selected 'C'")
        button_c.__setitem__("text", "Nope")
    elif the_choice == "D":
        letter = "D"
        feedback_text.__setitem__("text", "You selected 'D'")
        button_d.__setitem__("text", "Nope")
    elif the_choice == "E":
        letter = "E"
        feedback_text.__setitem__("text", "You selected 'E'")
        button_d.__setitem__("text", "Nope")


feedback_frame = LabelFrame(font=comic_sans_20, bg='gray71', bd=5, relief=RAISED)
feedback_frame.place(relx=.025, rely=.7, relwidth=.6, relheight=.1, anchor=NW)

feedback_text = Label(feedback_frame, text=f"^Click on your choice.^", bg='gray71', anchor='center', width=10,
                      font=comic_sans_20)
feedback_text.place(relx=.5, rely=.05, relwidth=.8, relheight=.9, anchor=N)

help_button_frame = LabelFrame(font=comic_sans_20, bg='gray71', bd=5, relief=RAISED)
help_button_frame.place(relx=.225, rely=.82, relwidth=.1, relheight=.1, anchor=NW)
help_button = ttk.Button(help_button_frame, text="HELP", command=help_action, style='HB.TButton')
help_button.place(relx=.05, rely=.0, relwidth=.9, relheight=.95, anchor=NW)

deal_button_frame = LabelFrame(font=comic_sans_20, bg='gray71', bd=5, relief=RAISED)
deal_button_frame.place(relx=.9, rely=.82, relwidth=.1, relheight=.1, anchor=NE)
deal_button = ttk.Button(deal_button_frame, text="DEAL", command=start_by_dealing, style='HB.TButton')
deal_button.place(relx=.05, rely=.0, relwidth=.9, relheight=.95, anchor=NW)

quit_button_frame = LabelFrame(font=comic_sans_20, bg='gray71', bd=5, relief=RAISED)
quit_button_frame.place(relx=.1, rely=.82, relwidth=.1, relheight=.1, anchor=NW)
quit_button = ttk.Button(quit_button_frame, text="QUIT", command=quit_action, style='HB.TButton')
quit_button.place(relx=.05, rely=0, relwidth=.9, relheight=.95, anchor=NW)

button_a = ttk.Button(answer_frame, text=answer_a, image=card_images[my_hand[0]], command=lambda: choice_made("A"), style='AB.TButton')
button_b = ttk.Button(answer_frame, text=answer_b, command=lambda: choice_made("B"), style='AB.TButton')
button_c = ttk.Button(answer_frame, text=answer_c, command=lambda: choice_made("C"), style='AB.TButton')
button_d = ttk.Button(answer_frame, text=answer_d, command=lambda: choice_made("D"), style='AB.TButton')
button_e = ttk.Button(answer_frame, text=answer_e, image=card_images[my_hand[4]],command=lambda: choice_made("E"), style='AB.TButton')

button_a.place(relx=.005, rely=.01, relwidth=.2, relheight=.98, anchor=NW)
button_b.place(relx=.2, rely=.01, relwidth=.2, relheight=.98, anchor=NW)
button_c.place(relx=.4, rely=.01, relwidth=.2, relheight=.98, anchor=NW)
button_d.place(relx=.6, rely=.01, relwidth=.2, relheight=.98, anchor=NW)
button_e.place(relx=.8, rely=.01, relwidth=.2, relheight=.98, anchor=NW)



root.mainloop()
