from arboles import Arbol
from cola import Cola
from lista import Lista

lista_dic_heroes = Lista()
arbol_criaturas = Arbol()
dic_criaturas = [{'Criatura': 'Ceto', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Tifon', 'Derrotado': 'Zeus', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Equidna', 'Derrotado': 'Argos panoptnes', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Dino', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Pefredo', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Enio', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Escila', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Caribdis', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Euriale', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Esteno', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Medusa', 'Derrotado': 'Perseo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Ladon', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Aguila del Caucaso', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Quimera', 'Derrotado': 'Belerofonte', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Hidra de Lerna', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Leon de Nemea', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Esfinge', 'Derrotado': 'Edipo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Dragon de la Colquida', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Cerbero', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Cerda de Cromion', 'Derrotado': 'Teseo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Ortro', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : 'Heracles'},
				{'Criatura': 'Toro de Creta', 'Derrotado': 'Teseo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Jabali De Calidon', 'Derrotado': 'Atalanta', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Carcinos', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Gerion', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Cloto', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Laquesis', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : 'Heracles'},
				{'Criatura': 'Atropos', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Minotauro de Creta', 'Derrotado': 'Teseo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Harpias', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Argos Panoptnes', 'Derrotado': 'Hermes', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Aves del Estinfalo', 'Derrotado': 'Heracles', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 5, 'Capturada' : '-'},
				{'Criatura': 'Talos', 'Derrotado': 'Medea', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Sirenas', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Piton', 'Derrotado': 'Apolo', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 1, 'Capturada' : '-'},
				{'Criatura': 'Cierva de Cerinea', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Basilisco', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				{'Criatura': 'Jabali de Erimanto', 'Derrotado': '-', 'Descripcion' : 'No hay descripcion', 'Cant_Derrotado': 0, 'Capturada' : '-'},
				]
    
arbol_criaturas = arbol_criaturas.cargar_arbol(dic_criaturas, 'Criatura')

def cargar_descripcion(arbol): # Punto B
    pendientes = Cola()
    pendientes.arribo(arbol)
    
    while(not pendientes.cola_vacia()):
        nodo = pendientes.atencion()
        print(nodo.info, nodo.datos)
        nodo.datos['Descripcion'] = input('Cargar descripcion de la criatura: ')
        if(nodo.izq is not None):
            pendientes.arribo(nodo.izq)
        if(nodo.der is not None):
            pendientes.arribo(nodo.der)

def ocurrencias_heroe(arbol, nombre_heroe): # Punto D
    cont = 0

    if(arbol.info is not None):
        if(arbol.datos['Derrotado'] == nombre_heroe):
            contador += 1
        if(arbol.izq is not None):
            contador += ocurrencias_heroe(arbol.izq, nombre_heroe)
        if(arbol.der is not None):
            contador += ocurrencias_heroe(arbol.der, nombre_heroe)
    
    return cont

def datos_arbol(arbol, campo, vec_datos=[]):
    if(arbol.info is not None):
        if(not((arbol.datos[campo] in vec_datos))
            and (arbol.datos[campo] not in ['', '-', None])):
            vec_datos.append(arbol.datos[campo])
        if(arbol.izq is not None):
            heroes = datos_arbol(arbol.izq, campo, vec_datos)
        if(arbol.der is not None):
            heroes = datos_arbol(arbol.der, campo, vec_datos)

    return vec_datos

def mayor_derrotados_heroes(arbol):
    vector_heroes = datos_arbol(arbol, 'Derrotado')
    ocurrencias = 0
    lista_dic_heroes = Lista()

    for nombre_heroe in vector_heroes:
        ocurrencias = mayor_derrotados_heroes(arbol, nombre_heroe)
        lista_dic_heroes.insertar({'nombre': nombre_heroe,
                                 'cantidad_Derrotados': ocurrencias}, 
                                 'cantidad_Derrotados')
    
    return lista_dic_heroes

def mostrar_tres_heroes_criaturasDerrotadas(lista):
    i = lista.tamanio()-1
    while((not lista.lista_vacia()) and (i >= (lista.tamanio()-3))):
        print(lista.obtener_elemento(i))
        i -= 1

def criaturas_derrotadas_inorden(arbol, nombre): # Punto E
    if(arbol.info is not None):
        if(arbol.izq is not None):
            criaturas_derrotadas_inorden(arbol.izq, nombre)
        if(arbol.datos['Derrotado'] == nombre):
            print(arbol.datos['Criatura'])
        if(arbol.der is not None):
            criaturas_derrotadas_inorden(arbol.der, nombre)

def modificar_campo_capturado(arbol, criaturas, capturado_por): # Punto H
    for criatura in criaturas:
        pos = arbol.busqueda(criatura)
        if(pos is not None):
            pos.datos['Capturada'] = capturado_por
        else:
            print('La criatura "' + criatura + '" no esta en el arbol')

def eliminar_criatura(arbol, criaturas): # Punto J
    for criatura in criaturas:
        info, datos = arbol.eliminar_nodo(criatura)

        if(info is None or datos is None):
            print('La criatura "' + criatura + '" no se encontro en el arbol')
        else:
            print('Eliminado: ', info, datos)

def modificar_criatura(arbol, campo, criatura, dato): # Punto K
    pos = arbol.busqueda(criatura)
    if(pos is not None):
        pos.datos[campo] = dato
    else:
        print('La criatura "' + criatura + '" no esta en el arbol')
    return pos


def modificar_nombre_criatura(arbol, criatura, nombre_modificado): # Punto L
    info, datos = arbol.eliminar_nodo(criatura)
    if datos is not None:
        datos['Criatura'] = nombre_modificado
        arbol.insertar_nodo(datos['Criatura'], datos)
    else:
        print('La criatura "' + criatura + '" no esta en el arbol')

def listado_criaturas_capturadas(arbol, nombre_heroe): # Punto N
    if(arbol.info is not None):
        if(arbol.izq is not None):
            listado_criaturas_capturadas(arbol.izq, nombre_heroe)
        if(arbol.datos['Capturada'] == nombre_heroe):
            print(arbol.info, arbol.datos)
        if(arbol.der is not None):
            listado_criaturas_capturadas(arbol.der, nombre_heroe)


arbol_criaturas.inorden() # Punto A

cargar_descripcion(arbol_criaturas) # Punto B

print(arbol_criaturas.busqueda('Talos').datos) # Punto C

# Punto D

lista_dic_heroes = mayor_derrotados_heroes(arbol_criaturas)
mostrar_tres_heroes_criaturasDerrotadas(lista_dic_heroes)


criaturas_derrotadas_inorden(arbol_criaturas, 'Heracles') # Punto E

criaturas_derrotadas_inorden(arbol_criaturas, '-') # Punto F

# Punto H
vec_criaturas = ['Cerbero', 'Toro de Creta', 'Cierva de Cerinea', 
                     'Jabali de Erimanto']

modificar_campo_capturado(arbol_criaturas, vec_criaturas, 'Heracles')


# Punto I

buscado = input('Ingrese nombre de criatura a buscar: ')
arbol_criaturas.busqueda_proximidad(buscado)


# Punto J

criaturas_eliminar = ['Basilisco', 'Las Sirenas']
eliminar_criatura(arbol_criaturas, criaturas_eliminar)


# Punto K

modificar_criatura(arbol_criaturas, 'Cant_Derrotado', 'Aves del Estinfalo', 10)
modificar_criatura(arbol_criaturas, 'Derrotado', 'Aves del Estinfalo', 'Heracles')


modificar_nombre_criatura(arbol_criaturas, 'Ladon', 'Dragon Ladon') # Punto L

arbol_criaturas.barrido_por_nivel() # Punto M

listado_criaturas_capturadas(arbol_criaturas, 'Heracles') # Punto N
