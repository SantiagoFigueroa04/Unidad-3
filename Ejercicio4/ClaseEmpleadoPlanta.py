from ClaseEmpleado import Empleado
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