from arboles import Arbol

arbol = Arbol()
arbolvillanos = Arbol()
arbolheroes = Arbol()

personajesMCU = [
                        {'name': 'Doctor Strnger', 'esHeroe': True},
                        {'name': 'Caballero Negro', 'esHeroe': True},
                        {'name': 'Iron man', 'esHeroe': True},
                        {'name': 'Doctor Muerte', 'esHeroe': False},
                        {'name': 'Doctor Octopus', 'esHeroe': False},
                        {'name': 'Calavera', 'esHeroe': True},
                        {'name': 'Thanos', 'esHeroe': False},
                        {'name': 'Spider man', 'esHeroe': True}
                    ]

arbol = arbol.cargar_arbol(personajesMCU, 'name')

def villanos_orden(arbol): # Printea villanos ordenados alfabeticamente
    if arbol.info is not None:
        if arbol.datos['esHeroe'] == False:
            print(arbol.info)
        if arbol.izq is not None:
            villanos_orden(arbol.izq)
        if arbol.der is not None:
            villanos_orden(arbol.der)

def heroesPorLetra(arbol, letra): # Muestra los heroes cuya inicial es la letra indicada 
    if arbol.info is not None:
        if arbol.datos['name'][0] == letra:
            print(arbol.info)
        if arbol.izq is not None:
            heroesPorLetra(arbol.izq, letra)
        if arbol.der is not None:
            heroesPorLetra(arbol.der, letra)    

def cantheroes(arbol): # Muestra la cantidad de Heroes en el arbol
    cont = 0
    if arbol.info is not None:
        if arbol.datos['esHeroe'] == True:
            cont += 1
        if arbol.izq is not None:
            cont += cantheroes(arbol.izq)        
        if arbol.der is not None:
            cont += cantheroes(arbol.der)

    return cont

def cambiarNombre(arbol, aprox, buscado): # Realiza busqueda por proximidad y cambia el nombre del Heroe
    arbol.busqueda_proximidad(aprox) # Busqueda aprox del nombre
    pos = arbol.busqueda(buscado) # Asigno posicion del nombre buscado
    if pos is not None:
        print('Datos del heroe:', pos.datos)
        nuevo_nombre = input('Ingrese el nuevo nombre: ') # Se reemplaza el nombre
        pos.datos['name'] = nuevo_nombre
        print('Nuevos datos del heroe:',pos.datos)
    else:
        print(buscado,'no se encuentra en el arbol')

def heroes_descendente(arbol): # Printea heroes en orden descendente
    if arbol.info is not None:
        if arbol.datos['esHeroe'] == True:
            print(arbol.info)
        if arbol.izq is not None:
            heroes_descendente(arbol.izq)
        if arbol.der is not None:
            heroes_descendente(arbol.der)

def generar_bosque(arbol, arbolheroes, arbolvillanos, campo='name'):
    if arbol.datos is not None:
        if arbol.datos['esHeroe'] == True:
            arbolheroes = arbolheroes.insertar_nodo(arbol.info, arbol.datos)
        else:
            arbolvillanos = arbolvillanos.insertar_nodo(arbol.info, arbol.datos)
        if arbol.izq is not None:
            arbolheroes, arbolvillanos = generar_bosque(arbol.izq, arbolheroes, arbolvillanos, campo)
        if arbol.der is not None:
            arbolheroes, arbolvillanos = generar_bosque(arbol.der, arbolheroes, arbolvillanos, campo)

    return arbolheroes, arbolvillanos

arbolheroes, arbolvillanos = generar_bosque(arbol, arbolheroes, arbolvillanos)

def contar_nodos(arbol): # Cuenta los nodos de un arbol
    cont = 0
    if arbol.info is not None:
        cont += 1
        if arbol.izq is not None:
            cont += contar_nodos(arbol.izq)
        if arbol.der is not None:
            cont+= contar_nodos(arbol.der)

    return cont

print('Villanos ordenados alfabeticamente: ')
villanos_orden(arbol)
print('--------')
heroesPorLetra(arbol, input('Ingresa una letra para buscar heroes con esa inicial: '))
print('--------')
print('Cantidad de Heroes:',cantheroes(arbol)) 
print('--------')
cambiarNombre(arbol, 'Doctor', 'Doctor Strnger') # Le paso el arbol, un nombre aproximado y nombre a buscar
print('--------')
print('Heroes ordenados descendentemente: ')
heroes_descendente(arbol)
print('--------')
print('Arbol de heroes: ')
arbolheroes.inorden()
print('--------')
print('Arbol de villanos: ')
arbolvillanos.inorden()
print('--------')
print('Cantidad de nodos del arbol de heroes:',contar_nodos(arbolheroes))
print('Cantidad de nodos del arbol de villanos:',contar_nodos(arbolvillanos))