# Write a program that lists all the files and directories in the current directories, as well as all files and
# directories in its sub-directories and so on.
import os

# def get_files_dirs(path='./'):

# Retourne le path :
path = "./"
mypath = os.path.abspath("./")
# print(mypath)
# List fichiers et directories
# print(os.listdir("./"))

# # list files:
# files = [f for f in os.listdir() if os.path.isfile(f)]
# print(files)
# # List dirs:
dir = [f for f in os.listdir() if os.path.isdir(f)]
# print(dir)

for d in dir:
    path += d
    sub1 = os.listdir(path)
    for d2 in sub1:
        if os.path.isdir(d2) == True:
            path += d2
            sub2 = os.listdir(path)
        else:
            break
