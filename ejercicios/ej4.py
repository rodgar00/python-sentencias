"""
Construir un programa en Python que gestione un pequeño registro de personajes y equipos de Marvel.
    -   Crea un diccionario llamado marvel donde cada clave sea un nombre de un personaje y su valor sea otro
        diccionario.
    - El valor debe de tener los siguientes elementos:
        - alias -> nombre de superheroe.
        - team -> será un array unidimensional. Valores añadidos por consola. "Avengers", "X-men", ...
        - powers -> lista de poderes (array de strings)
        - isAvailable -> Si está disponible o no (True o False)
        - rating -> valoración del personaje 0.0 al 10.0 (float)

    Incluir al menos 3 personajes. Todos los datos se introducen de forma manual.

    - Mostrar todos los personajes introducidos.
    - Mostrar todos los nombres de los personajes que estén disponibles.
    - Buscar un personaje, comprobar si existe o no. Si existe, decir los poderes de ese personaje.
    - Decir que personaje es el que tiene más rating de todos los introducidos
        (Este ejercicio es complejo, No es obligatorio).
"""
marvel = {}

for i in range(1):
    nombreReal = input("Nombre real del personaje: ")
    alias = input("Alias: ")

    teamUser = input("Equipos (separados por coma): ")
    team = [t.strip() for t in teamUser.split(",")]

    powersUser = input("Poderes (separados por coma): ")
    powers = [p.strip() for p in powersUser.split(",")]

    disponible = int(input("¿Está disponible? (1 para disponible, 0 para no disponible): "))
    isAvailable = disponible == 1

    rating = float(input("Valoración del personaje (0.0 - 10.0): "))

    marvel[nombreReal] = {
        "alias": alias,
        "team": team,
        "powers": powers,
        "isAvailable": isAvailable,
        "rating": rating
    }

print("\nLista completa de personajes")
for clave, valor in marvel.items():
    print(f"{clave}, {valor}")

print("\nPersonajes disponibles")
for nombre, datos in marvel.items():
    if datos["isAvailable"]:
        print(f"{nombre} (Alias: {datos['alias']})")
