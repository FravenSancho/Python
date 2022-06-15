class Auto():
    rueda = 4

    def desplazamiento(self):
        print('El auto esta en movimiento')

class Moto():

    rueda = 2
    def desplazamiento(self):
        print('La moto esta en movimiento')

class Animales():
    def __init__(self, nombre):
        self.nombre = nombre

    def tipo_animal(self):
        pass

class Leon(Animales):
    
    def tipo_animal(self):
        print('Animal Salvaje')

class Perro(Animales):

    def tipo_animal(self):
        print('Animal doméstico')

nuevo_animal = Leon('SIMBA')
nuevo_animal.tipo_animal()

nuevaoanimal2 = Perro('REX')
nuevaoanimal2.tipo_animal()


perras = Auto()
perras.desplazamiento()

zorras = Moto()
zorras.desplazamiento()