from tkinter import *
from tkinter import ttk

card_images = []
list_of_hand_probs = [0] * 10
list_of_hand_counts = [0] * 10

helvetica_20 = ("Helvetica", 20, "bold")
comic_sans_20 = ("Comic Sans MS", 20, "bold")
comic_sans_10 = ("Comic Sans MS", 10, "bold")

my_hand = [10, 11, 12, 13, 1]

ROYAL_FLUSH = 0
STRAIGHT_FLUSH = 1
FOUR_OAK = 2
FULL_HOUSE = 3
FLUSH = 4
STRAIGHT = 5
THREE_OAK = 6
TWO_PAIR = 7
ONE_PAIR = 8
HIGH_CARD = 9

list_of_hand_probs[ROYAL_FLUSH] = "12 in 649739.00"
list_of_hand_probs[STRAIGHT_FLUSH] = "1 in 72192.33"
list_of_hand_probs[FOUR_OAK] = "1 in 4164.00"
list_of_hand_probs[FULL_HOUSE] = "1 in 693.17"
list_of_hand_probs[FLUSH] = "1 in 508.80"
list_of_hand_probs[STRAIGHT] = "1 in 253.80"
list_of_hand_probs[THREE_OAK] = "1 in 46.33"
list_of_hand_probs[TWO_PAIR] = "1 in 20.04"
list_of_hand_probs[ONE_PAIR] = "1 in 2.37"
list_of_hand_probs[HIGH_CARD] = "1 in .99"

list_of_hand_counts[ROYAL_FLUSH] = 0
list_of_hand_counts[STRAIGHT_FLUSH] = 0
list_of_hand_counts[FOUR_OAK] = 0
list_of_hand_counts[FULL_HOUSE] = 0
list_of_hand_counts[FLUSH] = 0
list_of_hand_counts[STRAIGHT] = 0
list_of_hand_counts[THREE_OAK] = 0
list_of_hand_counts[TWO_PAIR] = 0
list_of_hand_counts[ONE_PAIR] = 0
list_of_hand_counts[HIGH_CARD] = 0




