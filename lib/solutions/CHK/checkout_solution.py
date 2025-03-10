

# noinspection PyUnusedLocal
# skus = unicode string
from collections import Counter


lookup = {"A": 50, "B": 30, "C": 20, "D": 15}

def checkout(skus):

    counter = Counter(skus)

    for c in counter:
        if c not in lookup:
            return -1

    if not skus:
        return 0

    if len(skus) == 1:
        return lookup[skus[0]] if skus[0] in lookup else -1

    offer = {"A": (3, 130), "B": (2, 45)}



    total_cost = 0
    for item, count in counter.items():

        if item in offer:
            offer_cnt, offer_price = offer[item]
            total_cost += (count // offer_cnt) * offer_price
            total_cost += (count % offer_cnt) * lookup[item]
        else:
            total_cost += (count * lookup[item]) if item in lookup else 0

    return total_cost



