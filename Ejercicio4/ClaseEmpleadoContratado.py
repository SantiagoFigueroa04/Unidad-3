from ClaseEmpleado import Empleado
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
