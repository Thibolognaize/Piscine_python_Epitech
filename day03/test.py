import string 

my_string = "Voici ma phrase..."
my_string = my_string.lower().replace(" ", "")
my_dict = dict()
for c in my_string:
    if c in string.punctuation:
        continue
    elif c not in my_dict:
        my_dict[c] = 1
    else:
        my_dict[c] = my_dict[c] + 1

print(my_dict)
# Etape 1 : Lire la string  => OK
# Etape 2 : stocker des les lettres en key et le nombre d'occurence en valeures => OK 
# Etape 3 : Si la lettre est dejà contenue cas => OK

