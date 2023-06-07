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