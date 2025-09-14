# Let's consider a list of names (the ambassador's banquet guests).
# Write a program that displays:
# ”welcome in” if a given name belongs to this list ;
# and ”get lost!” otherwise.
name_list = list(("Thibault", "Thalia", "Noya"))
name = input("Give me your name: \n")
if name in name_list:
    print("Welcome in")
else:
    print("Get lost")
