matriz = [[1,1,0,1,0],
          [1,1,1,1,0],
          [1,1,1,1,0],
          [1,0,1,0,0],
          [1,0,1,1,1]]
          
def salida(laberinto, x, y, tamanio_matriz):
    if x == tamanio_matriz and y == tamanio_matriz:
        laberinto[x][y] = 2
        return True
    else:
        if x >= 0 and x <= 4 and y >= 0 and y <= 4 and laberinto[x][y] == 1:
            laberinto[x][y] = 2
            if salida(laberinto,x,y+1, tamanio_matriz) or salida(laberinto,x+1,y, tamanio_matriz) or salida(laberinto,x-1,y, tamanio_matriz) or salida(laberinto,x,y-1, tamanio_matriz):
                return True
        else:
            return False

print(salida(matriz, 0, 0, len(matriz)-1))
print(matriz)