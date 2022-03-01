from heap import HeapMax
# Prioridades
empleado = 1
staff_ti = 2
gerente = 3

documentos = HeapMax()

doc_empleados = [
				['doc 1 empleado', empleado],
				['doc 2 empleado', empleado],
				['doc 3 empleado', empleado],
				]

doc_empleados2 = [
				['doc 4 empleado', empleado],
				['doc 5 empleado', empleado],
				]

doc_staff_ti = [
				['doc 6 staff ti', staff_ti],
				['doc 7 staff ti', staff_ti],
				]

doc_gerente = [
				['doc 8 gerente', gerente],
				]

doc_gerente2 = [
				['doc 9 gerente', gerente],
				]

documentos.arribo_muchos(doc_empleados) # Punto a

print(documentos.atencion()[1]) # Punto b

documentos.arribo_muchos(doc_staff_ti) # Punto c

documentos.arribo_muchos(doc_gerente) # Punto d

print()

for i in range(2): # Punto e
	print(documentos.atencion()[1])

documentos.arribo_muchos(doc_empleados2) # Punto f
documentos.arribo(doc_gerente2[0][0], doc_gerente2[0][1])

print()

while not documentos.vacio():
	print(documentos.atencion()[1])