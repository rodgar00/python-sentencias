persona = {
    "nombre": "Rodrigo",
    "apellido": "García",
    "esEstudiante": True,
    "frutas": ["manzana", "pera"],
    "animales": [{"animal1": "perro"}, {"animal2": "gato"}]
}

print(persona["nombre"])

if persona["esEstudiante"]:
    print("Es estudiante")
else:
    print("Es profesor")

for fruta in persona["frutas"]:
    print(fruta)


# print(persona["estaDeVacaciones", "No está definido"])

estaDeVacaciones = persona.get("estaDeVacaciones", False)

print(estaDeVacaciones)

persona.pop("esEstudiante") # borramos clave-valor del diccionario
print(persona)

del persona["frutas"]

print(persona)

# persona.clear()
# print(persona)

for clave, valor in persona.items():
    print(f"La clave es {clave} y su valor es {valor}")

for clave, valor in persona.items():
    print(clave, valor)

persona["esEstudiante"] = False
print()

for values in persona.values():
    print(values)
print()

for clave in persona.keys():
    print(clave)


for elemento in persona["animales"]:
    for clave, valor in elemento.items():
        print(f"La clave es {clave} y el valor {valor}")

clave_consola = int(input("Ingresa la clave: "))
valor_consola = bool(input("Ingresa la valor: "))
persona[clave_consola] = valor_consola
print()
print(persona)