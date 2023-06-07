import numpy as np
class ArregloNumpy:
    def __init__(self):
        tamaño=int(input(("Ingrese tamaño del arreglo numpy: ")))
        self.__arreglo=np.zeros(tamaño)
        self.__arreglo=np.genfromtxt("planta.csv", delimiter=";")
  
    def getdatos(self):
        return self.__arreglo