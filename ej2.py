# Crea diccionario person con
# name age height, color array, animales array vacio y location
# Pide por consola color y lo añades a colors.
# Sustituye el primer color de la lista por black
# Pide por consola mascota (name, type) y añadelo como diccionario a lista
# for para info por consola
# mostrar por pantalla pets y muestre: La "clave" es "valor" para cada mascota

person = {
    "name": "Rodrigo",
    "age": 20,
    "height": 190,
    "colors": ["orange", "yellow", "green", "blue"],
    "animales": [],
    "location": (12, 24)
}

colorUser = input("Ingresa el color a añadir: ")
person["colors"].append(colorUser)

print("\nInformación de la persona:")
for clave, valor in person.items():
    print(clave, valor)

person["colors"][0] = "black"

for i in range(3):
    print(f"\nMascota {i+1}:")
    mascotaNameUser = input("Ingresa el nombre de la mascota: ")
    mascotaTypeUser = input("Ingresa el tipo de mascota: ")
    mascota = {
        "name": mascotaNameUser,
        "type": mascotaTypeUser
    }
    person["animales"].append(mascota)

print("\nLista de mascotas:")
for mascota in person["animales"]:
    for clave, valor in mascota.items():
        print(f'La clave "{clave}" es "{valor}"')
    print()
