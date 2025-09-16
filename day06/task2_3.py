# Write a program that lists all the files and directories in the current directories, as well as all files and
# directories in its sub-directories and so on.
import os

# def get_files_dirs(path='./'):

# Retourne le path :
path = "./"
mypath = os.path.abspath("./")
print(mypath)
# List fichiers et directories
# print(os.listdir("./"))

# # list files:
files = [f for f in os.listdir() if os.path.isfile(f)]
# # List dirs:
dir = [f for f in os.listdir() if os.path.isdir(f)]
dir.sort()
# print(dir)
nb_dir = len(dir)
print(f"Full path selected: {mypath}")
print(f"Directory to explore: {nb_dir}\nList of directories: {dir}")
# Debut de la recursive
mypath = os.path.abspath("./")

# def list_dir(path):


for d in dir:
    path += d
    sub = os.listdir(path)
    print(sub)
    break
    for d2 in sub:
        print(f"Entered in {os.path.abspath(path)}")
        # files_found = [f for f in os.listdir() if os.path.isfile(f)]
        # dir_found = [f for f in os.listdir() if os.path.isdir(f)]
        # if len(files_found) > 0:
        #     print(f"Files found: {files_found}")
        # else:
        #     print(f"No files found")
        # if len(dir_found) > 0:
        #     print(f"Direcories found: {dir_found}")
        # else:
        #     print(f"No dir found")

        if os.path.isdir(d2) == True:
            path += d2
            sub2 = os.listdir(path)
            print(sub2)
        else:
            break
    print(f"Explorated path: {path}")
    path = path.replace(d, "")

# Ce code permet de renvoyer et de boucler sur tous les directories contenu dans le path
# Amelioration :
# Trier la liste {dir}, pour renvoyer de maniere ordonée les dirs / fichiers
# Utiliser une fonction recursive plutôt qu'une boucle
