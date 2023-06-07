from MostrarMenu import mostrarMenu
def menuDeOpciones(facultades):
   mostrarMenu()
   op = str(input("Ingrese una opcion--> "))   
   while op != "0":
       if op == "1":
           cod = int(input("Ingrese un codigo de facultad '1 - 5': "))
           facultades.mostrarDatosFacultad(cod)
       elif op == "2":
           NombreCarrera = str(input("Ingrese una carrera: "))
           facultades.mostrarDatosCarreras(NombreCarrera)  
       else:
           print("Opcion Incorrecta!")
           
       mostrarMenu()
       op = str(input("Ingrese una nueva opcion--> "))
   print("Finalizando operacion...")
          