import csv
from ClaseEmpleadoContratado import EmpleadoContratado
class ManejadorEmpleadoC():
    def LeerArchivo(self, Lista):
        with open("C:\\Users\\santi\\OneDrive\\Escritorio\\UNIDADES POO\\contratados.csv") as archivo:
            reader= csv.reader(archivo, delimiter=";")
            next(reader)#El next saltea la primer linea en el reader que contiene los nombres de los datos
            for i in reader:
                    Objeto=EmpleadoContratado(i[0],i[1],i[2],i[3],i[4],i[5],int(i[6]),float(i[7]))
                    Lista.append(Objeto)
        print("Datos de Empleado Contratado cargados correctamente!")
    
    def RegistrarHoras(self, Lista):
        i=0
        band=True
        dni=str(input("Ingrese dni de un empleado: "))
        horas=int(input("Ingrese la cantidad de horas trabajadas: "))
        while (i<len(Lista) and band==True):
            if(dni==Lista[i].getdni() and horas==Lista[i].gethoras()):
                horasinc=int(input("Ingrese la cantidad de horas que desea incrementar: "))
                Lista[i].incremento(horasinc)
                band=False
                print("Horas incrementadas correctamente!")
                print("Cantidad de horas nuevas: {}".format(Lista[i].gethoras()))
            else:
                print("El dni o la cantidad de horas no coincide.")
            i+=1
    
    def AyudaEconomica(self, Lista):
        for i in range(len(Lista)):
            if(Lista[i].getsueldo()<150000):
                print("{:<20} | {:<20} | {:<20}".format(Lista[i].getnombre(),Lista[i].getdireccion(),Lista[i].gettelefono()))
            