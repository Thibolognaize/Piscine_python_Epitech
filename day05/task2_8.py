first_names = [" Jackie ", " Chuck ", " Arnold ", " Sylvester "]
last_names = [" Stallone ", " Schwarzenegger ", " Norris ", " Chan "]
magic = [*zip(first_names, last_names[::-1])]
print(magic[0])
print(magic[3])
print(magic[1][0])
print(magic[0][1])
print(magic[2])
# La var magic:
# 1: Unpack les elements des listes
# 2: concat avec zip les elements en un seul obj tuple
# 3: [::-1] inverse la liste last_names
# Ce code crée une liste avec prenom / nom a chaque iteration de tuples
