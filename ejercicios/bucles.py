palabra = "Hola mundo"
arr_1 = [1,2,3,4,5]

for letra in palabra:
    print(letra)

for elemento in arr_1:
    print(elemento)

for n in range(10):
    print(n)

for j in range(10, 0, -2):
    print(n)

arr_2 = [k for k in range(10)]

arr_3 = []
for z in range(10):
    arr_3.append(z)

print(arr_2)
print(arr_3)

print()
for x in arr_2:
    if x % 2 == 0:
        print(x)

salir = False
cont = 0
# while not salir and cont < len(arr_2):
#     if arr_2[cont] == 4:
#         salir = True
#     cont += 1

while not salir and cont < len(arr_2):
    if arr_2[cont] % 2 == 0:
        salir = True
        cont += 1

dict_1: dict = {
    "nombre": "Rodrigo",
    "apellido": "Garcia"
    "email": "rodrigogarciaperez00@gmail.com",
}

for clave in dict_1:
    print(clave, ", ", dict_1[clave])

print()
for clave, valor in dict_1.items():
    print(clave, ": ", valor)

print()
for clave in dict_1.keys():
    print(clave, ": ", dict_1[clave])

print()
for valor in dict_1.values():