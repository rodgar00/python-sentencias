import random

class Student:
    def __init__(self, name):
        if not name or name.isnumeric():
            raise ValueError("El nombre no puede estar vacío ni ser numérico.")
        self.__name = name
        self.__grades = []
        self.__id = self.__generate_id()
        self.add_grade()

    @staticmethod
    def __generate_id():
        return random.randint(10000, 99999)

    def add_grade(self, nota=None):
        val = True
        while val:
            if nota is None:
                entrada = input(f"Ingrese una nota para {self.__name} (o -1 para acabar): ")
                if entrada == "-1":
                    val = False
                else:
                    try:
                        nota = float(entrada)
                    except ValueError:
                        print("La nota debe ser un número.")
                        nota = None

            if nota is not None:
                if not isinstance(nota, (int, float)):
                    print("La nota debe ser un número.")
                    nota = None
                elif nota < 0 or nota > 10:
                    print("La nota debe estar entre 0 y 10.")
                    nota = None
                else:
                    self.__grades.append(nota)
                    nota = None

            if nota is None and not val:
                val = False

    @property
    def nombre(self):
        return self.__name

    @property
    def media(self):
        if not self.__grades:
            return 0
        return sum(self.__grades) / len(self.__grades)

    def __str__(self):
        return f"[ID: {self.__id}] {self.__name} -> Notas: {self.__grades} | Media: {self.media:.2f}"
