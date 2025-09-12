p = "abcdefghij"
print(f"String de départ: {p}")

slice1 = p[:: -2]
print(f"Premier slice: {slice1}")
slice2 = slice1[:5]
print(f"Second slice: {slice2}")
slice3 = slice2[:: -1]
print(f"Troisieme slice: {slice3}")
slice4 = slice3[3:]
print(f"Quatrieme slice: {slice4}")

# Premier [] : extrait de 2 en 2 a partir de la fin 
# return => "jhfdb"
# Second [] : prends les 5 premiers car.
# return => "jhfdb"
# Troisieme [] : renvoie la string inversée
# return => "bdfhj "
# Quatrieme []: skip les 3 premiers car.
# return => "hj"