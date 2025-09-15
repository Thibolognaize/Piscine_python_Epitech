import string

# Write a recursive function that prompt the user for a string of characters, strip out the spaces and punctu-
# ation signs, lowercase the string, then test if is a palindrome
user_str = input("give a string to check if it's a palindrome\n")


def check_palindrome(user_str=user_str):
    user_str.lower().replace(" ", "")
    punctuations = string.punctuation
    if punctuations in user_str:
        for punct in punctuations:
            user_str = user_str.replace(punct, "")

    palindrome = False
    normal_str = ""
    reversed_str = ""

    normal_str += user_str[0]
    reversed_str += user_str[-1]

    palindrome = user_str == reversed_str

    lenght = len(user_str)

    if lenght <= 2:
        return palindrome

    return check_palindrome(user_str[1:-1])


print(check_palindrome())
