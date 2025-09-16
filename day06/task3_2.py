import task3_1

# Write a generic function to checks passwords : they must contain more than 16 characters, at least 3
# special character and 1 number.
# This function should be callable the following way:
fun1 = task3_1.funA
fun2 = task3_1.funB
fun3 = task3_1.funC


def passcheck(func, nbr, pwd):
    try:
        if func(pwd, nbr) != True:
            return "Password Not Strong Enough!"
        else:
            return "Password good enough!"
    except:
        print("An exception occurred")


print(passcheck(fun1, 16, "mysecretpassword"))
print(passcheck(fun2, 3, "mysecretpassword"))
print(passcheck(fun3, 1, "mysecretpassword"))
