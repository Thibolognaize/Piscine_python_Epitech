# Write a little program that computes the power function as fast as possible.
# How long does your program takes to compute 42^84? and 42^168?
# Compare your times and your code with your neighbors
import time

start = time.time()


def compute_power(nb, power):
    result = nb
    for i in range(1, power):
        result *= nb
    return result


# print(f"Resultat 1:\n{compute_power(42, 84)}\n")
# print(f"Resultat 2:\n{compute_power(42, 168)}\n")
# compute_power(42, 168)
# compute_power(42, 84)

print(f"Time taken: {time.time() - start}")
