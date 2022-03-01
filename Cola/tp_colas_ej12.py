from cola import Cola

cola = Cola()
cola2 = Cola()
colacombinada = Cola()

cola_num_1 = [1,2,3,4,5,6,7,8,9,10]
cola_num_2 = [1,5,7,10,15,16,19,20]

for i in range(1, len(cola_num_1)):
	cola.arribo(cola_num_1[i])

for i in range(1, len(cola_num_2)):
	cola.arribo(cola_num_2[i])

mov = 0

for i in range(0,cola.tamanio()):
	colacombinada.arribo(cola.mover_final())

for i in range(0,cola2.tamanio()):
	colacombinada.arribo(cola2.mover_final())

	while cola2.en_frente() > colacombinada.en_frente():
		colacombinada.mover_final()
		mov +=1 # cantidad de movimientos

	colacombinada.arribo(cola2.mover_final())

	for i in range(0, colacombinada.tamanio()-mov):
		colacombinada.mover_final()

while not colacombinada.cola_vacia():
	print(colacombinada.atencion())