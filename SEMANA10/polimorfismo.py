class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):

    def hablar(self):
        print("Yo no hablo")

class Pez(Animales):
    def hablar(self):
        print("Yo no hablo, soy un pez")

perro = Perro("Guau!")
perro.hablar()

animal = Animales("Miau")
animal.hablar()

pez = Pez("xdxd")
pez.hablar()

animal = Pez("perrra")
animal.hablar()