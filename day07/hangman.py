import random
from english_words import get_english_words_set


def loose(int):
    if int >= 12:
        print("You loose")


def random_choice():
    items = set(i for i in range(1, 6 + 1))
    selected = random.choice(list(items))
    return selected


web2lowerset = get_english_words_set(["web2"], lower=True)
print(web2lowerset)
