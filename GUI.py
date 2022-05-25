from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import tkinter.font
import re
import math

from probability_calcs import *
from card_utilities import *
from hand_rating import *
from card_images import *
# from config import my_hand, card_images, helvetica_20, comic_sans_20, comic_sans_10
from config import list_of_hand_counts
from button_functions import discard_one, quit_action, help_action, deal, check_the_currently_dealt_hand
from config import comic_sans_20, comic_sans_10, helvetica_20, list_of_hand_probs, my_hand
from config import ROYAL_FLUSH, STRAIGHT_FLUSH, FOUR_OAK, THREE_OAK, FULL_HOUSE, STRAIGHT, FLUSH, TWO_PAIR, ONE_PAIR
from config import discard_card_0, discard_card_1, discard_card_2, discard_card_3, discard_card_4

WIDTH = 1220
HEIGHT = 600
XPLACEMENT = 50
YPLACEMENT = 50

root = Tk()

root.title("Poker Hand Statistics")
root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, XPLACEMENT, YPLACEMENT))
root.minsize(WIDTH, HEIGHT)

main_frame = Frame(root, bd=5, bg="#264d00")
main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

load_images()


def find_pressed_buttons():
    i_count = 0
    this_card = -1

    if discard_card_0:
        i_count += 1
        this_card = 0

    if discard_card_1:
        i_count += 1
        this_card = 1

    if discard_card_2:
        i_count += 1
        this_card = 2

    if discard_card_3:
        i_count += 1
        this_card = 3

    if discard_card_4:
        i_count += 1
        this_card = 4

    if i_count == 1:
        discard_one(this_card)

    update_sccore_sheet()


def start_by_dealing():
    my_hand = deal()
    print(f"my hand from start---{my_hand}")
    card_0.config(image=card_images[my_hand[0]],
                  text=str(find_card_face_string(my_hand[0])) + " of " + find_card_suit(my_hand[0]))
    card_1.config(image=card_images[my_hand[1]],
                  text=str(find_card_face_string(my_hand[1])) + " of " + find_card_suit(my_hand[1]))
    card_2.config(image=card_images[my_hand[2]],
                  text=str(find_card_face_string(my_hand[2])) + " of " + find_card_suit(my_hand[2]))
    card_3.config(image=card_images[my_hand[3]],
                  text=str(find_card_face_string(my_hand[3])) + " of " + find_card_suit(my_hand[3]))
    card_4.config(image=card_images[my_hand[4]],
                  text=str(find_card_face_string(my_hand[4])) + " of " + find_card_suit(my_hand[4]))
    feedback_text.__setitem__("text", rate_the_hand(my_hand))
    check_the_currently_dealt_hand()
    update_sccore_sheet()
    card_0.state(['!pressed'])
    card_1.state(['!pressed'])
    card_2.state(['!pressed'])
    card_3.state(['!pressed'])
    card_4.state(['!pressed'])

    global discard_card_0
    global discard_card_1
    global discard_card_2
    global discard_card_3
    global discard_card_4

    discard_card_0 = False
    discard_card_1 = False
    discard_card_2 = False
    discard_card_3 = False
    discard_card_4 = False

    return my_hand


# --------------------------------------BUTTON STYLES---------------------------------------------------------------

help_btn_style = ttk.Style()
help_btn_style.theme_use('classic')
help_btn_style.configure('HB.TButton', backgroun='gray71', foreground='#006600', width=25,
                         borderwidth=1,
                         focusthickness=3,
                         focuscolor='green', font=helvetica_20, wraplength=100)
help_btn_style.map('HB.TButton', background=[('active', '#006600')], foreground=[('active', 'black')])

quit_btn_style = ttk.Style()
quit_btn_style.theme_use('classic')
quit_btn_style.configure('QB.TButton', backgroun='gray71', foreground='#ff3300', width=25,
                         borderwidth=1,
                         focusthickness=3,
                         focuscolor='green', font=helvetica_20, wraplength=100)
