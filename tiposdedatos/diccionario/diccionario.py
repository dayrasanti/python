cliente={
    "nombre":"Jorge",
    "apellido":"rodrigez",
    "edad":"30",
    "telefono":"321876590",
    "saldo":"5000"
}
print(cliente)
valor = cliente.get("nombre")
print(valor)
cliente["email"] = "jorge.rodrigez@example.com"
cliente["profesion"] = "ingeniero"
print(cliente)
print(cliente["telefono"])
del cliente["email"]
claves = cliente.keys()
print(cliente.keys())
print(cliente.values())