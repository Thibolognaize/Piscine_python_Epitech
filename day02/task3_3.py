# Write a snippet of code that calculates the sum of the digits of 123434565.
# Use the same code to calculates the sum of the digits of 345567426, then 44490320097.
def somme(num):
    num = str(num)
    res = 0
    for char in num:
        res += int(char)
    return res


print(somme(123434565))
print(somme(345567426))
print(somme(44490320097))
