# Prompt the user for an integer:
# - if it's 42, display ”a” ;
# - if it's smaller or equal than 21, display ”b” ;
# - if it's even, display ”c” ;
# - if this integer divided by 2 is smaller than 21 (excluded), display ”d” ;
# - finally, if it's is odd and greater or equal than 45, display ”e” ;
# - in any other cases, display ”f”.
usr_int = int(input("A int please:\n"))

if usr_int == 42:
    print("a")
elif usr_int <= 21:
    print("b")
elif usr_int % 2 != 0:
    print("c")
elif usr_int / 2 < 21:
    print("d")
elif usr_int % 2 == 0 and usr_int >= 45:
    print("e")
else:
    print("f")
