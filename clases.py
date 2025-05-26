class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def emitir_sonido(self):
        print("Este animal hace un sonido")


class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def emitir_sonido(self):
        print("Guau Guau")


class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def emitir_sonido(self):
        print("Miau")

class Pajaro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

    def emitir_sonido(self):
        print("Pío pío")

def hacer_emitir_sonido(animales: list):
    for animal in animales:
        animal.emitir_sonido()

if __name__ == "__main__":
    perro1 = Perro("Fido", 5)
    gato1 = Gato("Whiskers", 3)
    pajaro1 = Pajaro("Tweety", 1)
    animal_generico = Animal("Desconocido", 2)

    print("--- Demostración individual de sonidos ---")
    perro1.emitir_sonido()
    gato1.emitir_sonido()
    pajaro1.emitir_sonido()
    animal_generico.emitir_sonido()
    print("\n")

    print("--- Demostración de polimorfismo con hacer_emitir_sonido ---")
    lista_de_animales = [perro1, gato1, pajaro1, animal_generico]
    hacer_emitir_sonido(lista_de_animales)