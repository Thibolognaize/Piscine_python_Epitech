def div(x):
    lim = int(x / 2)
    for nb in range(2, lim + 1):
        for i in range(x - 1, 0, -1):
            if i % nb == 0:
                print(i, end=" ")
        print("")


div(14)


# Comment incrementer n jusqu'a n/2 ????????????

# Tour 1 : 14 / 2 | n = 14 lim =
