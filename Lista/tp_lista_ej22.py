from lista import Lista

datosJedis = [
             {'nombre' : 'Bo Keevil', 'maestros' : [], 'coloresDeSablesUsados' : [], 'especie' : 'Humano'},
             {'nombre' : 'Ahsoka Tano', 'maestros' : [], 'coloresDeSablesUsados' : [], 'especie' : 'Togruta'},
             {'nombre' : 'kit Fisto', 'maestros' : [], 'coloresDeSablesUsados' : [], 'especie' : 'Nautolano'},
             {'nombre' : 'Boba Fett:', 'maestros' : [], 'coloresDeSablesUsados' : [], 'especie' : 'desconocida'},
             {'nombre' : 'Jinx', 'maestros' : [], 'coloresDeSablesUsados' : [], 'especie' : 'Twi´lek'},
             {'nombre' : 'Bossk', 'maestros' : [], 'coloresDeSablesUsados' : [], 'especie' : 'Humano'},
            ]

maestrosJedis = [['Mace Windu', 'Yoda'],
                 ['Luke Skywalker'],
                 ['Lucien Draay'],
                 ['Yoda', 'Qui-Gon jin'],
                 ['Luke Skywalker'],
                 ['Qui-Gon jin'],
                 ]

sablesUsados = [
                ['rojo', 'azul', 'verde'],
                ['violeta'],
                ['gris', 'blanco', 'violeta'],
                ['rosado'], ['amarillo'],
                ['azul'], ['verde'], ['morado'], ['marron'],
                ['blanco']
                ]

lista = Lista()

for datosJedis in datosJedis:
   
    lista.insertar(datosJedis, 'nombre')

for i in range (0, lista.tamanio()):
    
    lista.obtener_elemento(i)['coloresDeSablesUsados'] = sablesUsados[i]
    lista.obtener_elemento(i)['maestros'] = maestrosJedis[i]


def info_personajes(lista, personajes): # Punto B
   
    indice = None

    for i in range(0,  len(personajes)):
        indice = lista.busqueda(personajes[i], 'nombre')
        if indice > -1:
            print(lista.obtener_elemento(indice))
        else:
            print('El personaje ', personajes[i],' no esta')

def padawans_de_maestros(lista, maestros): # Punto C
 
    for i in range(0, lista.tamanio()):
        jedi = lista.obtener_elemento(i)

        for j in range(0, len(jedi['maestros'])):
            if jedi['maestros'][j] in maestros:
                print(jedi)

def jedis_segun_especie(lista, especies): # Punto D

    for i in range(0, lista.tamanio()):
        jedi = lista.obtener_elemento(i)

        if jedi['especie'] in especies:
            print(jedi)

def jedis_inicial(lista, letras): # Punto E

    for i in range(0, lista.tamanio()):
        jedi = lista.obtener_elemento(i)

        if jedi['nombre'][0].upper() in letras:
            print(jedi)

def jedis_sables_color_diferente(lista, cantidad): # Punto F

    for i in range(0, lista.tamanio()):
        jedi = lista.obtener_elemento(i)

        if len(jedi['coloresDeSablesUsados']) > cantidad:
            print(jedi)

def jedis_segun_sable(lista, color): # Punto G
    
    cantidad = 0

    for i in range(0, lista.tamanio()):
        jedi = lista.obtener_elemento(i)

        for j in range(0, len(jedi['coloresDeSablesUsados'])):
            if jedi['coloresDeSablesUsados'][j] in color:
                cantidad += 1

    if cantidad > 0:
        print('La cantidad de Jedis que usaron el sable color ', color, ' es de: ', cantidad)
    else:
        print('No hay Jedi que haya usado ese color')


def nombre_padawans_de_maestros(lista, maestros): # Punto H

    for i in range(0, lista.tamanio()):
        jedi = lista.obtener_elemento(i)

    for j in range(0, len(jedi['maestros'])):
        if jedi['maestros'] in maestros:
            print(jedi['nombre'])


lista.ordenar('especie')
lista.barrido()

lista.ordenar('nombre')
info_personajes(lista, ['Ahsoka Tano', 'kit Fisto'])

padawans_de_maestros(lista, ['Yoda', 'Luke Skywalker'])

jedis_segun_especie(lista, ['Humano', 'Twi´lek'])

jedis_inicial(lista, ['A', 'K'])

jedis_sables_color_diferente(lista, 1)

jedis_segun_sable(lista, ['amarillo', 'violeta'])

nombre_padawans_de_maestros(lista, ['Qui-Gon jin', 'Mace Windu'])