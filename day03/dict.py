import string

alphabet = string.ascii_lowercase

# d_alpha = {lettre: 0 for lettre in alphabet}
# print(d_alpha)

# Clée est forcément de type immuable
tableau = [i for i in range(10)]
print(tableau)
tableau[5:] = []
print(tableau)
# print(tableau[5:])
tab = ""
