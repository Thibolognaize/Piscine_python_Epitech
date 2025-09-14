# Create a list of 5 numbers. Then, print the result of the multiplication of all its elements.
my_list = [x for x in range(1, 5 + 1)]
print(my_list)  # [1, 2, 3, 4, 5]
multiply = 1
for elt in my_list:
    multiply *= elt
print(multiply)
