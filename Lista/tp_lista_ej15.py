from lista import Lista

datosEntrenador = [
                    {'nombre': 'Ash', 'cantTorneosGanados' : 3, 'cantBatallasPerdidas': 30, 'cantBatallasGanadas': 180, 'pokemons': Lista()}, 
                    {'nombre': 'Serena', 'cantTorneosGanados' : 1, 'cantBatallasPerdidas': 64, 'cantBatallasGanadas': 300, 'pokemons': Lista()},
                    {'nombre': 'Misty', 'cantTorneosGanados' : 4, 'cantBatallasPerdidas': 33, 'cantBatallasGanadas': 50, 'pokemons': Lista()},
                    {'nombre': 'Brock', 'cantTorneosGanados' : 9, 'cantBatallasPerdidas': 150, 'cantBatallasGanadas': 20, 'pokemons': Lista()},
                    {'nombre': 'Clemo', 'cantTorneosGanados' : 0, 'cantBatallasPerdidas': 98, 'cantBatallasGanadas': 1, 'pokemons': Lista()},
                    ]

datosPokemnos1 = [{'nombre': 'Pikachu', 'nivel': 100, 'tipo' : 'Electrico', 'subtipo': 'ninguno'},
                 {'nombre': 'Raichu', 'nivel': 30, 'tipo' : 'Electrico', 'subtipo': 'Rayo'},
                 {'nombre': 'Pikachu', 'nivel': 100, 'tipo' : 'Electrico', 'subtipo': 'ninguno'},
                 {'nombre': 'Bulbasaur', 'nivel': 23, 'tipo' : 'Agua', 'subtipo': 'ninguno'},
                 {'nombre': 'Ivysaur', 'nivel': 12, 'tipo' : 'Fuego', 'subtipo': 'ninguno'},
                 ]

datosPokemnos2 = [{'nombre': 'Venusaur', 'nivel': 30, 'tipo' : 'Viento', 'subtipo': 'ninguno'},
                 {'nombre': 'Raichu', 'nivel': 50, 'tipo' : 'Electrico', 'subtipo': 'Rayo'},
                 {'nombre': 'Squirtle', 'nivel': 90, 'tipo' : 'Agua', 'subtipo': 'ninguno'},
                 ]

datosPokemnos3 = [{'nombre': 'Weedle', 'nivel': 90, 'tipo' : 'Yerba', 'subtipo': 'ninguno'},
                  {'nombre': 'Wigglytuff', 'nivel': 20, 'tipo' : 'Fuego', 'subtipo': 'Planta'},
                  {'nombre': 'Terrakion', 'nivel': 3, 'tipo' : 'Tierra', 'subtipo': 'Ninguno'},
                 ]

datosPokemnos4 = [{'nombre': 'Spearow', 'nivel': 12, 'tipo' : 'Magnetismo', 'subtipo': 'ninguno'},
                 {'nombre': 'Ekans', 'nivel': 30, 'tipo' : 'Hielo', 'subtipo': 'ninguno'},
                 {'nombre': 'Arbok', 'nivel': 2, 'tipo' : 'Hielo', 'subtipo': 'ninguno'},
                 {'nombre': 'Ivysaur', 'nivel': 1, 'tipo' : 'Fuego', 'subtipo': 'ninguno'},
                 ]

datosPokemnos5 = [{'nombre': 'Arbok', 'nivel': 100, 'tipo' : 'Hielo', 'subtipo': ''},
                 {'nombre': 'Nidoking', 'nivel': 100, 'tipo' : 'Ninguno', 'subtipo': 'ninguno'},
                 {'nombre': 'Arbok', 'nivel': 1, 'tipo' : 'Hielo', 'subtipo': ''},
                 ]

vector_pokemons = [datosPokemnos1, datosPokemnos2, datosPokemnos3, datosPokemnos4, datosPokemnos5]

lista = Lista()

for datosEntrenador in datosEntrenador:
    lista.insertar(datosEntrenador, 'nombre')

for i in range(0, len(vector_pokemons)):
    for pokemon in vector_pokemons[i]:
        lista.obtener_elemento(i)['pokemons'].insertar(pokemon, 'nombre')

def cant_pokemons_entrenador(nombre, lista): # Punto A
    pos = lista.busqueda(nombre, 'nombre')

    if pos != -1:
        return lista.obtener_elemento(pos)['pokemons'].tamanio()
    else:
        return 'El entrenador no se encuentra en la lista'

def entrenador_mas_torneos(lista): # Punto B
    for i in range(0, lista.tamanio()):
        if lista.obtener_elemento(i)['cantTorneosGanados'] > 3:
            print(lista.obtener_elemento(i)['nombre'])

def entrenador_mas_torneos_indice(lista): # Punto C
    indice = None
    cantTorneosGanados = 0

    for i in range(0, lista.tamanio()):
        if lista.obtener_elemento(i)['cantTorneosGanados'] > cantTorneosGanados:
            cantTorneosGanados = lista.obtener_elemento(i)['cantTorneosGanados']
            indice = i

    return indice

def pokemon_mayor_lvl(entrenador):
    pokemon = None
    lvlPokemon = 0

    for i in range(0, entrenador['pokemons'].tamanio()):
        if entrenador['pokemons'].obtener_elemento(i)['nivel'] > lvlPokemon:
            lvlPokemon = entrenador['pokemons'].obtener_elemento(i)['nivel']
            pokemon = entrenador['pokemons'].obtener_elemento(i)

        return pokemon

