import csv
from ClaseFacultad import Facultad
from ClaseCarrera import Carrera
class ManejaFacultades:

    def __init__(self):
       self.__facultades = []

    def cargarDatos(self): #Aqui intento hacer la carga de otra forma (modificar )
        archivo = open("C:\\Users\\santi\\OneDrive\Escritorio\\UNIDADES POO\\Ejercicio1\\facultades.csv")
        reader = csv.reader(archivo,delimiter=",")
        band = True
        j = 0
        for i in reader:
            if band:
               facultad = Facultad(int(i[0]),i[1],i[2],i[3],i[4])
               cod = int(i[0])
               self.__facultades.append(facultad)
               band = False
            else:
                if cod == int(i[0]):
                    carrera = Carrera(int(i[1]),i[2],i[3],i[4],i[5])
                    self.__facultades[j].addCarrera(carrera)
                else:
                    j+=1
                    cod = int(i[0])
                    facultad = Facultad(int(i[0]),i[1],i[2],i[3],i[4])
                    self.__facultades.append(facultad)
        print("Datos cardados con exito!")
        archivo.close()
        
        
    def mostrarDatosFacultad(self,cod):
        if cod >= 1 and cod <= 5:
            print(self.__facultades[cod-1].getNombre())
            self.__facultades[cod-1].mostrarCarreras()
        else:
            print("Codigo de Facultad Incorrecto!")
       
    def mostrarDatosCarreras(self, nomb): #####
        i = self.__facultades
        j = 0 #para ir cambiando de facultades
        band = True #para frenar el while una vez que encuentre la carrera de una facultad
        while j < len(i) and band == True:
            nombre = i[j].buscarCarrera(nomb)
            if nombre!= "0":
                print("Codigo de Facultad: {}   Codigo de Carrera: {}".format(i[j].getCodigo(),i[j].getCodigoCarrera(nombre)))
                print("{}  localizada en: {}".format(i[j].getNombre(),i[j].getLocalidad()))
                band = False
            j+=1
        if band == True: #por si no encontro la carrera
            print("No se encuentra registrada la carrera ingresada!")
       