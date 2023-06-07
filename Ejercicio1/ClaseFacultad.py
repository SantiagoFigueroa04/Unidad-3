class Facultad:
    __codigo: int
    __nombre: str
    __direccion: str
    __localidad: str
    __telefono: str
    __carreras = []
    
    def __init__(self,cod,nom,direc,loc,tel):
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = direc
        self.__localidad = loc
        self.__telefono = tel
        
    def addCarrera(self,carrera):
        self.__carreras.append(carrera)
        
    def getNombre(self):
        return self.__nombre
    def getCodigo(self):
        return self.__codigo
    def getLocalidad(self):
        return self.__localidad
    
    def mostrarCarreras(self):
        print("         Carreras")
        for i in self.__carreras:
            print("{}    {}".format(i.getNombre(), i.getDuracion()))
    
    def buscarCarrera(self,nom):
        aux = "0"
        for i in self.__carreras:
            if i.getNombre() == nom:
                aux = i.getNombre()
        return aux
        
    def getCodigoCarrera(self,nomb):
        codigo = "0"
        for i in self.__carreras:
            if i.getNombre() == nomb:
                codigo = i.getCodigo()
        return codigo
             
        
        