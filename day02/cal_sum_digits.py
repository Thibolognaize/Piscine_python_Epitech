def somme(num):
    num = str(num)
    res = 0
    for char in num:
        res += int(char)
    return res


print(somme(123434565))
print(somme(345567426))
print(somme(44490320097))

# print("input a number")
# x = int(input())
# n = 0
# while x%10 != x:
#     n += x%10
#     x = x//10

# n += x
# print(n)

# ZESTEDESAVOIR