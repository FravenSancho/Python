class Tomate():

    def origen(self):
        print('Peru')

    def color(self):
        print('Verde')

class Manzana():
    def origen(self):
        print('Venezuela')

    def color(self):
        print('Roja')

def funcion(objeto):
    objeto.origen() 
    objeto.color()

nuevo_tomate = Tomate()
funcion(nuevo_tomate)

nueva_manzana= Manzana()
funcion(nueva_manzana)


