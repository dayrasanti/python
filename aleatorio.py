# import random
# print(random.randint(3,9))
# print(random.choice([2,4,7,9,0,3]))
import random
print('Nombre')
Nombre = input()
numero = random.randint(1, 20)
print(Nombre + ', estoy pensando en un número entre 1 y 20.')
while True:
    valor = input()
    valor = int(valor)
    if valor < numero:
        print("frio")
    if valor> numero:
        print("muy caliente")
    if valor == numero:
        break
if valor == numero:
    print('¡Bien, ' + Nombre + '! ¡Has adivinado!')



