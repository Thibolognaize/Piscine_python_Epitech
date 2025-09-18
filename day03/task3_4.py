# Write a program that:
# ask the user to type a string ;
# extracts the first letter of each word in the string ;
# join these letters to make a word.
user_input = input("Write a string:\n")
words = user_input.split()
final_str = ""
for word in words:
    final_str += word[0]

print(final_str)
