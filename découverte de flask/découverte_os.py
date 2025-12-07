import os

# Le module OS permet d'interagir avec le système d'exploitation.

# print(dir(os)) permet de voir toutes les méthodes de l'application
# print(dir(os.path))

# permet de connaître le dossier actuel
print(os.getcwd()) 

# permet de changer le dossier actuel
os.chdir('/home/lujes/Bureau')

print(os.getcwd())

print("________________")
# permet de connaitre l'arboresence de fichier et de dossier à partir du dossier actuel
print(os.listdir())

# Créer un nouveau dossier nommé test
os.makedirs('test') # mkdir ne fait pas de sous dossier
print(os.listdir())

"""
# détruire de nouveaux fichiers
os.removedirs('test') # détruit les dossiers récursivement, rmdir ne fait pas ça
print(os.listdir())
"""

print("________________")
# renomer un ficher ou un fichier

os.rename('test', 'testtest')
print(os.listdir())

# extraire des informations concernant un fichier ou un dossier

print(os.stat('testtest'))
print(os.stat('testtest').st_size) # la taille du document
print(os.stat('testtest').st_mtime) # la dernière date de modification 

print("________________")
# Passage de l'output st_mtime qui n'est pas lisible pour les humains en un 
# output lisible pour nous fait de chaire et d'os (blague sur os).
'''
from datetime import datetime

mod_time = os.stat('testtest').st_mtime
print(datetime.fromtimestamp(mod_time))
'''

# Pour imprimer un arbre, génère un tuple de 3 informations :
# le chemin, le nom du dossier et le nom des fichiers dans le dossier

'''
for dirpath, dirnames, filenames in os.walk("/home/lujes/poubelle/pythonflask/exo2/découverte de flask"):
	print('current path : ', dirpath)
	print('directories names : ', dirnames)
	print('files names : ', filenames)
'''

# accéder à des variables d'environnements, et joindre des chemins : 
'''
Cette commande permet de trouver la variable d'environnement home à coup sur 
et d'y joindre le fait de trouver le dossier testest sans se soucier de trouver 
la bonne syntaxe ou de se tromper dans le nombre de /
'''

file_path = os.path.join(os.environ.get('HOME'), 'testtest', 'test.txt') 
print(file_path)

# savoir si un chemin existe 
'''
Rend un booléen True si le chemin est valide
'''
print(os.path.exists(file_path))
print(os.path.isdir(file_path))
print(os.path.isfile(file_path))
print(os.path.splitext(file_path)) # permet de sortir l'extension et le nom d'un fichier
