from random import randint

the_cards = []
card_is_used = []
all_possible_hands = []
a_hand = []


for index in range(1, 54):
    the_cards.append(index)
    card_is_used.append(False)

def count_values(this_hand, a_card):
    """looking for two, three, four of a kind"""
    count = 0
    for ele in this_hand:
        if find_card_value_int(ele) == find_card_value_int(a_card):
            count = count + 1
    return count


#  1-13 are spades A-K
# 14-26 are hearts
# 27-39 are diamonds
# 40-52 are clubs

def find_card_value_int(card_id):
    """find the integer value of cards"""
    value = card_id
    if value > 39:
        value = value - 13
    if value > 26:
        value = value - 13
    if value > 12:
        value = value - 13

    if card_id in (1, 14, 27, 40):
        value = 1
    if card_id in (11, 24, 37, 50):
        value = 11
    if card_id in (12, 25, 38, 51):
        value = 12
    if card_id in (13, 26, 39, 52):
        value = 13
    return value


def find_card_face_string(card_id):
    """find face value of a card"""
    face = card_id
    if face > 39:
        face = face - 13
    if face > 26:
        face = face - 13
    if face > 12:
        face = face - 13

    if card_id in (1, 14, 27, 40):
        face = "Ace"
    if card_id in (11, 24, 37, 50):
        face = "Jack"
    if card_id in (12, 25, 38, 51):
        face = "Queen"
    if card_id in (13, 26, 39, 52):
        face = "King"
    return str(face)


def find_card_suit(card_id):
    """find the suit of a card"""
    if 0 < card_id < 14:  # spades
        return "spades"
    if 13 < card_id < 27:  # hearts
        return "hearts"
    if 26 < card_id < 40:  # diamonds
        return "diamonds"
    if 39 < card_id < 53:  # clubs
        return "clubs"
    return "ERROR"

