import math
import random
from random import seed
from random import randint
#to generate seed number
#seed(101)
#random number generation within 0 to 5

the_cards = []
card_is_used = []
all_possible_hands = []
a_hand = []

for i in range(1, 54):
    the_cards.append(i)
    card_is_used.append(False)

for i in range(1, 54):
    the_cards.append(i)
    card_is_used.append(False)


def deal(the_hand):
    for i in range(1, 54):
        card_is_used[i] = False

    for _ in range(5):
        a_card = randint(1,52)
        while card_is_used[a_card]:
            a_card = randint(1,52)
            print("Card is used - pick another.")
        the_hand.append(a_card)
        card_is_used[a_card] = True
    # print(sorted(the_hand))
    return sorted(the_hand)

def all_hands_lister():
    for i in range(300):
        a_hand = []
        one_hand = deal(a_hand)
        if one_hand not in all_possible_hands:
            all_possible_hands.append("xxx")
            all_possible_hands[i] = deal(a_hand)
    # print(deal(one_hand))
    return all_possible_hands


#  1-13 are spades A-K
# 14-26 are hearts
# 27-39 are diamonds
# 40-52 are clubs

def find_card_value(card_id):
    value = card_id
    if value > 39:
        value = value - 13
    if value > 26:
        value = value - 13
    if value > 12:
        value = value - 13

    if card_id == 1 or card_id == 14 or card_id == 27 or card_id == 40:
        value = "Ace"
    if card_id == 11 or card_id == 24 or card_id == 37 or card_id == 50:
        value = "Jack"
    if card_id == 12 or card_id == 25 or card_id == 38 or card_id == 51:
        value = "Queen"
    if card_id == 13 or card_id == 26 or card_id == 39 or card_id == 52:
        value = "King"
    return str(value)


def find_card_face(card_id):
    if 0 < card_id < 14:  # spades
        return "spades"
    elif 13 < card_id < 27:  # hearts
        return "hearts"
    elif 26 < card_id < 40:  # diamonds
        return "diamonds"
    elif 39 < card_id < 53:  # clubs
        return "clubs"
    else:
        return "ERROR"


def combination(n, r):
    numerator = math.factorial(n)
    denominator = math.factorial(n - r) * math.factorial(r)
    return numerator / denominator


def probability(the_hand):
    # probability of a hand after being dealt 5 random cards.
    number_of_possible_hands = combination(52, 5)
    if the_hand == "royal flush":
        return 4 / number_of_possible_hands
    elif the_hand == "straight flush":
        return 40 / number_of_possible_hands
    elif the_hand == "4OAK":  # -- stands for 4 Of A Kind
        return combination(4, 4) * 13 * 48 / number_of_possible_hands
    elif the_hand == "full house":
        return 12 * 13 * combination(4, 2) * combination(4, 3) / number_of_possible_hands
    elif the_hand == "flush":
        return (4 * combination(13, 5) - 40) / number_of_possible_hands
    elif the_hand == "straight":
        return (10 * 4 ** 5 - 40) / number_of_possible_hands
    elif the_hand == "3OAK":
        return (13 * combination(4, 3) * (48 * 44) / 2) / number_of_possible_hands
    elif the_hand == "two pair":
        return (combination(13, 2) * combination(4, 2) ** 2 * 44) / number_of_possible_hands
    elif the_hand == "one pair":
        return 13 * combination(4, 2) * (48 * 44 * 40) / 6 / number_of_possible_hands
    elif the_hand == "high card":
        return (52 * 48 * 44 * 40 * 36 / 120 - 40 - 5108 - 10200) / number_of_possible_hands
    else:
        return 0


# print(combination(52, 5))
# print("%.8f" % probability("royal flush"))
# print("%.8f" % probability("straight flush"))
# print("%.8f" % probability("4OAK"))
# print("%.8f" % probability("full house"))
# print("%.8f" % probability("flush"))
# print("%.8f" % probability("straight"))
# print("%.8f" % probability("3OAK"))
# print("%.8f" % probability("two pair"))
# print("%.8f" % probability("one pair"))
# print("%.8f" % probability("high card"))


# id = 25
# print(find_card_value(id) + " of " + find_card_face(id))


my_hand = deal(a_hand)
print(my_hand)

for item in range(5):
    print(find_card_value(my_hand[item]) + " of " + find_card_face(my_hand[item]))

print("\n")

all_possible_hands = all_hands_lister()

for i in range(0, len(all_possible_hands)):
    print(all_possible_hands[i])