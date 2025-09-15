def bread():
    print(" <////////// > ")


def lettuce():
    print(" ~~~~~~~~~~~~ ")


def tomato():
    print("O O O O O O")


def ham():
    print(" =========== ")


def make_sandwiches(nb):
    if not isinstance(nb, int) or nb < 0:
        print("I can't do this!")
    else:
        for i in range(1, nb + 1):
            bread()
            ham()
            lettuce()
            ham()
            bread()
            print("\n")


make_sandwiches(1.2)
