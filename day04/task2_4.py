# For all integers from -30 to 30:
# 3 if it's a multiple of 3, display ”Fizz” ;
# 3 if it's a multiple of 5, display ”Buzz” ;
# 3 if it's a multiple of 3 and 5, display ”FizzBuzz” ;
# 3 if it does not meet any of the previous conditions, just print the integer itself.


for i in range(-30, 31):
    if i % 3 == 0:
        print("Fizz", end="")
    if i % 5 == 0:
        print(f"Buzz")
    else:
        print(f"{i}")
