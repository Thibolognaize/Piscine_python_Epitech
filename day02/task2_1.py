# Compute the value of 1 + 11 + 111 + ... + 111111111.
# Then, computes this result power 2, power 3, power 4 and power 5.
somme = 0
dig = 0
for i in range(1, 9 + 1):
    dig = dig * 10 + 1
    somme = somme + dig
print(somme)

print(somme**2)
print(somme**3)
print(somme**4)
print(somme**5)
