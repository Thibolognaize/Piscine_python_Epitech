p = "abcdefghij"
print (p [:: -2][:5][:: -1][3:])

# Premier [] : extrait de 2 en 2 a partir de la fin 
# return => "jhfdb"
# Second [] : prends les 5 premiers car.
# return => "jhfdb"
# Troisieme [] : renvoie la string inversée
# return => "bdfhj "
# Quatrieme []: skip les 3 premiers car.
# return => "hj"