# Display your entire list.
# Then, display each element of your list one by one
my_list = [x for x in range(1, 6)]
my_list.append(42)
for elt in my_list:
    print(elt)
