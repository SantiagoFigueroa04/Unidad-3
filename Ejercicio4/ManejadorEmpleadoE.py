import csv
from ClaseEmpleadoExterno import EmpleadoExterno
class ManejadorEmpleadoE:
    def LeerArchivo(self, Lista):
        with open("C:\\Users\\santi\\OneDrive\\Escritorio\\UNIDADES POO\\externos.csv") as archivo:
            reader= csv.reader(archivo, delimiter=";")
            next(reader)#El next saltea la primer linea en el reader que contiene los nombres de los datos
            for i in reader:
                    Objeto=EmpleadoExterno(i[0],i[1],i[2],i[3],i[4],i[5],i[6],int(i[7]),int(i[8]),float(i[9]))
                    Lista.append(Objeto)
        print("Datos de Empleado Externo cargados correctamente!")
    
    def TotalDeTarea(self, Lista):
        i=0
        band=True
        tarea=input("Ingrese una tarea: ")
        while (i<len(Lista) and band==True):
            if (tarea==Lista[i].gettarea()):
                print("El monto total a pagar por la tarea de {}, es de: {}".format(tarea, Lista[i].getmonto()))
            i+=1
    def AyudaEconomica(self, Lista):
        for i in range(len(Lista)):
            if(Lista[i].getsueldo()<150000):
                print("{:<20} | {:<20} | {:<20}".format(Lista[i].getnombre(),Lista[i].getdireccion(),Lista[i].gettelefono()))
                #:<20 Alinea el texto 