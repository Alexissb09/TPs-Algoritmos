from lista import Lista
from random import randint

superheroes = [
                        {'name' : "Iron Man",'anio' : 1963,'casa' : "Marvel",'biografia' : "Anthony Edward Stark conocido como Tony Stark, un multimillonario magnate empresarial estadounidense, playboy e ingenioso científico, quien sufrió una grave lesión en el pecho durante un secuestro. Cuando sus captores intentan forzarlo a construir un arma de destrucción masiva crea, en cambio, una armadura para salvar su vida y escapar del cautiverio."},
                        {'name' : "Linterna Verde",'anio' : 1940,'casa' : "DC",'biografia' : "Cada Linterna Verde posee un anillo de poder y una batería (en forma de linterna) que garantiza a su portador la posibilidad de manifestar una gran variedad de poderes."},
                        {'name' : "Hulk",'anio' : 1969,'casa' : "Marvel",'biografia' : "El Doctor Robert Bruce Banner es un científico de renombre y miembro fundador de los Vengadores. Él era un experto en la bioquímica, la física nuclear y la radiación gamma, por lo que el General Thaddeus Ross lo reclutó para recrear el Suero del Súper Soldado, pero esto resultó en un experimento fallido de radiación gamma, que convirtió a Banner en un monstruo verde llamado Hulk. Debido a lo peligroso que era, Banner abandonó a Elizabeth Ross para buscar una cura mientras era perseguido por Thaddeus Ross. Con el tiempo, Banner se reunió con Samuel Sterns y Elizabeth Ross para fabricar un antídoto, sin embargo, cuando Emil Blonsky se convirtió en la Abominación, Banner se vio forzado a utilizar a Hulk para vencerlo."},
                        {'name' : "Wolverine",'anio' : 1974,'casa' : "Marvel",'biografia' : "Wolverine, cuyo nombre de nacimiento es James Howlett (también conocido como James Logan o simplemente Logan)4​ es un superhéroe ficticio que aparece en los cómics estadounidenses publicado por Marvel Comics, principalmente en asociación con los X-Men. Es un mutante que posee sentidos afinados a los animales, capacidades físicas mejoradas, poderosa capacidad de regeneración conocida como un factor de curación, y tres garras retráctiles en cada mano. Wolverine ha sido representado de diversas formas como miembro de los X-Men, Alpha Flight, Fuerza-X y Los Vengadores."},
                        {'name' : "Dr.Strange",'anio' : 2016,'casa' : "DC",'biografia' : "El Doctor Stephen Strange, un neurocirujano muy reconocido, pierde el uso de sus manos en un terrible accidente de auto, quedando éstas aplastadas hasta el antebrazo. Strange sobrevive apenas. Su examante y compañera de trabajo Christine Palmer trata de ayudarlo a seguir adelante, pero en lugar de eso, el arrogante Strange quiere sanar rápidamente sus heridas."},
                        {'name' : "Capitana Marvel",'anio' : 1962,'casa' : "Marvel",'biografia' : "1995, en el planeta Hala, capital del Imperio Kree, la guerrera y miembro de la Fuerza Estelar Vers sufre de pesadillas recurrentes que involucran a una mujer mayor. Yon-Rogg, su mentor y comandante, le advierte mientras entrenan que controle sus habilidades, y a su vez la Inteligencia Suprema, una inteligencia artificial orgánica que actúa como gobernante Kree, la insta a mantener sus emociones bajo control."},
                        {'name' : "Mujer Maravilla",'anio' : 1941,'casa' : "DC",'biografia' : "El Traje de Mujer Maravilla ha variado con el tiempo, a pesar de que casi la totalidad de sus apariencias en sus encarnaciones han conservado una cierta forma de armadura, la tiara, los brazaletes y sus símbolos de estrella en su diseño.151​ Aunque el diseño de su traje se ha basado originalmente en el simbolismo de Estados Unidos y su iconografía, que permitió explicar más arraigada las raíces amazónicas. Durante una escena en retrospectiva en el volumen 3 de Wonder Woman,152​ Hipólita ordena la emisión de tener una prenda creada para Diana, que fue inspirada en el cielo nocturno en la noche en que Diana nació; una luna roja cazadora y en un campo de estrellas de azul profundo y el pectoral el águila, que es un símbolo de las representaciones antropomórficas de Atenea."},
                        {'name' : "Flash",'anio' : 1959,'casa' : "DC",'biografia' : "Bartholomew Henry Barry Allen es un científico asistente de la División de Ciencia Criminal y Forense del Departamento de Policía de Ciudad Central en 1956, conocido por ser lento y llegar siempre tarde a su trabajo, lo cual enojaba a su prometida Iris West. Una noche, le cayó un rayo , un rayo cayó en su laboratorio lleno de químicos que bañaron a Allen, creando un accidente que le otorgaría una súper velocidad e increíbles reflejos (también la capacidad de viajar en el tiempo y entre dimensiones). Con un traje rojo y el símbolo de un rayo (que recuerda al original Capitán Maravilla de Fawcett Comics), su novia lo nombró Flash, (ya que cuando era niño algo veloz mató a su madre y Barry dijo que fue como un flash) empezando así a combatir el crimen en Ciudad Central."},
                        {'name' : "Star-Lord",'anio' : 1976,'casa' : "Marvel",'biografia' : "supongamos que este tiene armadura, Cuando por accidente la nave de J'son cae en la Tierra, él es rescatado por Meredith Quill. Los dos forman una relación, mientras J'son hace reparaciones a su nave. Eventualmente, J'son se ve obligado a salir para regresar a casa y luchar en una guerra. Se va, sin saber que Meredith está embarazada de Peter Quill. 10 años más tarde, Meredith es asesinada cuando es atacada por dos soldados Badoon que han venido a matar a Peter y terminar la línea de sangre de J'son. Peter los mata con una pistola, encuentra la pistola de su padre por accidente, y escapa de su casa antes de que sea destruida por la nave Badoon. Los Badoon presumen que Peter es asesinado y se va. Peter es colocado en un orfanato y finalmente se une a la NASA. Finalmente se explicó que fue criado por su madre Lisa Chang, que era comandante de la NASA."},
                        ]