quit_btn_style.map('QB.TButton', background=[('active', '#ff3300')], foreground=[('active', 'black')])

calc_btn_style = ttk.Style()
calc_btn_style.theme_use('classic')
calc_btn_style.configure('CALC.TButton', background='gray71', foreground='#006600', width=55,
                         borderwidth=1,
                         focusthickness=3,
                         focuscolor='green', font=helvetica_20, wraplength=1000)
calc_btn_style.map('CALC.TButton', background=[('active', '#006600')], foreground=[('active', 'black')])

# -----------------------------------HEADER FRAME-----------------------------------------------------------------

header_frame = LabelFrame(text="", bg='gray71', font=helvetica_20, bd=5, relief=RAISED)
header_frame.place(relx=.025, rely=.05, relwidth=.6, relheight=.2, anchor=NW)

the_header = Label(header_frame,
                   text="Select one, two or three cards from a dealt hand to determine the odds of various winning poker hands. ",
                   font=comic_sans_20, wraplength=400, bg='gray71')
the_header.place(relx=.5, rely=.05, relwidth=.8, relheight=.85, anchor=N)

# ----------------------------------SCORE FRAME AND LABELS--------------------------------------------------------------------

score_frame = LabelFrame(font=helvetica_20, bg='gray71', bd=5, relief=RAISED)
score_frame.place(relx=.65, rely=.05, relwidth=.32, relheight=.75, anchor=NW)

rf_score = Label(score_frame, text="Royal Flush = " + list_of_hand_probs[ROYAL_FLUSH], anchor='w', width=10,
                 font=comic_sans_20, bg='gray71')
rf_score.place(relx=.05, rely=.05, relwidth=.9, relheight=.1, anchor=NW)

sf_score = Label(score_frame, text="Straight Flush = " + list_of_hand_probs[STRAIGHT_FLUSH], anchor='w', width=10,
                 font=comic_sans_20, bg='gray71')
sf_score.place(relx=.05, rely=.15, relwidth=.9, relheight=.1, anchor=NW)

four_score = Label(score_frame, text="4 of a Kind = " + list_of_hand_probs[FOUR_OAK], anchor='w', width=10,
                   font=comic_sans_20, bg='gray71')
four_score.place(relx=.05, rely=.25, relwidth=.9, relheight=.1, anchor=NW)

fh_score = Label(score_frame, text="Full House = " + list_of_hand_probs[FULL_HOUSE], anchor='w', width=10,
                 font=comic_sans_20, bg='gray71')
fh_score.place(relx=.05, rely=.35, relwidth=.9, relheight=.1, anchor=NW)

flush_score = Label(score_frame, text="Flush = " + list_of_hand_probs[FLUSH], anchor='w', width=10, font=comic_sans_20,
                    bg='gray71')
flush_score.place(relx=.05, rely=.45, relwidth=.9, relheight=.1, anchor=NW)

straight_score = Label(score_frame, text="Straight = " + list_of_hand_probs[STRAIGHT], anchor='w', width=10,
                       font=comic_sans_20, bg='gray71')
straight_score.place(relx=.05, rely=.55, relwidth=.9, relheight=.1, anchor=NW)

three_score = Label(score_frame, text="3 of a Kind = " + list_of_hand_probs[THREE_OAK], anchor='w', width=10,
                    font=comic_sans_20, bg='gray71')
three_score.place(relx=.05, rely=.65, relwidth=.9, relheight=.1, anchor=NW)

two_pair_score = Label(score_frame, text="Two Pair = " + list_of_hand_probs[TWO_PAIR], anchor='w', width=10,
                       font=comic_sans_20, bg='gray71')
two_pair_score.place(relx=.05, rely=.75, relwidth=.9, relheight=.1, anchor=NW)

one_pair_score = Label(score_frame, text="One Pair = " + list_of_hand_probs[ONE_PAIR], anchor='w', width=10,
                       font=comic_sans_20, bg='gray71')
one_pair_score.place(relx=.05, rely=.85, relwidth=.9, relheight=.1, anchor=NW)

