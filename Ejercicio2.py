import csv

class Sabor:
    def __init__(self, id, nombre, ingredientes):
        self.id = id
        self.nombre = nombre
        self.ingredientes = ingredientes

class ManejaSabores:
    def __init__(self):
        self.sabores = []

    def cargar_sabores(self, archivo):
        with open("C:\\Users\\santi\\OneDrive\\Escritorio\\UNIDADES POO\\Archivos csv\\Ejercicio2\\sabores.csv") as file:
            reader = csv.reader(file, delimiter=";")
            for i in reader:
                id = i[0]
                nombre = i[1]
                ingredientes= i[2]
                sabor = Sabor(id, nombre, ingredientes)
                self.sabores.append(sabor)

class Helado:
    def __init__(self, tipo):
        self.tipo = tipo
        self.sabores = []

    def agregar_sabor(self, sabor):
        self.sabores.append(sabor)

class ManejaHelados:
    def __init__(self):
        self.helados = []

    def registrar_helado(self, helado):
        self.helados.append(helado)

    def obtener_sabores_mas_pedidos(self):
        sabores_contador = {}
        for helado in self.helados:
            for sabor in helado.sabores:
                if sabor.nombre in sabores_contador:
                    sabores_contador[sabor.nombre] += 1
                else:
                    sabores_contador[sabor.nombre] = 1
        
        sabores_mas_pedidos = sorted(sabores_contador, key=sabores_contador.get, reverse=True)[:5]
        return sabores_mas_pedidos

    def obtener_gramos_vendidos(self, num_sabor):
        gramos_vendidos = 0
        for helado in self.helados:
            for sabor in helado.sabores:
                if sabor.id == num_sabor:
                    cantidad_sabores = len(helado.sabores)
                    gramos_vendidos += helado.tipo // cantidad_sabores
                    break

        return gramos_vendidos

    def obtener_sabores_por_tipo(self, tipo):
        sabores_vendidos = []
        for helado in self.helados:
            if helado.tipo == tipo:
                for sabor in helado.sabores:
                    sabores_vendidos.append(sabor.nombre)

        return sabores_vendidos

    def obtener_recaudacion_por_tipo(self):
        recaudacion_por_tipo = {}
        for helado in self.helados:
            if helado.tipo in recaudacion_por_tipo:
                recaudacion_por_tipo[helado.tipo] += helado.tipo
            else:
                recaudacion_por_tipo[helado.tipo] = helado.tipo

        return recaudacion_por_tipo


def cargar_datos_sabores(maneja_sabores):
    maneja_sabores.cargar_sabores('sabores.csv')
    print("¡Datos de sabores cargados exitosamente!")


def registrar_helado(maneja_sabores, maneja_helados):
    print("Registrar un helado vendido:")

    tipos_helado = {1: "Pequeño", 2: "Mediano", 3: "Grande"}

    tipo_helado = int(input("Ingrese el tipo de helado (1: Pequeño, 2: Mediano, 3: Grande): "))
    if tipo_helado not in tipos_helado:
        print("Tipo de helado inválido.")
        return

    helado = Helado(tipos_helado[tipo_helado])

    print("Seleccione los sabores del helado (ingrese el número de sabor):")
    for i, sabor in enumerate(maneja_sabores.sabores):
        print(f"{i + 1}. {sabor.nombre}")

    while True:
        num_sabor = int(input("Ingrese el número de sabor (0 para finalizar): "))
        if num_sabor == 0:
            break
        elif num_sabor < 1 or num_sabor > len(maneja_sabores.sabores):
            print("Número de sabor inválido.")
        else:
            sabor_seleccionado = maneja_sabores.sabores[num_sabor - 1]
            helado.agregar_sabor(sabor_seleccionado)

    maneja_helados.registrar_helado(helado)
    print("Helado registrado exitosamente!")


def mostrar_sabores_mas_pedidos(maneja_helados):
    sabores_mas_pedidos = maneja_helados.obtener_sabores_mas_pedidos()
    print("Los 5 sabores de helado más pedidos son:")
    for i, sabor in enumerate(sabores_mas_pedidos, start=1):
        print(f"{i}. {sabor}")


def estimar_gramos_vendidos(maneja_helados):
    num_sabor = int(input("Ingrese el número de sabor para estimar los gramos vendidos: "))
    gramos_vendidos = maneja_helados.obtener_gramos_vendidos(num_sabor)
    print(f"Se estima que se han vendido {gramos_vendidos} gramos de ese sabor.")


def mostrar_sabores_por_tipo(maneja_helados):
    tipos_helado = {1: "Pequeño", 2: "Mediano", 3: "Grande"}

    tipo_helado = int(input("Ingrese el tipo de helado (1: Pequeño, 2: Mediano, 3: Grande): "))
    if tipo_helado not in tipos_helado:
        print("Tipo de helado inválido.")
        return

    sabores_vendidos = maneja_helados.obtener_sabores_por_tipo(tipos_helado[tipo_helado])
    print(f"Los sabores vendidos en helados de tipo {tipos_helado[tipo_helado]} son:")
    for i, sabor in enumerate(sabores_vendidos, start=1):
        print(f"{i}. {sabor}")


def mostrar_recaudacion_por_tipo(maneja_helados):
    recaudacion_por_tipo = maneja_helados.obtener_recaudacion_por_tipo()
    print("Recaudación por tipo de helado:")
    for tipo, recaudacion in recaudacion_por_tipo.items():
        print(f"{tipo}: {recaudacion}")


def mostrar_menu():
    print("======= Heladería ========")
    print("1. Cargar datos de sabores")
    print("2. Registrar un helado vendido")
    print("3. Mostrar los 5 sabores de helado más pedidos")
    print("4. Estimar gramos vendidos de un sabor")
    print("5. Mostrar sabores vendidos por tipo de helado")
    print("6. Mostrar recaudación por tipo de helado")
    print("0. Salir")
    print("==========================")

    while True:
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            cargar_datos_sabores(maneja_sabores)
        elif opcion == "2":
            registrar_helado(maneja_sabores, maneja_helados)
        elif opcion == "3":
            mostrar_sabores_mas_pedidos(maneja_helados)
        elif opcion == "4":
            estimar_gramos_vendidos(maneja_helados)
        elif opcion == "5":
            mostrar_sabores_por_tipo(maneja_helados)
        elif opcion == "6":
            mostrar_recaudacion_por_tipo(maneja_helados)
        elif opcion == "0":
            print("¡Gracias por usar la aplicación!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")




if __name__ == "__main__":
    maneja_sabores = ManejaSabores()
    maneja_helados = ManejaHelados()
    mostrar_menu()