import numpy as np
import csv
class Empleado:
    def __init__(self, nom, dni, dir, tel):
        self.__nombre=nom
        self.__dni=dni
        self.__direccion=dir
        self.__telefono=tel
    
    def getdni(self):
        return self.__dni
    def getnombre(self):
        return self.__nombre
    def getdireccion(self):
        return self.__direccion
    def gettelefono(self):
        return self.__telefono
    
class EmpleadoPlanta(Empleado):
    def __init__(self, dni, nom, dir, tel, sueldo, anti):
        super().__init__(dni, nom, dir, tel)
        self.__sueldo=sueldo
        self.__antiguedad=anti

    def getsueldo(self):
        return self.__sueldo+0.01*self.__antiguedad
    def getnombre(self):
        return super().getnombre()
    def getdireccion(self):
        return super().getdireccion()
    def gettelofono(self):
        return super().gettelefono()
    
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

class EmpleadoContratado(Empleado):
    def __init__(self, dni, nom, dir, tel, fechaI, fechaF, horas, valor):
        super().__init__(dni, nom, dir, tel)
        self.__fechaI=fechaI
        self.__fechaF=fechaF
        self.__canthoras=horas
        self.__valorhora=valor
    
    def getsueldo(self):
        return self.__canthoras*self.__valorhora
    
    def getdni(self):
        return super().getdni()
    
    def gethoras(self):
        return self.__canthoras
    
    def incremento(self, horas):
        self.__canthoras+=horas

    def getnombre(self):
        return super().getnombre()
    def getdireccion(self):
        return super().getdireccion()
    def gettelofono(self):
        return super().gettelefono()

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
            
class EmpleadoExterno(Empleado):
    def __init__(self, dni, nom, dir, tel, tarea, fechaI, fechaF, monto, costo, montoS):
        super().__init__(dni, nom, dir, tel)
        self.__tarea=tarea
        self.__fechaI=fechaI
        self.__fechaF=fechaF
        self.__montoV=monto
        self.__costoObra=costo
        self.__montoS=montoS

    def getsueldo(self):
        return self.__costoObra-self.__montoV-self.__montoS
    
    def gettarea(self):
        return self.__tarea
    def getmonto(self):
        return self.__costoObra
    
    def getnombre(self):
        return super().getnombre()
    def getdireccion(self):
        return super().getdireccion()
    def gettelofono(self):
        return super().gettelefono()
    
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

class ArregloNumpy:
    def __init__(self):
        tamaño=int(input(("Ingrese tamaño del arreglo numpy: ")))
        self.__arreglo=np.zeros(tamaño)
        self.__arreglo=np.genfromtxt("planta.csv", delimiter=";")
  
    def getdatos(self):
        return self.__arreglo
    
if __name__=="__main__":
    ListaPlanta=[]
    MEP=ManejadorEmpleadoP()
    MEP.LeerArchivo(ListaPlanta)

    ListaContratado=[]
    MEC=ManejadorEmpleadoC()
    MEC.LeerArchivo(ListaContratado)

    ListaExterno=[]
    MEE=ManejadorEmpleadoE()
    MEE.LeerArchivo(ListaExterno)

    MEC.RegistrarHoras(ListaContratado)
    MEE.TotalDeTarea(ListaExterno)

    print("Nombre, direccion y dni del empleado cuyo sueldo es inferior a $150000 ")
    MEP.AyudaEconomica(ListaPlanta)
    MEC.AyudaEconomica(ListaContratado)
    MEE.AyudaEconomica(ListaExterno)

    