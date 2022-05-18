import math


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


print(combination(52, 5))

print("%.8f" % probability("royal flush"))
print("%.8f" % probability("straight flush"))
print("%.8f" % probability("4OAK"))
print("%.8f" % probability("full house"))
print("%.8f" % probability("flush"))
print("%.8f" % probability("straight"))
print("%.8f" % probability("3OAK"))
print("%.8f" % probability("two pair"))
print("%.8f" % probability("one pair"))
print("%.8f" % probability("high card"))
