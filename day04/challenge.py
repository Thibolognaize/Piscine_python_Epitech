user_str, user_int = input("Enter a string AND an int:\n").split()
if int(user_int) == 0:
    exit()
# Permet de vérifier si au moins un des caractères (any) du set de voyelles correspond a un caractère 'c' de ma string
elif any(c in {"a", "e", "i", "o", "u", "y"} for c in user_str.lower()):
    print(user_int)
elif int(user_int) >= 42:
    print(user_int)
else:
    print(user_str)
