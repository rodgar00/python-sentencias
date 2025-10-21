from clases.Student import Student

estudiantes = []

salir = False
while not salir:
    nombre = input("s para salir.\nIngrese su nombre: ")
    if nombre != "s":
        try:
            estudiante = Student(nombre)
            estudiantes.append(estudiante)
        except ValueError as e:
            print(e)
    else:salir = True
    print()
for estudiante in estudiantes:
    print(estudiante)