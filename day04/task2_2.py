# Prompt the user for a string.
# Display all the characters of this string twice.
usr_str = input("Give me a string !\n")
new_str = ""
for c in usr_str:
    new_str += c * 2

print(new_str)
