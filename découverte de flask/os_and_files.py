import os

print("___Lire un fichier___")

# Lire un fichier

file_path = os.path.join(os.environ.get('HOME'),'Bureau', 'testtest') 
print(file_path)

print(os.path.exists(file_path))

# open permet d'ouvrir un fichier 
f = open(os.path.join(file_path + '/' + 'test.txt'), 'r') 

print("___Des méthodes___")

'''
r', 'w', 'a', 'r+' pour les autorisations de modification
read, write, append, read+ pour lire et écrire.
'''

# essayer de printer f nous montre l'item python qui encode test.txt et non le contenu de test.txt
print(f)

#f.name nous permet d'extraire le nom du fichier ouvert
print(f.name, f.mode)

# f.close est un élément obligatoire pour être sur de ne pas laisser 
# le fichier ouvert en arrière plan et créer des fuites de mémoires
f.close()

print("___Le manager de contexte___")

# manager de contexte pour éviter d'avoir à f.close(), 
'''
Après avoir fermer ce bloc de code, python ferme automatiquement le fichier, cependant, 
il est possible d'appeller la variable f en dehors du bloc de code et d'accéder 
quand même au fichier.
'''
with open(os.path.join(file_path + '/' + 'test.txt'), 'r') as f:
	f_content = f.read() # création d'une variable f_content dans le manager
	print(f_content) # d'autres méthodes comme head, tail

	'''
	f_content = f.readlines()
	print(f_content)

	Permet de n'imprimer que le début de chaques lignes et de faire une liste de toutes les lignes.

	f.realine() sans le s ne choppe que la première ligne, incrémente une variable de 1,
	 ou le numéro de ligne donné en paramètre.
	'''


'''
print(f.read()) # en dehors du manager de contexte créer erreur 
du au fait que nous ne sommes pas dans le manager de contexte

f.read(100) lit les 100 premiers caractères
'''

'''
Cette variation permet d'imprimer des grands documents lignes 
par lignes sans se soucier de soucies de mémoires

with open(os.path.join(file_path + '/' + 'test.txt'), 'r') as f:
	for line in f: 
	print(line, end='')
'''
'''print("___Lire un gros fichier___")

with open(os.path.join(file_path + '/' + 'test.txt'), 'r') as f:
	size_to_read = 1
	f_content = f.read(size_to_read)

	while len(f_content) > 0:
		print(f_content, end='*')
		f_content = f.read(size_to_read) # permet de sortir de la boucle while à la fin du fichier '''

# print(f.tell()) permet de savoir la position actuellement de la lecture d'un fichier
# f.seek(0) recherche la position dans le fichier (le début)

print("___Écrire dans un fichier___")
# Écrire dans un fichier

with open(os.path.join(file_path + '/' + 'test2.txt'), 'w') as f:  # bien mettre 'w' à la place de 'r', ou 'a' pour append
	f.write('test')
	print(os.listdir(file_path))

'''
utiliser juste pass aurait créer le fichier sans écrire dedans
'''

print("___Écrire et lire dans un fichier___")
# Écrire dans un fichier

with open(os.path.join(file_path + '/' + 'test.txt'), 'r') as rf:
	with open(os.path.join(file_path + '/' + 'test_copy.txt'), 'w') as wf:
		for line in rf:
			wf.write(line)
	with open(os.path.join(file_path + '/' + 'test_copy.txt'), 'r') as wrf:
		wrf_content = wrf.read()
		print(wrf_content)


	print(os.listdir(file_path))


'''print("___Écrire et lire dans un fichier qui n'est pas du texte___")

with open(os.path.join(file_path + '/' + 'img.jpg'), 'rb') as rf: # rb pour read bytes
	with open(os.path.join(file_path + '/' + 'image_copy.jpg'), 'wb') as wf: # wb pour write bytes
		for line in rf:
			wf.write(line)

'''





