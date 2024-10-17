# cantidad = int(input("ingrese la cantidad de producto"))
# valor= int(input("ingrese el valor del producto"))
# def funcion (valor, cantidad):
#     total=cantidad*valor
#     return total

# subtotal=0
# while cantidad !=0:
#     cantidad = int(input("ingrese la cantidad de producto"))
#     valor= int(input("ingrese el valor del producto"))
#     calculo=funcion(valor, cantidad)
#     subtotal=subtotal+calculo

# print(f"el total a pagar es{subtotal}")
clientes = []
def agregarclientes():
    nombre=input("Nombre ")
    apellido=input("Apellido ")
    edad=input("Edad ")
    telefono=input("Telefono ")
    cliente ={"nombre":nombre,
             "apellido": apellido,
             "edad":edad,
             "telefono":telefono}
    clientes.append(cliente)
    print("cliente agregado")

def verclientes():
    if not clientes:
        print("No hay clientes registrados.")
        return
    for idx, cliente in enumerate(clientes, start=1):
        print(f"{idx}. Nombre: {cliente["nombre"]}, Apellido: {cliente["apellido"]}, Edad: {cliente["edad"]}, Telefono: {cliente["telefono"]}")

def borrarclientes():
    verclientes()
    try:
        indice = int(input("Ingresa el número del cliente a borrar: ")) - 1
        if 0 <= indice < len(clientes):
            clientes.pop(indice)
            print("Cliente borrado con éxito.")
        else:
            print("Número de cliente inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def editarclientes():
    verclientes()
    try:
        indice = int(input("Ingresa el número del cliente a editar: ")) - 1
        if 0 <= indice < len(clientes):
            cliente = clientes[indice]
            print("Deja en blanco para mantener el dato actual.")
            cliente["nombre"] = input(f"Nombre [{cliente["nombre"]}]: ") or cliente["nombre"]
            cliente["apellido"] = input(f"Apellido [{cliente["apellido"]}]: ") or cliente["apellido"]
            cliente["edad"] = input(f"Edad [{cliente["edad"]}]: ") or cliente["edad"]
            cliente["telefono"] = input(f"Teléfono [{cliente["telefono"]}]: ") or cliente["telefono"]
            print("Cliente editado con éxito.")
        else:
            print("Número de cliente inválido.")
    except ValueError:
        print("Por favor, ingresa un número válido.")


def menu():
    while True:           
        print("Banco")
        print("ingrese 1 para agregar clientes")
        print("ingrese 2 para ver clientes")
        print("ingrese 3 para borrar clientes")
        print("ingrese 4 para editar clientes")
        opcion= int(input("ingresa la opcion"))
        if opcion == 1:
            agregarclientes()
        elif opcion == 2:
            verclientes()
        elif opcion == 3:
            borrarclientes()
        elif opcion == 4:
            editarclientes()
        else:
            print("opcion invalida")



menu()