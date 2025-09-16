import os


# lister_fichiers_recursivement("./")
def lister_fichiers_recursivement(repertoire):
    list_directory = sorted(os.listdir(repertoire))
    # print(list_directory)
    for i in list_directory:
        print(i, end=" ")
        if os.path.isdir(i) == True and i[0] != ".":
            # Plonge d'un niveau
            lister_fichiers_recursivement(repertoire + "/" + i)
        else:
            # Remonte d'un niveau
            i = ""
    print("\n")


lister_fichiers_recursivement("./")
