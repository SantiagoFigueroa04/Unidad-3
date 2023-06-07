from ClaseEmpleado import Empleado
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
    