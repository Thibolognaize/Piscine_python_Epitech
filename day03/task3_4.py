user_input = input("Write a string:\n")
words = user_input.split()
final_str = ""
for word in words:
    final_str += word[0]

print(final_str)
