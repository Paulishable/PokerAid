import math

the_cards = []
card_is_used = []
all_possible_hands = []
a_hand = []


def combination(total_num, taken_at_a_time):
    """mathematical  combination calculation"""
    numerator = math.factorial(total_num)
    denominator = math.factorial(total_num - taken_at_a_time) * math.factorial(taken_at_a_time)
    return numerator / denominator


def probability(a_particular_hand):
    """probability calculations for a dealt hand"""
    number_of_possible_hands = combination(52, 5)
    if a_particular_hand == "royal flush":
        return 4 / number_of_possible_hands
    if a_particular_hand == "straight flush":
        return 40 / number_of_possible_hands
    if a_particular_hand == "4OAK":  # -- stands for 4 Of A Kind
        return combination(4, 4) * 13 * 48 / number_of_possible_hands
    if a_particular_hand == "full house":
        return 12 * 13 * combination(4, 2) * combination(4, 3) / number_of_possible_hands
    if a_particular_hand == "flush":
        return (4 * combination(13, 5) - 40) / number_of_possible_hands
    if a_particular_hand == "straight":
        return (10 * 4 ** 5 - 40) / number_of_possible_hands
    if a_particular_hand == "3OAK":
        return (13 * combination(4, 3) * (48 * 44) / 2) / number_of_possible_hands
    if a_particular_hand == "two pair":
        return (combination(13, 2) * combination(4, 2) ** 2 * 44) / number_of_possible_hands
    if a_particular_hand == "one pair":
        return 13 * combination(4, 2) * (48 * 44 * 40) / 6 / number_of_possible_hands
    if a_particular_hand == "high card":
        return (52 * 48 * 44 * 40 * 36 / 120 - 40 - 5108 - 10200) / number_of_possible_hands
    return 0


def number_of_good_hands():
    """ calculate how many good hands are possible in 5 cards"""
    total = 0
    # "from royal flush":
    total += 4
    # "from straight flush":
    total += 40
    # "from 4OAK":  # -- stands for 4 Of A Kind
    total += combination(4, 4) * 13 * 48
    # "from full house":
    total += 12 * 13 * combination(4, 2) * combination(4, 3)
    # "from flush":
    total += (4 * combination(13, 5) - 40)
    # "from straight":
    total += (10 * 4 ** 5 - 40)
    # "from 3OAK":
    total += (13 * combination(4, 3) * (48 * 44) / 2)
    # "from two pair":
    total += (combination(13, 2) * combination(4, 2) ** 2 * 44)
    # "from one pair":
    total += 13 * combination(4, 2) * (48 * 44 * 40) / 6
    return total

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
