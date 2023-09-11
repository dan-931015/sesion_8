import os
import random
from functools import reduce

class Juego:
    def __init__(self, mapa, inicio, fin):
        self.mapa = mapa
        self.inicio = inicio
        self.fin = fin
    
    def mover(self, direccion):
        fila_actual, columna_actual = self.inicio
        print(f"Coordenadas actuales: Fila {fila_actual}, Columna {columna_actual}")

        if direccion == 'arriba':
            fila_actual -= 1
        elif direccion == 'abajo':
            fila_actual += 1
        elif direccion == 'izquierda':
            columna_actual -= 1
        elif direccion == 'derecha':
            columna_actual += 1
        
        print(f"Intentando moverse a: Fila {fila_actual}, Columna {columna_actual}")

        if self.mapa[fila_actual][columna_actual] == '#':
            print("¡Se encontró una pared!")
            return False
        elif self.mapa[fila_actual][columna_actual] == 'F':
            print("¡Has llegado a la meta!")
            return True
        
        self.inicio = (fila_actual, columna_actual)
        return False

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        mapa, inicio, fin = self.leer_mapa_aleatorio(path_a_mapas)
        super().__init__(mapa, inicio, fin)
    
    def convertir_cadena_a_matriz(self, cadena):
        return list(map(list, filter(None, cadena.split('\n'))))

    def leer_mapa_aleatorio(self, path_a_mapas):
        lista_archivos = os.listdir(path_a_mapas)
        nombre_archivo = random.choice(lista_archivos)
        path_completo = os.path.join(path_a_mapas, nombre_archivo)

        with open(path_completo, 'r') as archivo:
            lineas = archivo.readlines()
            dimensiones = list(map(int, lineas[0].strip().split(',')))
            filas, columnas = dimensiones[0], dimensiones[1]
            inicio = tuple(map(int, lineas[filas + 1].strip().split(',')))
            fin = tuple(map(int, lineas[filas + 2].strip().split(',')))

            mapa = reduce(lambda acc, linea: acc + linea.strip(), lineas[1:filas + 1], "")

        return self.convertir_cadena_a_matriz(mapa), inicio, fin

if __name__ == "__main__":
    path_a_mapas = r"C:\Users\Los Foneffos\Desktop\mi_juego\map"
    juego = JuegoArchivo(path_a_mapas)
      
    while True:
        print("\nMapa actual:")
        for fila in juego.mapa:
            print("".join(fila))
        
        direccion = input("Ingresa la dirección (arriba/abajo/izquierda/derecha): ")
        if juego.mover(direccion):
            print("¡Has llegado a la meta!")
            break
