import string

# user_str = input("What message would you encrypt ?\n")
# encryption_key = int(input("Now, what's your key for the encryption ? [1 - 25]\n"))
user_str = "je m'appelle"
encryption_key = 24
alpha_list = list(string.ascii_lowercase)
# convertion de list à dict pour l'alphabet
alphabet = dict()
i = 0
for char in alpha_list:
    alphabet[char] = i
    i += 1

# On lower la string pour etre certain de ne pas avoir de prb
user_str = user_str.lower()
char_value = 0
final_str = ""
for char in user_str:
    if char in string.ascii_lowercase:
        # ici je transforme la lettre en chiffre (valeure du dict)
        char_value = int(alphabet.get(char))  # Recuperation de la valeure de la lettre
        if char_value - encryption_key < 0:
            char_value = (char_value + 25) - encryption_key
            final_str += str(alphabet.get(char_value))
        else:
            final_str = alphabet.get(str(char_value - encryption_key))
    elif char not in string.ascii_lowercase:
        final_str += char


print(final_str)

# Mtn j'ai l'alphabet avec des valeurs je peux comparer chaqu'une des valeures
# Pour gérer les espaces je vais utiliser split
# Il faudra aussi gérer la ponctuation ".'!?"... Mais on le fera apres


# def encrypt_msg(user_str, encryption_key):
#     msg_len = len(user_str)
#     encrypted_str = ""
#     for char in user_str:
#         char = ALPHABET[encryption_key + 1]
#         encrypted_str += char
#     print(f"Your encrypted message is:\n {encrypted_str}")


# encrypt_msg(user_str, encryption_key)

# A FAIRE : Gérer les espaces dans le message (passer sur une liste serait plus pratique ?)
