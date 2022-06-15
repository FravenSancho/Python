class Animales():

    def habla(self):
        print("Yo soy un Animal")

    def descripcion(self):
        print("Yo soy un {}".format(self.animal))

class Perro(Animales):
    pass

class Abeja(Animales):
    
    def __init__(self, animal):
        self.animal = animal

animal = Animales()
animal.habla()

perro = Perro()
perro.habla()

abeja = Abeja("Abeja")
animal.descripcion()
