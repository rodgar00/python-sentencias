import random

class Student():
    def __init__(self, name):
        if not name or name.isnumeric():
            raise ValueError("El nombre no puede estar vacío ni ser numérico.")
        self.__name = name
        self.__grades = []
        self.__id = self.__generate_id()

    def __generate_id(self):
        return random.randint(10000, 99999)

    def add_grade(self, nota):
        if not isinstance(nota, (int, float)):
            raise TypeError("La nota debe ser un número.")
        if nota < 0 or nota > 10:
            raise ValueError("La nota debe estar entre 0 y 10.")
        self.__grades.append(nota)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if not name or name.isnumeric():
            raise ValueError("El nombre no puede estar vacío ni ser numérico.")
        self.__name = name

    @property
    def media(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def __str__(self):
        return f"[ID: {self.__id}] {self.__name} -> Notas: {self.__grades} | Media: {self.media:.2f}"


