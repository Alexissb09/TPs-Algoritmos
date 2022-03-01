from grafo import Grafo
from lista import Lista

grafo = Grafo(dirigido=False)

grafo.insertar_vertice('Atenas', {'latitud' : 17, 'longitud' : 8})
grafo.insertar_vertice('Zeus', {'latitud' : 13, 'longitud' : 14})
grafo.insertar_vertice('Hera', {'latitud' : 7, 'longitud' : 1})
grafo.insertar_vertice('Apolo', {'latitud' : 3, 'longitud' : 5})
grafo.insertar_vertice('Poseidon', {'latitud' : 1, 'longitud' : 1})
grafo.insertar_vertice('Artemisa', {'latitud' : 3, 'longitud' : 20})
grafo.insertar_vertice('Teatro', {'latitud' : 20, 'longitud' : 3})

def crear_grafo(grafo):
	lugar = Lista()
	for i in range(grafo.inicio.tamanio()):
		lugar_origen = grafo.inicio.obtener_elemento(i)
		km_origen = lugar_origen['data']['latitud'] + lugar_origen['data']['longitud']

		for j in range(i+1, grafo.inicio.tamanio()):
			lugar_destino = grafo.inicio.obtener_elemento(j)
			km_destino = lugar_destino['data']['latitud'] + lugar_destino['data']['longitud']
			distancia = abs(km_origen - km_destino)
			grafo.insertar_arista(distancia, lugar_origen['info'], lugar_destino['info'])

def expancion_min(grafo, lugar): # Halla arbol de expancion minima
	vertice_origen = grafo.buscar_vertice(lugar)

	if vertice_origen != 1:
		grafo.prim(vertice_origen)

def camino_corto(grafo, origen, destino): # Busca el camino mas corto entre dos vertices
	vertice_origen = grafo.buscar_vertice(origen)
	vertice_destino = grafo.buscar_vertice(destino)
	costo = None

	if vertice_origen != -1 and vertice_destino != -1:
		camino = grafo.dijkstra(vertice_origen)
		while not camino.pila_vacia():
			dato = camino.desapilar()
			if dato[1][0] == destino:
				if costo is None:
					costo = dato[0]
				print('paso por', dato[1][0])
				destino = dato[1][1]
		print('Camino mas corto:', costo)

crear_grafo(grafo)
expancion_min(grafo, 'Atenas')
camino_corto(grafo,	'Atenas', 'Apolo')