# ---------------------------------FEEDBACK, HELP AND QUIT BUTTONS-----------------------------------------------------

feedback_frame = LabelFrame(font=comic_sans_20, bg='gray71', bd=5, relief=RAISED)
feedback_frame.place(relx=.025, rely=.635, relwidth=.6, relheight=.165, anchor=NW)

feedback_text = Label(feedback_frame, text=f"^Click on your choice.^", bg='gray71', anchor='center', width=10,
                      font=comic_sans_20)

feedback_text.place(relx=.5, rely=.05, relwidth=.8, relheight=.9, anchor=N)

help_button_frame = LabelFrame(font=comic_sans_20, bg='gray71', bd=5, relief=RAISED)
help_button_frame.place(relx=.14, rely=.82, relwidth=.1, relheight=.1, anchor=NW)
help_button = ttk.Button(help_button_frame, text="HELP", command=help_action, style='HB.TButton')
help_button.place(relx=.0, rely=.0, relwidth=1.0, relheight=.95, anchor=NW)

deal_button_frame = LabelFrame(font=comic_sans_20, bg='gray71', bd=5, relief=RAISED)
deal_button_frame.place(relx=.65, rely=.82, relwidth=.33, relheight=.1, anchor=NW)
deal_button = ttk.Button(deal_button_frame, text="DEAL", command=lambda: start_by_dealing(), style='HB.TButton')
deal_button.place(relx=.0, rely=.0, relwidth=1.0, relheight=.95, anchor=NW)

quit_button_frame = LabelFrame(font=comic_sans_20, bg='gray71', bd=5, relief=RAISED)
quit_button_frame.place(relx=.025, rely=.82, relwidth=.1, relheight=.1, anchor=NW)
quit_button = ttk.Button(quit_button_frame, text="QUIT", command=quit_action, style='QB.TButton')
quit_button.place(relx=.05, rely=0, relwidth=.9, relheight=.95, anchor=NW)

calculate_button_frame = LabelFrame(font=comic_sans_10, bg='gray71', bd=5, relief=RAISED)
calculate_button_frame.place(relx=.25, rely=.82, relwidth=.375, relheight=.1, anchor=NW)
calculate_button = ttk.Button(calculate_button_frame, text="CALCULATE", command=find_pressed_buttons,
                              style='CALC.TButton')
calculate_button.place(relx=.5, rely=0, relwidth=1.0, relheight=.95, anchor=N)


# ---------------------------------CARD BUTTONS AND CHOICES-----------------------------------------------------

def choice_made(the_choice):
    global discard_card_0
    global discard_card_1
    global discard_card_2
    global discard_card_3
    global discard_card_4
    if the_choice == "A":
        feedback_text.__setitem__("text", "Discarding " + card_0["text"])
        discard_card_0 = True
    elif the_choice == "B":
        feedback_text.__setitem__("text", "Discarding " + card_1["text"])
        discard_card_1 = True
    elif the_choice == "C":
        feedback_text.__setitem__("text", "Discarding " + card_2["text"])
        discard_card_2 = True
    elif the_choice == "D":
        feedback_text.__setitem__("text", "Discarding " + card_3["text"])
        discard_card_3 = True
    elif the_choice == "E":
        feedback_text.__setitem__("text", "Discarding " + card_4["text"])
        discard_card_4 = True


