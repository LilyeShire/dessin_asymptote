import os 
import sys
import fonctions

filename = input()
filename_a = filename + ".asy"
filename_c = filename + '.bat'
fichier = open(filename_a,'a')
fichier.write("unitsize(1cm);")
stock = open('stockvar.txt','x')
compil = open('compilator.bat','x')
chaine = 'asy -f pdf ' + filename
compil.write(chaine)
compil.write('\ndel texput.aux')
compil.write('\ndel texput.log')
compil.close()
chaine = 'ren compilator.bat ' + filename_c
renommer = open('renommer.bat','x')
renommer.write(chaine)
chaine = '\nmd ' + filename
renommer.write(chaine)
chaine = '\nmove ' + filename + '.bat ' + filename
renommer.write(chaine)
chaine = '\nmove ' + filename + '.asy ' + filename
renommer.write(chaine)
chaine = '\nmove ' + filename + '.pdf ' + filename
renommer.write(chaine)
renommer.close() 
stock.write(filename_a)
stock.close()


print('Entrez les coordonnées du circuit :')
entree = input().split()
longueur = entree[0]
largeur = entree[1]
if longueur == '0' and largeur == '0':
	pass
else:
	fonctions.contour(fichier,longueur,largeur)
	print('Voulez-vous ajouter des mailles ? (O : oui, N : non)')
	rep = input()
	while rep !='O' and rep !='N':
		print('Entrez O ou N.')
		rep = input()
	if rep == 'O':
		print('Quel est le nombre de mailles ?')
		nbMailles = int(input())
		for i in range(nbMailles):
			entree = input().split()
			if entree[0] == 'h':
				fonctions.hligne(fichier,entree[1],longueur)
			else:
				fonctions.vligne(fichier,entree[1],largeur)
	elif rep == 'N':
		pass
print('Quel(s) élément(s) ajouter au circuit ?')