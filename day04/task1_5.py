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