

biblioteca = {

}

for _ in range(3):
    tituloUser = input("Introduce el título del libro -> ")
    autor = input("Introduce el nombre del autor -> ")

    disponibilidad = input("¿Está disponible? (1 para Sí, 0 para No) -> ")
    while disponibilidad != "0" and disponibilidad != "1":
        print("Por favor, introduce 1 o 0.")
        disponibilidad = input("¿Está disponible? (1 para Sí, 0 para No) -> ")

    if disponibilidad == "1":
        disponible = True
    else:
        disponible = False

    valorDicc = {
        "autor": autor,
        "disponible": disponible
    }
    biblioteca[tituloUser] = valorDicc

print("\nBuscar libros")
libro_buscar = input("Introduce el título del libro que quieres buscar: ")

if libro_buscar in biblioteca:
    print(f"\nEl libro '{libro_buscar}' está en la biblioteca.")
    if biblioteca[libro_buscar]["disponible"]:
        print("Y está disponible.")
    else:
        print("Pero no está disponible.")
else:
    print("El libro no existe en la biblio.")

print("\nContenido completo de la biblioteca:")
for titulo, info in biblioteca.items():
    if info["disponible"]:
        estado = "Disponible"
    else:
        estado = "No disponible"
    print("- " + titulo + ": Autor: " + info["autor"] + ", Estado: " + estado)
