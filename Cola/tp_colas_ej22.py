from cola import Cola

cola = Cola()

PJMCU = [
		['Tony Stark', 'Iron Man', 'M'],
		['Thor Odinson', 'Thor', 'M'],
		['Carol Danvers','Capitana Marvel','F'],
		['Steve Rogers', 'Capitan America', 'M'],
		['Scott Lang', 'Hombre Hormiga', 'M'],
		['Stephen Strange', 'Doctor Strange', 'M'], 
		]

for i in range(0, len(PJMCU)):
	cola.arribo(PJMCU[i])

def nombre_pj(cola, personaje):
	nombre = None
	for i in range(0,cola.tamanio()):
		if cola.en_frente()[1] == personaje:
			nombre = cola.en_frente()[0] # Nombre del personaje

		cola.mover_final()

	return nombre

def heroinas(cola):
	v_heroinas = []
	for i in range(0,cola.tamanio()):
		if cola.en_frente()[2] == 'F':
			v_heroinas.append(cola.en_frente()[1])
		
		cola.mover_final()
			
	return v_heroinas

def heroes(cola):
	v_heroes = []
	for i in range(0,cola.tamanio()):
		if cola.en_frente()[2] == 'M':
			v_heroes.append(cola.en_frente()[1])
		
		cola.mover_final()
			
	return v_heroes

def nombre_heroe(cola, personaje):
	nombre = None
	for i in range(0,cola.tamanio()):
		if cola.en_frente()[0] == personaje:
			nombre = cola.en_frente()[1] # Nombre del Superheroe

		cola.mover_final()

	return nombre

def inicial(cola, letra):
	v_inicial = []
	for i in range(0,cola.tamanio()):
		if cola.en_frente()[0][0] == letra or cola.en_frente()[1][0] == letra:
			v_inicial.append([cola.en_frente()[0], cola.en_frente()[1]])
		
		cola.mover_final()
			
	return v_inicial

def buscar_pj(cola, personaje):
	bandera = False
	nombre = None 
	superheroe = None 
	for i in range(0, cola.tamanio()):
		if cola.en_frente()[0] == personaje:
			bandera == True
			nombre = cola.en_frente()[0]
			superheroe = cola.en_frente()[1]
			msj = nombre + ' se encuentra en la cola, su superheroe es ' + superheroe
			return msj

		cola.mover_final()

	if bandera != True:
		return 'No se encuentra el personaje indicado'


print('Nombre del personaje:',nombre_pj(cola, 'Capitana Marvel'))
print('Heroinas: ', heroinas(cola))
print('Heroes: ', heroes(cola))
print('Nombre del Superheroe:',nombre_heroe(cola, 'Scott Lang'))
print('Personajes con inicial S', inicial(cola, 'S'))
print(buscar_pj(cola, 'Carol Danvers'))