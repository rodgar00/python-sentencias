arr_1 = [10,20,30]
frutas: list[str] = ["manzana", "pera", "uva"]

for numero in arr_1:
    print(numero)

print()

for fruta in frutas:
    print(fruta)


frutas.append("mango")


for fruta in frutas:
    print(frutas)

frutas.pop() # Eliminamos último elemento de la lista si no ponemos nada
print()
for fruta in frutas:
    print(frutas)

frutas.pop(0)
print()
for fruta in frutas:
    print(frutas)

frutas.insert(0, "banana")
frutas.insert(2, "sandia")
for fruta in frutas:
    print(frutas)
print()

print(frutas[1])

frutas.remove("uva")


for fruta in frutas:
    print(frutas)
print()

frutas.sort()
for fruta in frutas:
    print(frutas)
print()


print(frutas.count("banana"))


print(f"Hay {frutas.count("banana")} bananas en frutas")

