"""import random


class Persona:

    #1 _ es protegido, 2 __ es privado
    def __init__(self, nombre):
        self.__id = self.__generate_id()
        self.__nombre = nombre

    def __generate_id(self):
        return random.randint(10000,99999)



    @property #acceder a atributo sin necesidad de modificarlo
    def nombre_completo(self):
        return self.__nombre

    def get_nombre(self):
        return self.__nombre

    def get_id(self):
        return self.__id



    def __str__(self):
        return f"{self.__nombre} y el id es {self.get_id()}"

persona = Persona("Rodrigo")
print(persona.get_nombre())
print(persona.get_id())
print(persona)

print(persona.nombre_completo)"""
import dataclasses


@dataclasses.dataclass
class Producto:
    def __init__(self,nombre,cantidad,precio):
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

def get_nombre(self):
    return self.__nombre

def set_nombre(self,nombre):
    return self.__nombre

def get_cantidad(self):
    return self.__cantidad
def set_cantidad(self,cantidad):
    return self.__cantidad

def get_precio(self):
    return self.__precio

def set_precio(self):
    return self.__precio

def descuento(self, descuento):
    self.__precio -= descuento

def __str__(self):
    return f"{self.__nombre} cantidad {self.get_cantidad()}, precio {self.__precio()}"

presupuesto = 2200

p1 = Producto("TV", 3, 350)
p2 = Producto("PC Sobremesa", 1, 1900)

