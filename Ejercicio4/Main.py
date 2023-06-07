from ManejadorEmpleadoC import ManejadorEmpleadoC
from ManejadorEmpleadoE import ManejadorEmpleadoE
from ManejadorEmpleadoP import ManejadorEmpleadoP
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

    