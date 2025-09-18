# Ask the user his/her name and then greet him/her with ”Hello <Username>!”.
# Careful, only the first letter is capitalized, such as ”Hello Archibald!”.
username = input("What's your username?\n")
answer = "Hello " + username.capitalize()
print(answer)
