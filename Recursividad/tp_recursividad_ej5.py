def calc_valor_letra(letra):

	if letra == 'M':
		valor = 1000

	elif letra == 'D':
		valor = 500

	elif letra == 'C':
		valor = 100

	elif letra == 'L':
		valor = 50

	elif letra == 'X':
		valor = 10

	elif letra == 'V':
		valor = 5

	elif letra == 'I':
		valor = 1

	return valor

def convertir(num_romano):

	val_letra = 0
	val_letra_aux = 0
	i = 2

	if len(num_romano) == 0:
		return val_letra
	else:
		val_letra = calc_valor_letra(num_romano[-1])

		if len(num_romano) > 1:
			val_letra_aux = calc_valor_letra(num_romano[-2])
		else:
			i = 1

		if val_letra > val_letra_aux:
			val_letra -= val_letra_aux
		else:
			val_letra += val_letra_aux

		return val_letra + convertir(num_romano[:-i])

print(convertir('XV'))