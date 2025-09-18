# Write a snippet of code that counts the total of occurrences of the strings ”cat”, ”garden” and ”mice” in
# any string, considering that:
# each substring can be read left to right OR right to left ;
# matches must be case insensitive ;
# you should not bother with overlaps.
def count_words(str_input):
    words = ["cat", "garden", "mice"]  # Mots à trouver dans la chaine
    final_str = str_input.lower().replace(
        " ", ""
    )  # String nettoyé : sans espace + sans majs
    reversed_str = final_str[::-1]  # Inverse la string finale

    final_result = 0  # Intialisation du compteur d'occurence à 0
    # Boucle sur les mots à chercher
    for word in words:
        final_result += final_str.count(word) + reversed_str.count(
            word
        )  # Ajout des counts au résultat final

    return f"Nombre d'occurence des mots {words} dans la phrase '{str_input}' : {final_result}"


print(count_words("the CataCat attaCk a Cat"))
print(count_words("thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"))