lista = Lista()

for datos in superheroes:
    lista.insertar(datos, 'name')

def eliminar_info(lista, nombre): # Elimina el pj indicado de la lista
    info = lista.eliminar(nombre, 'name')

    if info != None:
        return 'Personaje ' + nombre + ' eliminado de la lista'
    else:
        return 'El personaje no esta en la lista'

def aparicion(lista, nombre): # Indica anio de aparicion de personaje indicado
    pos = lista.busqueda(nombre, 'name')
    infopj = None

    if pos != -1:
        infopj = lista.obtener_elemento(pos)
        return 'Anio de aparicion de ' + infopj['name'] + ' es: ' + str(infopj['anio'])
    else:
        return 'El personaje no esta en la lista'

def cambiar_casa(lista, nombre, nuevacasa):
    pos = lista.busqueda(nombre, 'name')
    infopj = None 

    if pos != -1:
        infopj = lista.obtener_elemento(pos)

        infopj['casa'] = nuevacasa

        lista.modificar_elemento(pos, infopj, 'casa')

        return 'La casa de ' + infopj['name'] + ' ahora es ' + infopj['casa']

    else:
        return 'El personaje no esta en la lista'

def traje_biografia(lista): # Indica si traje o armadura esta en la biografia
    infopj = None
    for i in range(0, lista.tamanio()):
        infopj = lista.obtener_elemento(i)

        if infopj['biografia'].find('traje') != -1 or infopj['biografia'].find('armadura') != -1:
            print(infopj['name'])

def aparicion_1963(lista): # Indica los personajes que aparecen antes de esta fecha
    infopj = None
    for i in range(0, lista.tamanio()):
        infopj = lista.obtener_elemento(i)

        if infopj['anio'] < 1963:
            print(infopj['name'], '-', infopj['casa'])

def mostrar_casa(lista, nombre):
    infopj = None 
    pos = lista.busqueda(nombre, 'name')

    if pos != -1:
        infopj = lista.obtener_elemento(pos)
        return 'La casa de ' + infopj['name'] + ' es ' + infopj['casa']

def mostrar_info(lista, nombre):
    infopj = None 
    pos = lista.busqueda(nombre, 'name')

    if pos != -1:
        infopj = lista.obtener_elemento(pos)
        return 'Nombre: ' + infopj['name'] + '\nCasa: ' + infopj['casa'] + '\nAnio de aparicion: ' + str(infopj['anio']) + '\nBiografia: ' + infopj['biografia']

def superheroe_inicial(lista, inicial):
    infopj = None 
    hay = False
    for i in range(0,lista.tamanio()):
        infopj = lista.obtener_elemento(i)
        if infopj['name'][0] == inicial:
            print(infopj['name'])
            hay = True
    if not hay:
        print('No hay personajes que tengan esa inicial')

def cant_superheroes_casa(lista):
    infopj = None
    cont_marvel = 0
    cont_dc = 0 
    for i in range(0,lista.tamanio()):
        infopj = lista.obtener_elemento(i)
        if infopj['casa'] == 'Marvel':
            cont_marvel +=1
        if infopj['casa'] == 'DC':
            cont_dc +=1
    return 'Marvel: ' + str(cont_marvel) + ', DC: ' + str(cont_dc)
    
print('\nCantidad de superheroes en cada casa de comics:')
print(cant_superheroes_casa(lista))

print(eliminar_info(lista, 'Linterna Verde'))

print(aparicion(lista, 'Wolverine'))

print(cambiar_casa(lista, 'Dr.Strange', 'Marvel'))

print('\nPersonajes que contienen traje o armadura en su biografia:')
traje_biografia(lista)
print('\nPersonajes que aparecieron antes de 1963:')
aparicion_1963(lista)
print()
print(mostrar_casa(lista, 'Capitana Marvel'))
print(mostrar_casa(lista, 'Mujer Maravilla'))
print()
print(mostrar_info(lista, 'Flash'))
print()
print(mostrar_info(lista, 'Star-Lord'))
print('\nSuperheroes con inicial B:')
superheroe_inicial(lista, 'B')
print('\nSuperheroes con inicial M:')
superheroe_inicial(lista, 'M')
print('\nSuperheroes con inicial S:')
superheroe_inicial(lista, 'S')