def mostrar_datos(entrenador): # Punto D
    print('Nombre: ', entrenador['nombre'], ', torneos ganados: ', entrenador['cantTorneosGanados'], ', batallas perdidas: ', entrenador['cantBatallasPerdidas'],
          ' , batallas ganadas: ', entrenador['cantBatallasGanadas'])

    print('Pokemones: ')
    for i in range(entrenador['pokemons'].tamanio()):
        print(entrenador['pokemons'].obtener_elemento(i))

def entrenadores_porcentaje_batallasGanadas(lista, porcentaje): # Punto E
    entrenador = None
    total = None

    for i in range(lista.tamanio()):
        entrenador = lista.obtener_elemento(i)
        total = entrenador['cantBatallasPerdidas'] + entrenador['cantBatallasGanadas']

        if entrenador['cantBatallasGanadas']*100/total > porcentaje:
            print(lista.obtener_elemento(i))

def entrenador_pokemon_tipo_subtipo(lista, tipo1, subtipo1, tipo2, subtipo2): # Punto F
    entrenador = None 
    pokemon = None 

    for i in range(0, lista.tamanio()):
        entrenador = lista.obtener_elemento(i)

        for i in range(0, entrenador['pokemons'].tamanio()):
            pokemon = entrenador['pokemons'].obtener_elemento(i)
            if ((pokemon['tipo'].lower() == tipo1.lower()) and (pokemon['subtipo'].lower() == subtipo1.lower())) or ((pokemon['tipo'].lower() == tipo2.lower()) and (pokemon['subtipo'].lower() == subtipo2.lower())):
                print(entrenador)
                break

def promedio_pokemones(lista): # Punto G
    sumalvl = 0

    for i in range(0, lista.tamanio()):
        entrenador = lista.obtener_elemento(i)

        for i in range(0, entrenador['pokemons'].tamanio()):
            sumalvl += entrenador['pokemons'].obtener_elemento(i)['nivel']

        print('El promedio de los pokemones del entrenador ', entrenador['nombre'], ' es de: ', sumalvl/entrenador['pokemons'].tamanio())

def entrenadores_por_pokemon(lista, pokemon): # Punto H
    cont = 0

    for i in range(lista.tamanio()):
        entrenador = lista.obtener_elemento(i)

        for i in range(0, entrenador['pokemons'].tamanio()):
            if entrenador['pokemons'].obtener_elemento(i)['nombre'].lower() == pokemon.lower():
                cont += 1
                break

    return 'El pokemon ', pokemon, ' lo tienen ', cont, ' entrenadores'

def entrenadores_pokemones_repetidos(lista): # Punto I
    cont = None 

    for i in range(0, lista.tamanio()):
        entrenador = lista.obtener_elemento(i)

        for i in range(0, entrenador['pokemons'].tamanio()):
            cont = 0

            for j in range(0, entrenador['pokemons'].tamanio()):
                if entrenador['pokemons'].obtener_elemento(i)['nombre'].lower() == entrenador['pokemons'].obtener_elemento(j)['nombre'].lower():
                    cont += 1

                    if cont > 1:
                        print(entrenador)
                        break

def entrenador_pokemon_conjunto(lista, conjunto): # Punto J
    cont = 0

    for i in range(0, lista.tamanio()):
        entrenador = lista.obtener_elemento(i)

        for i in range(0, entrenador['pokemons'].tamanio()):

            if entrenador['pokemons'].obtener_elemento(i)['nombre'] in conjunto:
                cont += 1
                break

    print ('Cantidad de entrenadores que tengan algun pokemon del conjunto ', conjunto, ' es de: ', cont)


def entrenador_tiene_pokemon(lista, nombre_entrenador, nombre_pokemon): # Punto K
    indice_entrenador = None
    indice_pokemon = None
    entrenador = None

    indice_entrenador = lista.busqueda(nombre_entrenador, 'nombre')

    if indice_entrenador > -1:
        indice_pokemon = lista.obtener_elemento(indice_entrenador)['pokemons'].busqueda(nombre_pokemon, 'nombre')

        if indice_pokemon > -1:
            entrenador = lista.obtener_elemento(indice_entrenador)
            pokemon = entrenador['pokemons'].obtener_elemento(indice_pokemon)
            print('El entrenador ', entrenador['nombre'], ' tiene al pokemon ', pokemon['nombre'])
            print('INFO')
            print('Nombre: ', entrenador['nombre'], ', torneos ganados: ', entrenador['cantTorneosGanados'], ', batallas perdidas: ', entrenador['cantBatallasPerdidas'], ', batallas ganadas: ', entrenador['cantBatallasGanadas'])
            print('Pokemon: ', pokemon['nombre'], ', nivel: ', pokemon['nivel'], ', tipo: ', pokemon['tipo'], ', subtipo: ', pokemon['subtipo'])
        else:
            print('El entrenador ', nombre_entrenador ,' no tiene a ', nombre_pokemon)
    else:
        print('El entrenador ', nombre_entrenador, ' no esta en la lista.')

# ===========================

print(cant_pokemons_entrenador('Ash', lista))
entrenador_mas_torneos(lista)

indice = entrenador_mas_torneos_indice(lista)
pokemon = pokemon_mayor_lvl(lista.obtener_elemento(indice))
print(pokemon)

mostrar_datos(lista.obtener_elemento(3))

entrenadores_porcentaje_batallasGanadas(lista, 79)

entrenador_pokemon_tipo_subtipo(lista, 'fuego', 'planta', 'agua', 'volador')

promedio_pokemones(lista)

print(entrenadores_por_pokemon(lista, 'Raichu'))
entrenadores_pokemones_repetidos(lista)

entrenador_pokemon_conjunto(lista, ('Tyrantrum', 'Terrakion', 'Wingull'))
entrenador_tiene_pokemon(lista, 'Ash', 'Raichu')