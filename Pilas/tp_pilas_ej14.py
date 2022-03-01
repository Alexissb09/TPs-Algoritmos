from pila import Pila
from random import randint

pila = Pila()
pilaux = Pila()

for i in range(0,5):
	num = randint(0,10)

	if not pila.pila_vacia():
		if num >= pila.elemento_cima():
			pila.apilar(num)
		else:
			while not pila.pila_vacia() and num < pila.elemento_cima():
				x = pila.desapilar()
				pilaux.apilar(x)

			pila.apilar(num)

			while not pilaux.pila_vacia():
				pila.apilar(pilaux.desapilar())

	else:

		pila.apilar(num)

while not pila.pila_vacia():
	print(pila.desapilar())