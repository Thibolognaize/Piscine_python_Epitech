# Calculate the first 6 decimals of Pi using :
# Pi = 4 * (1/1 - 1/3 + 1/5 - 1/7...)

nums = []
somme = 0
for i in range(10000000):
    if i % 2 == 1:
        nums.append(i)
        length = len(nums)
        if length % 2 == 0:
            nums[-1] = i * (-(1**i))
        somme += 1 / (nums[-1])
print(round(4 * somme, 6))
