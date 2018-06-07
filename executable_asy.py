import os 
import sys
import fonctions

stock = open('stockvar.txt','r')
filename = stock.read()
fichier = open(filename,'a')

entree = input()

while 1: #Interaction avec l'utilisateur
	
#J'ai choisi une boucle avec des break car il était plus facile et rapide ainsi de gérer les sorties en cas d'erreur

	if entree =="quit":
		break
	if entree == '':
		print('Il manque des informations.')
		break
	mots = entree.split()
	try:
		functionname = mots[0]
	except:
		print('Il manque des informations.')
		break
	try:
		c1 = mots[1]
	except:
		print('Il manque des informations.')
		break
	try:
		c2 = mots[2]
	except:
		print('Il manque des informations.')
		break
	try:
		nom = mots[3] 
	except:
		print('Il manque des informations.')
		break
	try:
		direction = mots[4]
	except:
		print('Il manque des informations.')
		break
	if functionname == 'resistance':
		fonctions.resistance(fichier,c1,c2,nom,direction)
		break
	elif functionname == 'gtension':
		fonctions.gtension(fichier,c1,c2,nom,direction)
		break
	elif functionname == 'gcourant':
		fonctions.gcourant(fichier,c1,c2,nom,direction)
		break
	elif functionname == 'courant':
		fonctions.courant(fichier,c1,c2,nom,direction)
		break
	elif functionname == 'condo':
		fonctions.condo(fichier,c1,c2,nom,direction)
		break
	elif functionname == 'diode':
		fonctions.diode(fichier,c1,c2,direction)
		break
	elif functionname == 'interrupteurO':
		fonctions.interrupteurO(fichier,c1,c2,direction)
		break
	elif functionname == 'bobine':
		fonctions.bobine(fichier,c1,c2,direction)
		break
	else:
		print('La fonction n\'est pas reconnue. ')
		break
if entree == 'quit':
	fichier.close()
	fin = open('fin.txt','x')
	fin.close()