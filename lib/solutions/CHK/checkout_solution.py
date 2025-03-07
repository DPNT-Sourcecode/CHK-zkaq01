

# noinspection PyUnusedLocal
# skus = unicode string


# lookup = {"A": 50, "B": 30, "C": 20, "D": 15}
from collections import Counter

def checkout(skus):
    if not skus:
        return -1

    counter = Counter(skus)

    for item in counter.items():



    return skus

