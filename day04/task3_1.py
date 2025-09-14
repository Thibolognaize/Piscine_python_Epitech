import string

# Prompt the user for a clear message and a key. Then, use Caesar cipher to encrypt the clear message with
# the key. Finally, print the encrypted message.


def encode_caesar_cipher():
    user_str = input("Give a string to encode:\n")
    encryption_key = int(input("Give a key between 1 and 25:\n"))
    alphabet_list = list(string.ascii_lowercase)
    encoded_str = ""
    for char in user_str.lower():
        if char in alphabet_list:
            char_value = alphabet_list.index(char)
            if char_value + encryption_key > 25:
                encoded_str += alphabet_list[(char_value - 26) + encryption_key]
            else:
                encoded_str += alphabet_list[char_value + encryption_key]
        else:
            encoded_str += char

    print(f"Your original string: {user_str}")
    print(f"Your encoded string: {encoded_str} with a key of {encryption_key}")


encode_caesar_cipher()
