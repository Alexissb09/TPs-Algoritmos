from pila import Pila

pilaV = Pila()
pilaVII = Pila()
pilactores = Pila()
pilaux = Pila()

EP_V = ['Luke Skywalker', 'Han Solo', 'Darth Vader', 'Leia Organa',
		'Yoda', 'Capitán Needan', 'Almirante Ozzel', 'Lando Calrissian']

EP_VII = ['Kylo Ren', 'Rey', 'Han Solo', 'Luke Skywalker', 'C3PO',
		'Leia Organa', 'Chewbacca', '	Poe Dameron']

for i in range(0, len(EP_V)):
	pilaV.apilar(EP_V[i])

for i in range(0, len(EP_VII)):
	pilaVII.apilar(EP_VII[i])


while not pilaV.pila_vacia():
	x = pilaV.desapilar()
	while not pilaVII.pila_vacia():
		y = pilaVII.desapilar()

		if x == y:
			pilactores.apilar(x)
		else:
			pilaux.apilar(y)

	while not pilaux.pila_vacia():
		y = pilaux.desapilar()
		pilaVII.apilar(y)

print('Personajes en ambas peliculas: ')

while not pilactores.pila_vacia():
	z = pilactores.desapilar()
	print('- '+z)