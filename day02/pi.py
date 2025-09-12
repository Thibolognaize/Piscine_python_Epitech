nums = []
somme = 0
for i in range (10000000):
    if (i % 2 == 1):
        nums.append(i)
        length = len(nums)
        if length % 2 == 0:
            nums[-1] = i*(-1**i)
        somme += 1/(nums[-1])
print(4*somme)




