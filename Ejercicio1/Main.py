from ManejaFacultades import ManejaFacultades
from MenuDeOpciones import menuDeOpciones
if __name__ == "__main__":
    facultades = ManejaFacultades()
    facultades.cargarDatos()
    menuDeOpciones(facultades)
        
    