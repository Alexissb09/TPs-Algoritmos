from lista import Lista

lista = Lista()
lista2 = Lista()

datos = [
            {'name': 'Alexis', 'anio': 2000, 'id' : '01'},
            {'name': 'Facundo', 'anio': 1999, 'id' : '02'},
            {'name': 'Alejandro', 'anio': 2000, 'id' : '03'},
            {'name': 'Angela', 'anio': 2008, 'id' : '04'},
            {'name': 'Marcelo', 'anio': 1978, 'id' : '05'},
            ]
    
datos2 = [
            {'name': 'Gonzalo', 'anio': 2000, 'id' : '01'},
            {'name': 'Fabiana', 'anio': 2004, 'id' : '02'},
            {'name': 'Susana', 'anio': 2001, 'id' : '03'},
            {'name': 'Angela', 'anio': 2008, 'id' : '04'},
            {'name': 'Marcelo', 'anio': 1950, 'id' : '09'},
            {'name': 'Alejandro', 'anio': 2000, 'id' : '03'},
            ]

for dato in datos:
	lista.insertar(dato, 'name')

for dato in datos2:
	lista.insertar(dato, 'name')

def concatenar(lista, lista2):
	for i in range(0, lista2.tamanio()):
		lista.insertar(lista2.obtener_elemento(i), 'name')

def concatenar_sin_repetir(lista, lista2):
	diferente = False
	tamanio = lista.tamanio()
	for i in range(0, lista2.tamanio()):
		for j in range(0, lista.tamanio()):
			if lista2.obtener_elemento(i) != lista.obtener_elemento(j):
				diferente = True
			else:
				diferente = False

		if diferente:
			tamanio += 1
			lista.insertar(lista.obtener_elemento(i), 'name')


def repetidos(lista, lista2):
	cont_repetidos = 0
	diferente = False
	for i in range(0, lista2.tamanio()):
		for j in range(0, lista.tamanio()):
			if lista2.obtener_elemento(i) != lista.obtener_elemento(j):
				diferente = True
			else:
				diferente = False
				break

		if not diferente:
			cont_repetidos += 1

	return cont_repetidos

def eliminar_nodos(lista):
	while not lista.lista_vacia():
		print(lista.eliminar(lista.obtener_elemento(0)['name'], 'name')


concatenar(lista, lista2)
concatenar_sin_repetir(lista, lista2)
repetidos(lista, lista2)
eliminar_nodos(lista)