from pila import Pila

pila = Pila()
pilaux = Pila()

MCU = [['Black Widow', 'Avengers Confidential', 'Iron Man: Rise of Technovore', 'Avengers: Infinity War'],
        ['Iron Man', 'Iron Man I', 'Iron Man II','Avengers Confidential', 'Iron Man: Rise of Technovore', 'The Invincible Iron Man', 'Avengers: Infinity War'],
        ['Hulk', 'Avengers Confidential', 'Hulk vs Thor', 'Avengers: Infinity War'],
        ['Hawkeye', 'Avengers Confidential'],
        ['Thor', 'Hulk vs Thor', 'Avengers: Infinity War'],
        ['Groot', 'Infinity War'],
        ['Rocket Raccoon', 'Infinity War']
        ]

for i in range(0,len(MCU)):
    pila.apilar(MCU[i])

def pos_pj(): # determina en que posicion estan Groot y Rocket Raccon
    cont = 0
    while not pila.pila_vacia():
        x = pila.desapilar()
        pilaux.apilar(x)

    while not pilaux.pila_vacia(): # devuelve los pj a su pila original
        cont += 1
        x = pilaux.desapilar()
        if x[0] == 'Rocket Raccoon':
            print('Rocket Raccon se encuentra en la posicion', cont)
        if x[0] == 'Groot':
            print('Groot se encuentra en la posicion', cont)
        pila.apilar(x)

def cantidad_peliculas(): # PJ en 5 o mas peliculas, indicando cuantas. AGREGADO PUNTO BLACK WIDOW 

    print('Personajes que se encuentran en 5 o mas peliculas: ')

    while not pila.pila_vacia():
        x = pila.desapilar()
        aux = len(x)-1
        if aux >= 5:
            print(x[0], '- peliculas:', aux)
        pilaux.apilar(x)
        if x[0] == 'Black Widow' and pila.pila_vacia(): # Para que se muestre al final de todos los PJ
            aux = len(x)-1
            print('--')
            print('Black Widow participo en', aux, 'peliculas')

    while not pilaux.pila_vacia():
        x = pilaux.desapilar()
        pila.apilar(x)


def iniciales_pj(): # Indica que PJs tienen nombres que empiecen con C, D y G
    while not pila.pila_vacia():
        x = pila.desapilar()
        if x[0][0] in ['C', 'D', 'G']:
            print(x[0])
        pilaux.apilar(x)

    while not pilaux.pila_vacia():
        x = pilaux.desapilar()
        pila.apilar(x)


pos_pj()
print('---')
cantidad_peliculas()
print('---')
iniciales_pj()