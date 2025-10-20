color = "azul"
otro_color = "rojo"
num_1 = 12
num_2 = 13
usuario_activo = True
user = None
arr_1 = [1, 2, 3]

if num_1 > num_2 and color == "azul":
    print(num_1)

if color not in ["rojo"]:
    print(num_1)

if not usuario_activo:
    print("Usuario no activo")
else:
    print("Usuario activo")

if user is None:
    print("Usuario anónimo")

if user is not None:
    print("User loggeado")

if arr_1 is arr_1:
    print("Es el mismo array")

if 4 in arr_1:
    print("El 4 se encuentra")

if 5 not in arr_1:
    print("El 5 no se encuentra")