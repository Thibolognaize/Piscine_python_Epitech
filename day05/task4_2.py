# Write a program that deletes all the duplicated elements in a list.
# Test it with [1, 1, 2, 2, 3] and with ['a', 2, 'a', 2, 'A'], they should return 3 elements.
my_list = list((1, 1, 2, 2, 3, 3))
my_list2 = ["a", 2, "a", 2, "A"]
print(list(set(my_list)))
print(list(set(my_list2)))
