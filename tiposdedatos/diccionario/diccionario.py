# cliente={
#     "nombre":"Jorge",
#     "apellido":"rodrigez",
#     "edad":"30",
#     "telefono":"321876590",
#     "saldo":"5000"
# }
# print(cliente)
# valor = cliente.get("nombre")
# print(valor)
# cliente["email"] = "jorge.rodrigez@example.com"
# cliente["profesion"] = "ingeniero"
# print(cliente)
# print(cliente["telefono"])
# del cliente["email"]
# claves = cliente.keys()
# print(cliente.keys())
# print(cliente.values())

redes={}
def menu():
    while True:           
        print("Banco")
        print("ingrese 1 para agregar una red")
        print("ingrese 2 para ver la red")
        
        opcion= int(input("ingresa la opcion"))
        if opcion == '1':
           print("opcion invalida")
        elif opcion == '2':
            print("opcion invalida")
        else:
            print("opcion invalida")
def agregarclientes():
    red=input("Nombre de red ")
    clave=input("clave ")
    redes.append(redes)
    print("clave agregado")
menu()