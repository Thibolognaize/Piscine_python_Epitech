# Add the ten integers from 11 to 21 at the end of your list.
my_list = [x for x in range(1, 6)]
for i in range(11, 21 + 1):
    my_list.append(i)
print(my_list)
