# Write a program that can decrypt any Caesar-ciphered text.
import string


def decode_caesar_cipher():
    user_str = input("Give a string to decode:\n")
    encryption_key = int(input("Give the know key between 1 and 25:\n"))
    alphabet_list = list(string.ascii_lowercase)
    decoded_str = ""
    for char in user_str.lower():
        if char in alphabet_list:
            char_value = alphabet_list.index(char)
            if char_value - encryption_key < 0:
                decoded_str += alphabet_list[(char_value + 26) - encryption_key]
            else:
                decoded_str += alphabet_list[char_value - encryption_key]
        else:
            decoded_str += char

    print(f"Your original string: {user_str}")
    print(f"Your decoded string: {decoded_str}")


decode_caesar_cipher()
