def resistance(fichier, c1, c2, nom, direction):
	if direction == 'h':
		resistanceh(fichier,c1,c2,nom)
	elif direction == 'v':
		resistancev(fichier,c1,c2,nom)

def contour(fichier, lon, lar):
	fichier.write('\ndraw ((0,0)--({},0)--({},{})--(0,{})--cycle);'.format(lon,lon,lar,lar))

def hligne(fichier, c, lon):
	fichier.write('\ndraw ((0, {})--({}, {}));'.format(c,lon,c))

def vligne(fichier, c, lar):
	fichier.write('\ndraw (({}, 0)--({}, {}));'.format(c,c,lar))

def gtension(fichier, c1, c2, nom, direction):
	fichier.write("\ndraw (circle(({},{}),1/2));".format(c1,c2))
	if direction == 'h':
		fichier.write('\ndraw (Label("${}$",align = RightSide),({}-5/8,{}-1/2)--({}-5/8,{}+1/2),Arrow(10bp));'.format(nom,c1,c2,c1,c2))
	elif direction == 'b':
		fichier.write('\ndraw (Label("${}$",align = RightSide),({}-5/8,{}+1/2)--({}-5/8,{}-1/2),Arrow(10bp));'.format(nom,c1,c2,c1,c2))
	elif direction == 'd':
		fichier.write('\ndraw (Label("${}$",align = LeftSide),({}-1/2,{}+5/8)--({}+1/2,{}+5/8),Arrow);'.format(nom,c1,c2,c1,c2))
	elif direction == 'g':
		fichier.write('\ndraw (Label("${}$",align = LeftSide),({}+1/2,{}+5/8)--({}-1/2,{}+5/8),Arrow);'.format(nom,c1,c2,c1,c2))
	else:
		print('Erreur dans les informations, l\'action n\'a pas pu être effectuée.')

def gcourant(fichier, c1, c2, nom, direction):
	fichier.write('\nfilldraw(circle(({},{}),1/2),white,black);'.format(c1,c2))
	if direction == 'h' or direction == 'b':
		fichier.write('\ndraw (({}-1/2,{})--({}+1/2,{}));'.format(c1,c2,c1,c2))
		if direction == 'h':
			fichier.write('\ndraw (Label("${}$",EndPoint,align=E),({},{}+1/2)--({},{}+3/4),Arrow(10bp));'.format(nom,c1,c2,c1,c2))
		else:
			fichier.write('\ndraw (Label("${}$",EndPoint,align=E),({},{}-1/2)--({},{}-3/4),Arrow(10bp));'.format(nom,c1,c2,c1,c2))
	elif direction == 'g' or direction == 'd':
		fichier.write('\ndraw (({},{}-1/2)--({},{}+1/2));'.format(c1,c2,c1,c2))
		if direction == 'g':
			fichier.write('\ndraw (Label("${}$",EndPoint,align=E),({}-1/2,{})--({}-3/4,{}),Arrow(10bp));'.format(nom,c1,c2,c1,c2))
		else:
			fichier.write('\ndraw (Label("${}$",EndPoint,align=E),({}+1/2,{})--({}+3/4,{}),Arrow(10bp));'.format(nom,c1,c2,c1,c2))
	else:
		print('Erreur dans les informations, l\'action n\'a pas pu être effectuée.')

def courant(fichier, c1, c2, nom, direction):
	if direction == 'h':
		fichier.write('\ndraw ("${}$",({},{}-1/3)--({},{}),Arrow());'.format(nom,c1,c2,c1,c2))
	elif direction == 'b':
		fichier.write('\ndraw ("${}$",({},{}+1/3)--({},{}),Arrow());'.format(nom,c1,c2,c1,c2))
	elif direction == 'g':
		fichier.write('\ndraw ("${}$",({}+1/3,{})--({},{}),Arrow());'.format(nom,c1,c2,c1,c2))
	elif direction == 'd':
		fichier.write('\ndraw ("${}$",({}-1/3,{})--({},{}),Arrow());'.format(nom,c1,c2,c1,c2))
	else:
		print('Erreur dans les informations, l\'action n\'a pas pu être effectuée.')

