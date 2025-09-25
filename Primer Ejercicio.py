nombre = "Rodrigo"
edad = 20
edadJosu = 20
altura = 1.90
list   = ["negro", "azul"]

edadUser = int(input("Edad: "))
if edadUser > edad:
    print("Eres mayor")
elif edad == edadUser:
    print("Tenemos la misma edad")
else:
    print("Eres menor")
