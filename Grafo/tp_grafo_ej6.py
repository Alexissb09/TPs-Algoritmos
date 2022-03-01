from grafo import Grafo
from lista import Lista

def inicializar_grafo1(grafo):
    grafo.insertar_vertice('Urano')
    grafo.insertar_vertice('Cronos')
    grafo.insertar_vertice('Rea')
    grafo.insertar_vertice('Zeus')
    grafo.insertar_vertice('Hades')
    grafo.insertar_vertice('Demeter')
    grafo.insertar_vertice('Atenea')
    grafo.insertar_vertice('Apollo')
    grafo.insertar_vertice('Persefone')
    grafo.insertar_vertice('Theia')
    grafo.insertar_vertice('Helios')
    grafo.insertar_vertice('Eos')
    grafo.insertar_vertice('Selene')

    grafo.insertar_arista(1, 'Urano', 'Cronos', data={'relacion': ['padre', 'hijo']})

    grafo.insertar_arista(1, 'Cronos', 'Zeus', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Hades', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Demeter', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Rea', data={'relacion': ['pareja']})

    grafo.insertar_arista(1, 'Zeus', 'Hades', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Zeus', 'Atenea', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Zeus', 'Apollo', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Zeus', 'Persefone', data={'relacion': ['padre', 'hijo']})

    grafo.insertar_arista(1, 'Demeter', 'Persefone', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Demeter', 'Urano', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Apollo', 'Persefone', data={'relacion': ['hermano']})

    grafo.insertar_arista(1, 'Theia', 'Helios', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Theia', 'Eos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Theia', 'Selene', data={'relacion': ['madre', 'hijo']})
    
def inicializar_grafo(grafo):
    grafo.insertar_vertice('Gaia')
    grafo.insertar_vertice('Urano')
    
    grafo.insertar_vertice('Themis')
    grafo.insertar_vertice('Minemosyne')
    grafo.insertar_vertice('Hyperion')
    grafo.insertar_vertice('Theia')
    grafo.insertar_vertice('Crios')
    grafo.insertar_vertice('Cronos')
    grafo.insertar_vertice('Rhea')
    grafo.insertar_vertice('Kdios')
    grafo.insertar_vertice('Phoibe')
    grafo.insertar_vertice('Iapetos')
    grafo.insertar_vertice('Okeanos')
    grafo.insertar_vertice('Tedds')
    
    grafo.insertar_vertice('Helios')
    grafo.insertar_vertice('Eos')
    grafo.insertar_vertice('Selene')
    grafo.insertar_vertice('Prometheus')
    grafo.insertar_vertice('Epimetheus')
    grafo.insertar_vertice('Atlas')
    grafo.insertar_vertice('Pleione')
    
    grafo.insertar_vertice('Hades')
    grafo.insertar_vertice('Demeter')
    grafo.insertar_vertice('Poseidon')
    grafo.insertar_vertice('Hestia')
    grafo.insertar_vertice('Hera')
    grafo.insertar_vertice('Zeus')
    grafo.insertar_vertice('Leto')
    grafo.insertar_vertice('Semelle')
    grafo.insertar_vertice('Maia')
    
    grafo.insertar_vertice('Persephone')
    grafo.insertar_vertice('Aphrodite')
    grafo.insertar_vertice('Ares')
    grafo.insertar_vertice('Hephaistos')
    grafo.insertar_vertice('Athena')
    grafo.insertar_vertice('Apollo')
    grafo.insertar_vertice('Artemis')
    grafo.insertar_vertice('Dionysos')
    grafo.insertar_vertice('Hermes')
    grafo.insertar_vertice('Penelopeia')
    
    grafo.insertar_vertice('Phobos')
    grafo.insertar_vertice('Deimos')
    grafo.insertar_vertice('Eros')
    grafo.insertar_vertice('Himeros')
    
    grafo.insertar_vertice('Hermaphrodite')
    grafo.insertar_vertice('Pan')
    
    grafo.insertar_arista(1, 'Urano', 'Gaia', data={'relacion': ['hijo', 'madre', 'pareja']})
    
    grafo.insertar_arista(1, 'Urano', 'Themis', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Hyperion', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Theia', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Crios', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Cronos', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Rhea', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Iapetos', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Okeanos', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Urano', 'Tedds', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Gaia', 'Themis', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Hyperion', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Theia', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Crios', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Cronos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Rhea', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Iapetos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Okeanos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Gaia', 'Tedds', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Hyperion', 'Theia', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Hyperion', 'Helios', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Hyperion', 'Eos', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Hyperion', 'Selene', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Theia', 'Helios', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Theia', 'Eos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Theia', 'Selene', data={'relacion': ['madre', 'hijo']})
    
    grafo.insertar_arista(1, 'Iapetos', 'Prometheus', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Iapetos', 'Epimetheus', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Iapetos', 'Atlas', data={'relacion': ['padre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Okeanos', 'Tedds', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Okeanos', 'Pleione', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Tedds', 'Pleione', data={'relacion': ['madre', 'hijo']})
    

    grafo.insertar_arista(1, 'Cronos', 'Rhea', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Cronos', 'Hades', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Demeter', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Poseidon', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Hestia', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Hera', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Cronos', 'Zeus', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Rhea', 'Hades', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Rhea', 'Demeter', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Rhea', 'Poseidon', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Rhea', 'Hestia', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Rhea', 'Hera', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Rhea', 'Zeus', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Kdios', 'Phoibe', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Kdios', 'Leto', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Phoibe', 'Leto', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Atlas', 'Pleione', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Atlas', 'Maia', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Pleione', 'Maia', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Demeter', 'Zeus', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Demeter', 'Persephone', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Zeus', 'Persephone', data={'relacion': ['padre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Hera', 'Zeus', data={'relacion': ['pareja', 'hermano']})
    
    grafo.insertar_arista(1, 'Hera', 'Ares', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Hera', 'Hephaistos', data={'relacion': ['madre', 'hijo']})
    
    grafo.insertar_arista(1, 'Zeus', 'Ares', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Zeus', 'Hephaistos', data={'relacion': ['padre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Zeus', 'Athena', data={'relacion': ['pareja']})
    
    
    grafo.insertar_arista(1, 'Zeus', 'Leto', data={'relacion': ['pareja']})
    
    grafo.insertar_arista(1, 'Zeus', 'Apollo', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Zeus', 'Artemis', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Leto', 'Apollo', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Leto', 'Artemis', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Zeus', 'Semelle', data={'relacion': ['pareja']})
    
    grafo.insertar_arista(1, 'Zeus', 'Dionysos', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Semelle', 'Dionysos', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Zeus', 'Maia', data={'relacion': ['pareja']})
    
    grafo.insertar_arista(1, 'Zeus', 'Hermes', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Maia', 'Hermes', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Hades', 'Persephone', data={'relacion': ['pareja']})
    
    
    grafo.insertar_arista(1, 'Aphrodite', 'Ares', data={'relacion': ['pareja']})
    
    grafo.insertar_arista(1, 'Aphrodite', 'Phobos', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Aphrodite', 'Deimos', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Aphrodite', 'Eros', data={'relacion': ['padre', 'hijo']})
    grafo.insertar_arista(1, 'Aphrodite', 'Himeros', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Ares', 'Phobos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Ares', 'Deimos', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Ares', 'Eros', data={'relacion': ['madre', 'hijo']})
    grafo.insertar_arista(1, 'Ares', 'Himeros', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Aphrodite', 'Hephaistos', data={'relacion': ['pareja']})
    
    
    grafo.insertar_arista(1, 'Aphrodite', 'Hermes', data={'relacion': ['pareja']})
    
    grafo.insertar_arista(1, 'Aphrodite', 'Hermaphrodite', data={'relacion': ['madre', 'hijo']})
    
    grafo.insertar_arista(1, 'Hermes', 'Hermaphrodite', data={'relacion': ['padre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Hermes', 'Penelopeia', data={'relacion': ['pareja']})
    
    grafo.insertar_arista(1, 'Hermes', 'Pan', data={'relacion': ['padre', 'hijo']})
    
    grafo.insertar_arista(1, 'Penelopeia', 'Pan', data={'relacion': ['madre', 'hijo']})
    
    
    grafo.insertar_arista(1, 'Themis', 'Minemosyne', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Hyperion', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Theia', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Crios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Cronos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Rhea', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Kdios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Phoibe', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Themis', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Minemosyne', 'Hyperion', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Theia', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Crios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Cronos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Rhea', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Kdios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Phoibe', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Minemosyne', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Hyperion', 'Crios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Cronos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Rhea', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Kdios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Phoibe', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hyperion', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Theia', 'Cronos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Theia', 'Rhea', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Theia', 'Kdios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Theia', 'Phoibe', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Theia', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Theia', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Theia', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Cronos', 'Rhea', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Cronos', 'Kdios', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Cronos', 'Phoibe', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Cronos', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Cronos', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Cronos', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Kdios', 'Phoibe', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Kdios', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Kdios', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Kdios', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Phoibe', 'Iapetos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Phoibe', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Phoibe', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Iapetos', 'Okeanos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Iapetos', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Okeanos', 'Tedds', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Helios', 'Eos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Helios', 'Selene', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Eos', 'Selene', data={'relacion': ['hermano']})
    
    
    grafo.insertar_arista(1, 'Prometheus', 'Epimetheus', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Prometheus', 'Atlas', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Epimetheus', 'Atlas', data={'relacion': ['hermano']})

    
    grafo.insertar_arista(1, 'Hades', 'Demeter', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hades', 'Poseidon', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hades', 'Hestia', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hades', 'Hera', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hades', 'Zeus', data={'relacion': ['hermano']})
    

    grafo.insertar_arista(1, 'Demeter', 'Poseidon', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Demeter', 'Hestia', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Demeter', 'Hera', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Poseidon', 'Hestia', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Poseidon', 'Hera', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Poseidon', 'Zeus', data={'relacion': ['hermano']})

    grafo.insertar_arista(1, 'Hestia', 'Hera', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Hestia', 'Zeus', data={'relacion': ['hermano']})

    
    grafo.insertar_arista(1, 'Ares', 'Hephaistos', data={'relacion': ['hermano']})
    
    
    grafo.insertar_arista(1, 'Apollo', 'Artemis', data={'relacion': ['hermano']})
    
    
    grafo.insertar_arista(1, 'Phobos', 'Deimos', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Phobos', 'Eros', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Phobos', 'Himeros', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Deimos', 'Eros', data={'relacion': ['hermano']})
    grafo.insertar_arista(1, 'Deimos', 'Himeros', data={'relacion': ['hermano']})
    
    grafo.insertar_arista(1, 'Eros', 'Himeros', data={'relacion': ['hermano']})

grafo_dioses = Grafo(dirigido = False)
inicializar_grafo(grafo_dioses)

def cargar_descripcion(grafo):
    
    pausa = ' '

    for i in range(0, grafo.inicio.tamanio()):
        pasa_20_palabras = False

        dios = grafo.inicio.obtener_elemento(i)

        while not pasa_20_palabras:
            descripcion = input('Agregar descripcion a ' + dios['info'] + ' : ')

            if len(descripcion.split()) < 3:
                dios['data'] = descripcion
                pasa_20_palabras = True
            else:
                print('La descripcion debe ser igual o menor a 20 letras')
                pausa = input()
                pasa_20_palabras = False


def mostrar_hijos(grafo, vertice_dios):

    pos_origen = grafo.buscar_vertice(vertice_dios)
    nombre = ' '
    pausa = ' '

    if pos_origen != -1:
        dios = grafo.inicio.obtener_elemento(pos_origen)

        for i in range(0, dios['aristas'].tamanio()):
            nombre = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']

            if len(dios_aux['relacion']) > 1:
                if dios_aux['relacion'][0] == 'padre' or dios_aux['relacion'][0] == 'madre':
                    print(nombre, ' relacion: ', dios_aux['relacion'])
    else:
        print('El dios ', vertice_dios, ' no esta')

def nombres_parientes_dios(grafo, vertice_dios):
    
    pos_origen = grafo.buscar_vertice(vertice_dios)
    nombre = ''

    if pos_origen != -1:
        dios = grafo.inicio.obtener_elemento(pos_origen)
        print('Nombre dios: ', vertice_dios)

        for i in range(0, dios['aristas'].tamanio()):
            nombre = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']
            print(nombre, dios_aux['relacion'])

def relacion_directa(grafo, ver_origen, ver_destino):
    print('Relacion directa: ')
    pos = grafo.buscar_arista(ver_origen, ver_destino)

    if pos != -1:
        pos_aux = grafo.buscar_vertice(ver_origen)
        print(grafo.inicio.obtener_elemento(pos_aux)['aristas'].obtener_elemento(pos))

def camino_mas_corto_vertices(grafo, nom_origen, nom_destino):

    ver_origen = grafo.buscar_vertice(nom_origen)
    ver_destino = grafo.buscar_vertice(nom_destino)
    costo = None

    if ver_origen != -1 and ver_destino != -1:
        camino = grafo.dijkstra(ver_origen)

        while not camino.pila_vacia():
            dato = camino.desapilar()

            if dato[1][0] == nom_destino:
                if costo is None:
                    costo = dato[0]
                print('Paso por: ', dato[1][0])
                destino = dato[1][1]

        print('El costo del camino mas corto es: ', costo)

def buscar_dios_relacion(grafo, vertice_dios, nom_relacion):
    pos_origen = grafo.buscar_vertice(vertice_dios)
    nombre = ''

    if pos_origen != -1:
        dios = grafo.inicio.obtener_elemento(pos_origen)

        for i in range(dios['aristas'].tamanio()):
            relacion = dios['aristas'].obtener_elemento(i)['data']['relacion']

            if len(relacion) > 1 and relacion[1] == nombre_relacion:
                return  dios['aristas'].obtener_elemento(i)['destino']
    else:
        return None

def barrido_mostrando_relacion(grafo, pos_vertice_dios, nombre_relacion):

    while pos_vertice_dios < grafo.inicio.tamanio():
        vertice = grafo.inicio.obtener_elemento(pos_vertice_dios)

        if not vertice['visitado']:
            vertice['visitado'] = True
            madre_dios = buscar_dios_relacion(grafo, vertice['info'], nombre_relacion)

            if madre_dios is not None:
                print(vertice['info'], ' madre: ', madre_dios)
            else:
                print(vertice['info'], ' no tiene madre')
            aristas = 0

            while aristas < vertice['aristas'].tamanio():
                arista = vertice['aristas'].obtener_elemento(aristas)
                pos_vertice = grafo.buscar_vertice(arista['destino'])
                nuevo_vertice = grafo.inicio.obtener_elemento(pos_vertice)

                if not nuevo_vertice['visitado']:
                    barrido_mostrando_relacion(grafo, pos_vertice, nombre_relacion)
                    aristas += 1

        pos_vertice_dios += 1

def falta_elemento(dato, vector, campo):
    for vec in vector:
        if vec[campo] == dato:
            return False
    return True

def ancestro_de_dios(grafo, nom_origen, nom_dios = '', vec_ancestros = [], pasada = True):
    pausa = None
    indice = 0
    relacion = ''
    pos_origen = grafo.buscar_vertice(nom_dios)
    nombre = ''

    if pos_origen >= 0 and pos_origen != -1:
        dios = grafo.inicio.obtener_elemento(pos_origen)

        for i in range(dios['aristas'].tamanio()):
            nombre = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']

            if pasada and len(dios_aux['relacion']) > 1:
                if dios_aux['relacion'][0] == 'hijo':
                    vec_ancestros.append({'nombre': nombre, 'relacion': dios_aux['relacion'][1], 'visitado': False})

            if not pasada:
                if len(dios_aux['relacion']) > 1:
                    indice = 1
                else:
                    indice = 0

            if dios_aux['relacion'][indice] == 'hermano':
                relacion = 'tio'
            elif dios_aux['relacion'][indice] == 'pareja':
                relacion = 'madrastra'
            else:
                relacion = dios_aux['relacion'][indice]

            if falta_elemento(nombre, vec_ancestros, 'nombre') and nombre != nom_origen and relacion != 'hijo':
                vec_ancestros.append({'nombre': nombre, 'relacion': relacion, 'visitado': False})

        if i == (dios['aristas'].tamanio() - 1):
            for ancestro in vec_ancestros:
                if ancestro['relacion'] in ['padre', 'madre'] and ancestro['visitado'] == False:
                    ancestro['visitado'] = True
                    ancestro_de_dios(grafo, nom_origen, ancestro['nombre'], vec_ancestros, False)
    else:
        print('El dios ', nom_dios, ' no esta en el grafo')

def mostrar_ancestro_de_dios(grafo, nom_dios):
    vec_ancestros = []
    ancestro_de_dios(grafo, nom_dios, nom_dios, vec_ancestros)
    print('Ancestros de ', nom_dios)
    for ancestro in vec_ancestros:
        print('Nombre: ', ancestro['nombre'], ', relacion: ', ancestro['relacion'])


def hijos_de_dios(grafo, vertice_dios, vec_nietos = []):
    pos_origen = grafo.buscar_vertice(vertice_dios)
    nombre = ''

    if pos_origen != -1:
        dios = grafo.inicio.obtener_elemento(pos_origen)

        for i in range(dios['aristas'].tamanio()):
            nombre = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']

            if len(dios_aux['relacion']) > 1:
                if dios_aux['relacion'][0] == 'padre' or dios_aux['relacion'][0] == 'madre':
                    if not nombre in vec_nietos:
                        vec_nietos.append(nombre)
    else:
        print('El dios ', vertice_dios, ' no esta en el grafo')

def mostrar_nietos_de_dios(grafo, nom_dios):
    pos_origen = grafo.buscar_vertice(nom_dios)
    nombre = ''
    vec_nietos = []

    if pos_origen != -1:
        dios = grafo.inicio.obtener_elemento(pos_origen)

        for i in range(dios['aristas'].tamanio()):
            nombre = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']

            if len(dios_aux['relacion']) > 1:
                if dios_aux['relacion'][0] == 'padre' or dios_aux['relacion'][0] == 'madre':
                    hijos_de_dios(grafo, nombre, vec_nietos)
    else:
        print('El dios ', nom_dios, ' no esta en el grafo')

    print('Nietos de ', nom_dios)
    for nieto in vec_nietos:
        print(nieto)


# cargar_descripcion(grafo_dioses) # Punto A
print()
mostrar_hijos(grafo_dioses, 'Cronos') # Punto C
print()
nombres_parientes_dios(grafo_dioses, 'Cronos') # Punto D
print()
relacion_directa(grafo_dioses, 'Cronos', 'Rea') # Punto E
print()
camino_mas_corto_vertices(grafo_dioses, 'Urano', 'Cronos') # Punto F
print()
grafo_dioses.barrido_profundidad(0) # Punto G
grafo_dioses.barrido_amplitud(0) 
print()
barrido_mostrando_relacion(grafo_dioses, 0, 'madre') # Punto H
print()
mostrar_ancestro_de_dios(grafo_dioses, 'Persephone') # Punto I
print()
mostrar_nietos_de_dios(grafo_dioses, 'Cronos') # Punto J
print()
mostrar_hijos(grafo_dioses, 'Theia')