def condo(fichier, c1, c2, nom, direction):
	if direction == 'h' or direction == 'b':
		fichier.write('\nfill (({}-1/2,{}+1/4)--({}+1/2,{}+1/4)--({}+1/2,{}-1/4)--({}-1/2,{}-1/4)--cycle,white);'.format(c1,c2,c1,c2,c1,c2,c1,c2))
		fichier.write('\ndraw (({}-1/2,{}+1/4)--({}+1/2,{}+1/4));'.format(c1,c2,c1,c2))
		fichier.write('\ndraw (({}+1/2,{}-1/4)--({}-1/2,{}-1/4));'.format(c1,c2,c1,c2))
		if direction == 'h':
			fichier.write('\ndraw ("${}$",({}-3/4,{}-1/2)--({}-3/4,{}+1/2),Arrow());'.format(nom,c1,c2,c1,c2))
		else:
			fichier.write('\ndraw ("${}$",({}-3/4,{}+1/2)--({}-3/4,{}-1/2),Arrow());'.format(nom,c1,c2,c1,c2))
	elif direction =='g' or direction == 'd':
		fichier.write('\nfill (({}-1/4,{}+1/2)--({}+1/4,{}+1/2)--({}+1/4,{}-1/2)--({}-1/4,{}-1/2)--cycle,white);'.format(c1,c2,c1,c2,c1,c2,c1,c2))
		fichier.write('\ndraw (({}-1/4,{}+1/2)--({}+1/4,{}+1/2));'.format(c1,c2,c1,c2))
		fichier.write('\ndraw (({}+1/4,{}-1/2)--({}-1/4,{}-1/2));'.format(c1,c2,c1,c2))
		if direction == 'd':
			fichier.write('\ndraw ("${}$",({}-1/2,{}+3/4)--({}+1/2,{}+3/4),Arrow());'.format(nom,c1,c2,c1,c2))
		else:
			fichier.write('\ndraw ("${}$",({}+1/2,{}+3/4)--({}-1/2,{}+3/4),Arrow());'.format(nom,c1,c2,c1,c2))
	else:
		print('Erreur dans les informations, l\'action n\'a pas pu être effectuée.')

def diode(fichier, c1, c2, direction):
	fichier.write('\npath diode = (({}-1/2,{}-1/4)--({}-1/2,{}+1/4)--({}+1/2,{})--cycle);'.format(c1,c2,c1,c2,c1,c2))
	if direction == 'd':
		fichier.write('\ndraw (diode);')
	elif direction == 'g':
		fichier.write('\ndraw (rotate(180,diode));')
	elif direction == 'h':
		fichier.write('\ndraw (rotate(90,diode));')
	elif direction == 'b':
		fichier.write('\ndraw (rotate(-90,diode));')
	else:
		print('Erreur dans les informations, l\'action n\'a pas pu être effectuée.')

def interrupteurO(fichier, c1, c2, direction):
	fichier.write('\npair pA = ({}-1/2,{}),pB = ({}+1/2,{}+1/4),pC = ({}+1/2,{});'.format(c1,c2,c1,c2,c1,c2))
	fichier.write('\npath l=pA--pB;')
	fichier.write('\npath d=pA--pC;')
	if direction == 'v':
		fichier.write('\ndraw (rotate(-90,l));')
		fichier.write('\ndraw (rotate(-90,d),white)')
	elif direction == 'h':
		fichier.write('\ndraw (l);')
		fichier.write('\ndraw (d,white);')
		fichier.write('\ndot (pA);')
	else:
		print('Erreur dans les informations, l\'action n\'a pas pu être effectuée.')

def bobine(fichier, c1, c2, direction):
	if direction == 'h' or direction == 'b':
		fichier.write('\npair A=({},{}+4/10),B=({},{}-1/2),C=({},{}+1/2);'.format(c1,c2,c1,c2,c1,c2))
		fichier.write('\npath demi=arc(A,1/10,270,90);')
		fichier.write('\ndraw (demi);')
		fichier.write('\ndraw (shift(0,-1/5)*demi);')
		fichier.write('\ndraw (shift(0,-2/5)*demi);')
		fichier.write('\ndraw (shift(0,-3/5)*demi);')
		fichier.write('\ndraw (shift(0,-4/5)*demi);')
		fichier.write('\ndraw (B--C,white);')
	elif direction == 'g' or direction == 'd':
		fichier.write('\npair A=({}-4/10,{}),B=({}-1/2,{}),C=({}+1/2,{});'.format(c1,c2,c1,c2,c1,c2))
		fichier.write('\npath demi=arc(A,1/10,0,180);')
		fichier.write('\ndraw (demi);')
		fichier.write('\ndraw (shif t(1/5,0)*demi);')
		fichier.write('\ndraw (shift(2/5,0)*demi);')
		fichier.write('\ndraw (shift(3/5,0)*demi);')
		fichier.write('\ndraw (shift(4/5,0)*demi);')
		fichier.write('\ndraw (B--C,white);')
	else:
		print('Erreur dans les informations, l\'action n\'a pas pu être effectuée.')
