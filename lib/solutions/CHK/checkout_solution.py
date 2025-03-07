

# noinspection PyUnusedLocal
# skus = unicode string


lookup = {"A": 50, "B": 30, "C": 20, "D": 15}
from collections import Counter

def checkout(skus):
    if not skus:
        return -1

    counter = Counter(skus)
    cost = 0
    for item, value in counter:
        if item=="B" and value % 2 == 0:
            cost += (value // 2) * 45
        if item=="B" and value % 2 != 0 and value > 2:
            cost += (value % 2)



        if item=="A" and value % 3 == 0:
            cost += (value // 2) * 130



    return skus




