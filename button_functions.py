from config import *
from hand_rating import *
from tkinter import messagebox
from random import randint


def deal():
    """deal the hand"""

    global my_hand
    card_is_used = []
    for index in range(0, 54):
        card_is_used.append(False)

    my_hand = []
    for i in range(1, 54):
        card_is_used[i] = False

    for _ in range(5):
        a_card = randint(1, 52)
        while card_is_used[a_card]:
            a_card = randint(1, 52)
            # print("Card is used - pick another.")
        my_hand.append(a_card)
        card_is_used[a_card] = True

    return sorted(my_hand)


def help_action():
    messagebox.showinfo("Help", f"""
Select one, two or three cards from a dealt hand to determine the odds of various winning poker hands
""")


def quit_action():
    exit(0)


def discard_one(card_number):
    """ throw out the 'card numberth' card from my hand and see what happens"""

    global list_of_hand_probs
    for i in range(0, 10):
        list_of_hand_probs[i] = 0
        list_of_hand_counts[i] = 0

    my_new_hand = my_hand.copy()
    my_new_hand = sorted(my_new_hand)
    #print(f"my new hand from discard one is {my_new_hand} and we're changing number {card_number}")

    for card in range(1, 53):
        if card not in my_new_hand:
            #my_new_hand = my_hand.copy()
            my_new_hand[card_number] = card
            #my_new_hand = sorted(my_new_hand)
            #print(f"My new hand from discard one: {my_new_hand}")
            if is_it_royal_flush(sorted(my_new_hand)):
                list_of_hand_counts[ROYAL_FLUSH] = + 1
            if is_it_a_straight(sorted(my_new_hand)) and is_it_a_flush(sorted(my_new_hand)):
                list_of_hand_counts[STRAIGHT_FLUSH] += 1
            if is_it_4_of_a_kind(sorted(my_new_hand)):
                list_of_hand_counts[FOUR_OAK] += 1
            if is_it_a_full_house(sorted(my_new_hand)):
                list_of_hand_counts[FULL_HOUSE] += 1
            if is_it_a_flush(sorted(my_new_hand)):
                list_of_hand_counts[FLUSH] += 1
            if is_it_a_straight(sorted(my_new_hand)):
                list_of_hand_counts[STRAIGHT] += 1
            if is_it_3_of_a_kind(sorted(my_new_hand)):
                list_of_hand_counts[THREE_OAK] += 1
            if is_it_2_pair(sorted(my_new_hand)):
                list_of_hand_counts[TWO_PAIR] += 1
            if is_it_a_pair(sorted(my_new_hand)):
                list_of_hand_counts[ONE_PAIR] += 1

    list_of_hand_probs[ROYAL_FLUSH] = "Royal Flush = {0:.2f}%".format(list_of_hand_counts[ROYAL_FLUSH] / 47 * 100)
    list_of_hand_probs[STRAIGHT_FLUSH] = "Straight Flush = {0:.2f}%".format(
        list_of_hand_counts[STRAIGHT_FLUSH] / 47 * 100)
    list_of_hand_probs[FOUR_OAK] = "Four of a Kind = {0:.2f}%".format(list_of_hand_counts[FOUR_OAK] / 47 * 100)
    list_of_hand_probs[FULL_HOUSE] = "Full House = {0:.2f}%".format(list_of_hand_counts[FULL_HOUSE] / 47 * 100)
    list_of_hand_probs[FLUSH] = "Flush = {0:.2f}%".format(list_of_hand_counts[FLUSH] / 47 * 100)
    list_of_hand_probs[STRAIGHT] = "Straight = {0:.2f}%".format(list_of_hand_counts[STRAIGHT] / 47 * 100)
    list_of_hand_probs[THREE_OAK] = "Three of a Kind = {0:.2f}%".format(list_of_hand_counts[THREE_OAK] / 47 * 100)
    list_of_hand_probs[TWO_PAIR] = "Two Pair = {0:.2f}%".format(list_of_hand_counts[TWO_PAIR] / 47 * 100)
    list_of_hand_probs[ONE_PAIR] = "One Pair = {0:.2f}%".format(list_of_hand_counts[ONE_PAIR] / 47 * 100)

    return


def check_the_currently_dealt_hand():
    """ after the hand is dealt,  what do we have?"""

    global list_of_hand_probs
    for i in range(0, 10):
        list_of_hand_probs[i] = 0
        list_of_hand_counts[i] = 0

    if is_it_royal_flush(my_hand):
        list_of_hand_counts[ROYAL_FLUSH] = 47
    if is_it_a_straight(my_hand) and is_it_a_flush(my_hand):
        list_of_hand_counts[STRAIGHT_FLUSH] = 47
    if is_it_4_of_a_kind(my_hand):
        list_of_hand_counts[FOUR_OAK] = 47
    if is_it_a_full_house(my_hand):
        list_of_hand_counts[FULL_HOUSE] = 47
    if is_it_a_flush(my_hand):
        list_of_hand_counts[FLUSH] = 47
    if is_it_a_straight(my_hand):
        list_of_hand_counts[STRAIGHT] = 47
    if is_it_3_of_a_kind(my_hand):
        list_of_hand_counts[THREE_OAK] = 47
    if is_it_2_pair(my_hand):
        list_of_hand_counts[TWO_PAIR] = 47
    if is_it_a_pair(my_hand):
        list_of_hand_counts[ONE_PAIR] = 47

    print(f"full house count {list_of_hand_counts[FULL_HOUSE]}")
    print(f"ONE_PAIR count {list_of_hand_counts[ONE_PAIR]}")

    list_of_hand_probs[ROYAL_FLUSH] = "Royal Flush = {0:.2f}%".format(list_of_hand_counts[ROYAL_FLUSH] / 47 * 100)
    list_of_hand_probs[STRAIGHT_FLUSH] = "Straight Flush = {0:.2f}%".format(list_of_hand_counts[STRAIGHT_FLUSH] / 47 * 100)
    list_of_hand_probs[FOUR_OAK] = "Four of a Kind = {0:.2f}%".format(list_of_hand_counts[FOUR_OAK] / 47 * 100)
    list_of_hand_probs[FULL_HOUSE] = "Full House = {0:.2f}%".format(list_of_hand_counts[FULL_HOUSE] / 47 * 100)
    list_of_hand_probs[FLUSH] = "Flush = {0:.2f}%".format(list_of_hand_counts[FLUSH] / 47 * 100)
    list_of_hand_probs[STRAIGHT] = "Straight = {0:.2f}%".format(list_of_hand_counts[STRAIGHT] / 47 * 100)
    list_of_hand_probs[THREE_OAK] = "Three of a Kind = {0:.2f}%".format(list_of_hand_counts[THREE_OAK] / 47 * 100)
    list_of_hand_probs[TWO_PAIR] = "Two Pair = {0:.2f}%".format(list_of_hand_counts[TWO_PAIR] / 47 * 100)
    list_of_hand_probs[ONE_PAIR] = "One Pair = {0:.2f}%".format(list_of_hand_counts[ONE_PAIR] / 47 * 100)

    return
