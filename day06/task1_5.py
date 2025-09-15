# Add a parameter to provide the possibility for veg sandwich (double vegetables + no ham).
# If this option isn't specified, the sandwich must be a lettuce-tomato-double ham one by default.
def bread():
    print(" <////////// > ")


def lettuce():
    print(" ~~~~~~~~~~~~ ")


def tomato():
    print("O O O O O O")


def ham():
    print(" =========== ")


def make_sandwiches(nb, veggie=False):
    if isinstance(nb, int) != True or nb < 0:
        print("I can't do this!")
    else:
        if veggie != True:
            for i in range(1, nb + 1):
                bread()
                ham()
                lettuce()
                ham()
                bread()
                print("\n")
        else:
            for i in range(1, nb + 1):
                bread()
                lettuce()
                lettuce()
                bread()
                print("\n")


make_sandwiches(2)
