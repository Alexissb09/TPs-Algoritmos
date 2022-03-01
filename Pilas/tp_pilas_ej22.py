\from pila import Pila

pila_boba = Pila()
pila_din = Pila()
pilaux = Pila()

nave_boba = [['Alderaan', 3479.42, 'Almirante Ozzel'], 
			['Anoat', 2389.23, 'Kylo Ren'],
            ['Corellia', 20045.68,'Han Solo'],
			['Base Starkiller', 21354.00, 'Chewbacca'], 
			['Christophsis', 3221.30, 'C3PO']
			]
                          
nave_din = [['Cantonica', 347.42, 'Yoda'], 
			['Dagobah', 23809.23, 'Rey'],
			['Felucia', 49.00, 'R2-D2'],
			['Corellia', 20045.68,'Han Solo'],
			['Dantooine', 2134.00, 'Leia Organa'], 
			['Eadu', 920981.30, 'Obi-Wan Kenobi'],
			['Hoth',0.00,'Fallo']
			]

for i in range(0, len(nave_boba)):
	pila_boba.apilar(nave_boba[i])

for i in range(0, len(nave_din)):
	pila_din.apilar(nave_din[i])

def orden_mision(): # Muestra las misiones de cada PJ realizadas en orden
	print("Planetas Mision Boba: ")
	while not pila_boba.pila_vacia():
		x = pila_boba.desapilar()
		pilaux.apilar(x)
	while not pilaux.pila_vacia():
		x = pilaux.desapilar()
		print("- "+x[0])
		pila_boba.apilar(x)

	print()

	print("Planetas Mision Din")
	while not pila_din.pila_vacia():
		x = pila_din.desapilar()
		pilaux.apilar(x)
	while not pilaux.pila_vacia():
		x = pilaux.desapilar()
		print("- "+x[0])
		pila_din.apilar(x)


def mayor_fortuna(): # Suma lo recaudado y devuelve quien recaudo mas
	
	fortuna_boba = 0.0
	fortuna_din = 0.0

	while not pila_boba.pila_vacia(): # Sumatoria del dinero recaudado por BOBA
		x = pila_boba.desapilar()
		fortuna_boba += x[1]
		pilaux.apilar(x)

	while not pilaux.pila_vacia():
		x = pilaux.desapilar()
		pila_boba.apilar(x)

	while not pila_din.pila_vacia(): # Sumatoria del dinero recaudado por DIN
		x = pila_din.desapilar()
		fortuna_din += x[1]
		pilaux.apilar(x)
	while not pilaux.pila_vacia():
		x = pilaux.desapilar()
		pila_din.apilar(x)

	print("Fortuna de Boba: "+str(fortuna_boba)+" creditos galacticos")
	print("Fortuna de Din: "+str(fortuna_din)+" creditos galacticos")

	if (fortuna_boba > fortuna_din):
		print("Boba obtuvo mayor fortuna")
	else:
		print("Din obtuvo mayor fortuna")

def mision_captura_hansolo():
	cont = 0
	while not pila_boba.pila_vacia():
		x = pila_boba.desapilar()
		pilaux.apilar(x)
	while not pilaux.pila_vacia():
		x = pilaux.desapilar()
		cont += 1
		if x[2] == 'Han Solo':
			print('Boba Fett captura a Han Solo en la mision', cont) # Se hace en segundo While para contar desde abajo hacia arriba de la pila
		pila_boba.apilar(x)

def cantidad_capturados():
	cont_boba = 0
	cont_din = 0
	while not pila_boba.pila_vacia(): 
		x = pila_boba.desapilar()
		if x[2] != 'Fallo':
			cont_boba +=1
		pilaux.apilar(x)

	while not pilaux.pila_vacia():
		x = pilaux.desapilar()
		pila_boba.apilar(x)

	while not pila_din.pila_vacia(): 
		x = pila_din.desapilar()
		if x[2] != 'Fallo':
			cont_din +=1
		pilaux.apilar(x)
	while not pilaux.pila_vacia():
		x = pilaux.desapilar()
		pila_din.apilar(x)

	print("Cantidad de capturados por Boba:", cont_boba)
	print("Cantidad de capturados por Din:", cont_din)

orden_mision()
print("---")
mayor_fortuna()
print("---")
mision_captura_hansolo()
print("---")
cantidad_capturados()