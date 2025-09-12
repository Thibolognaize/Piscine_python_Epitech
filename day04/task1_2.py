# Ask an integer to the user. If it's equal to 42, display ”This is correct!”.

correct = False

while correct != True:
    usr_numb = int(input("Enter an Int:\n"))
    if usr_numb == 42:
        print("This is correct!")
        correct = True
    else:
        print("Try again...")
        correct = False