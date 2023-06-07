import csv
from ClaseEmpleadoPlanta import EmpleadoPlanta
class ManejadorEmpleadoP():
    def LeerArchivo(self, Lista):
        with open("C:\\Users\\santi\\OneDrive\\Escritorio\\UNIDADES POO\\planta.csv") as archivo:
            reader= csv.reader(archivo, delimiter=";")
            next(reader)#El next saltea la primer linea en el reader que contiene los nombres de los datos
            for i in reader:
                    Objeto=EmpleadoPlanta(i[0],i[1],i[2],i[3],float(i[4]),int(i[5]))
                    Lista.append(Objeto)
        print("Datos de Empleado Planta cargados correctamente!")

    def AyudaEconomica(self, Lista):
        for i in range(len(Lista)):
            if(Lista[i].getsueldo()<150000):
                print("{:<20} | {:<20} | {:<20}".format(Lista[i].getnombre(),Lista[i].getdireccion(),Lista[i].gettelefono()))
