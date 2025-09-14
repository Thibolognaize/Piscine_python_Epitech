# Prompt the user for an integer. Then, if it is:
# - odd, display ”This integer is odd” ;
# - even, display ”This integer is even”.
usr_numb = int(input("Enter an Int:\n"))
if usr_numb % 2 == 0:
    print("This integer is odd")
else:
    print("This integer is even")
