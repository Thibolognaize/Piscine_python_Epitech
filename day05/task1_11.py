# What does the following code do?
my_first_list = [4, 5, 6]
my_second_list = [1, 2, 3]
my_first_list.extend(my_second_list)

# Ce code ajoute la seconde list a la fin de la premiere (elle 'etend' la premiere liste)

my_first_list = [7, 8, 9]
my_second_list = [4, 5, 6]
my_first_list = [*my_first_list, *my_second_list]

print(my_first_list)

# L'opérateur précise de prendre tous les elements de la liste d'apres
