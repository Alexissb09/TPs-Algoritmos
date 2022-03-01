from cola import Cola

cola = Cola()
colaux = Cola()

PJSW =[
		['Chewbacca', 'Anoat'],
		['Obi-Wan Kenobi', 'Tatooine'],
		['Yoda','Endor'],
		['BB8', 'Alderaan'],
		['Padme Amidala','Atollon'],
		['Luke Skywalker', 'Tatooine'],   
		['Han Solo','Corellia'],
		['Jar Jar Binks', 'Anoat']
		]

planetas = ['Tatooine', 'Alderaan', 'Endor']

for i in range(0, len(PJSW)):
	cola.arribo(PJSW[i])

def pj_planetas():
	print('Personajes que habitan en Tatooine, Alderaan o Endor')
	for i in range(0, cola.tamanio()):
		x = cola.atencion()
		if x[1] in planetas:
			print(x[0],'en',x[1])
		cola.arribo(x)


def planeta_natal(): # Indica planeta natal de Luke y Han
	for i in range(0, cola.tamanio()):
		x = cola.atencion()
		if x[0] == 'Luke Skywalker' or x[0] == 'Han Solo':
			print('El planeta natal de', x[0],'es', x[1])	
		cola.arribo(x)

def insertar_detras_yoda():
	for i in range(0, cola.tamanio()):
		x = cola.atencion()
		if x[0] == 'Yoda': # Luego de Yoda arriba un PJ nuevo
			cola.arribo(['PJ Nuevo', 'Planeta de PJ'])

		cola.arribo(x)

def borrar_pj(): # Borra PJ despues de Jar Jar
	cont = 1
	for i in range(0, cola.tamanio()):
		x = cola.atencion()
		if x[0] != 'Jar Jar Binks':
			cont += 1
			cola.arribo(x)
		elif x[0] == 'Jar Jar Binks':
			colaux.arribo(x)
	for i in range(1, cont-1):
		x = cola.atencion()
		if i == cont:
			colaux.arribo(x)
		else:
			cola.arribo(x)

pj_planetas()
print('---')
planeta_natal()
insertar_detras_yoda()
borrar_pj()

print('--------------')

for i in range(0, cola.tamanio()):
	x = cola.atencion()
	print(x)