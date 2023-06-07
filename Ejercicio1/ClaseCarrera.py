class Carrera:
    __codigo: int
    __nombre: str
    __fechaInicio: str
    __duracion: str
    __titulo: str
    
    def __init__(self,cod,nom,fecha,dur,tit):
        self.__codigo = cod
        self.__nombre = nom
        self.__fechaInicio = fecha
        self.__duracion = dur
        self.__titulo = tit
        
    def getNombre(self):
        return self.__nombre
    def getDuracion(self):
        return self.__duracion
    def getCodigo(self):
        return self.__codigo
        