def update_sccore_sheet():
    list_of_hand_probs[ROYAL_FLUSH] = "Royal Flush = {0:.2f}%".format(list_of_hand_counts[ROYAL_FLUSH] / 47 * 100)
    list_of_hand_probs[STRAIGHT_FLUSH] = "Straight Flush = {0:.2f}%".format(
        list_of_hand_counts[STRAIGHT_FLUSH] / 47 * 100)
    list_of_hand_probs[FOUR_OAK] = "Four of a Kind = {0:.2f}%".format(list_of_hand_counts[FOUR_OAK] / 47 * 100)
    list_of_hand_probs[FULL_HOUSE] = "Full House = {0:.2f}%".format(list_of_hand_counts[FULL_HOUSE] / 47 * 100)
    list_of_hand_probs[FLUSH] = "Flush = {0:.2f}%".format(list_of_hand_counts[FLUSH] / 47 * 100)
    list_of_hand_probs[STRAIGHT] = "Straight = {0:.2f}%".format(list_of_hand_counts[STRAIGHT] / 47 * 100)
    list_of_hand_probs[THREE_OAK] = "Three of a Kind = {0:.2f}%".format(list_of_hand_counts[THREE_OAK] / 47 * 100)
    list_of_hand_probs[TWO_PAIR] = "Two Pair = {0:.2f}%".format(list_of_hand_counts[TWO_PAIR] / 47 * 100)
    list_of_hand_probs[ONE_PAIR] = "A Pair = {0:.2f}%".format(list_of_hand_counts[ONE_PAIR] / 47 * 100)

    rf_score.config(text=list_of_hand_probs[ROYAL_FLUSH])
    sf_score.config(text=list_of_hand_probs[STRAIGHT_FLUSH])
    four_score.config(text=list_of_hand_probs[FOUR_OAK])
    fh_score.config(text=list_of_hand_probs[FULL_HOUSE])
    flush_score.config(text=list_of_hand_probs[FLUSH])
    straight_score.config(text=list_of_hand_probs[STRAIGHT])
    three_score.config(text=list_of_hand_probs[THREE_OAK])
    two_pair_score.config(text=list_of_hand_probs[TWO_PAIR])
    one_pair_score.config(text=list_of_hand_probs[ONE_PAIR])


card_frame = LabelFrame(font=helvetica_20, bd=2, bg='gray71')
card_frame.place(relx=.025, rely=.28, relwidth=.6, relheight=.32, anchor=NW)

card_btn_style = ttk.Style()
card_btn_style.theme_use('classic')
card_btn_style.configure('CB.TButton', background='#e6f2ff', foreground='black', borderwidth=8,
                         focusthickness=5,
                         focuscolor='gray', font=comic_sans_20, wraplength=100, relief=RAISED)
card_btn_style.map('CB.TButton', background=[('active', '#006600')])

card_0 = ttk.Button(card_frame, text=str(find_card_face_string(my_hand[0])) + " of " + find_card_suit(my_hand[0]),
                    image=card_images[my_hand[0]], command=lambda: choice_made("A"), style='CB.TButton')
card_1 = ttk.Button(card_frame, text=str(find_card_face_string(my_hand[1])) + " of " + find_card_suit(my_hand[1]),
                    image=card_images[my_hand[1]], command=lambda: choice_made("B"), style='CB.TButton')
card_2 = ttk.Button(card_frame, text=str(find_card_face_string(my_hand[2])) + " of " + find_card_suit(my_hand[2]),
                    image=card_images[my_hand[2]], command=lambda: choice_made("C"), style='CB.TButton')
card_3 = ttk.Button(card_frame, text=str(find_card_face_string(my_hand[3])) + " of " + find_card_suit(my_hand[3]),
                    image=card_images[my_hand[3]], command=lambda: choice_made("D"), style='CB.TButton')
card_4 = ttk.Button(card_frame, text=str(find_card_face_string(my_hand[4])) + " of " + find_card_suit(my_hand[4]),
                    image=card_images[my_hand[4]], command=lambda: choice_made("E"), style='CB.TButton')

card_0.place(relx=.1, rely=.5, relwidth=.2, relheight=.98, anchor=CENTER)
card_1.place(relx=.3, rely=.5, relwidth=.2, relheight=.98, anchor=CENTER)
card_2.place(relx=.5, rely=.5, relwidth=.2, relheight=.98, anchor=CENTER)
card_3.place(relx=.7, rely=.5, relwidth=.2, relheight=.98, anchor=CENTER)
card_4.place(relx=.9, rely=.5, relwidth=.2, relheight=.98, anchor=CENTER)

root.mainloop()
