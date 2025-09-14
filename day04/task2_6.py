# Write a program that takes an integer n as input. Then, for each integer from 2 to n/2, display the list of its
# multiples strictly smaller than n, in descending order.
def div(n):
    lim = int(n / 2)
    for nb in range(2, lim + 1):
        for i in range(n - 1, 0, -1):
            if i % nb == 0:
                print(i, end=" ")
        print("")


div(14)
