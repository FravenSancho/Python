from archivos import f

class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def imprimir(self):
        return "El auto es de color: {}\nTiene una cantidad de ruedas: {}".format(self.color,self.ruedas)

cliente1 = Vehiculo("Rojo","4")
print(cliente1.imprimir())

f = open('testarchive.txt','r')
print(f.read())
