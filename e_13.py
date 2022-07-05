class Vehiculo():

  def __init__(self, color, ruedas, puertas):
    self.color = color
    self.ruedas = ruedas
    self.puertas = puertas

  def __str__(self):
    return "Color : {}\nN° de Ruedas: {}\nN° de Puertas: {}".format(self.color, self.ruedas, self.puertas)

class Coche(Vehiculo):
  
  def __init__(self, velocidad, cilindrada, color, ruedas, puertas):
    super().__init__(color, ruedas, puertas)

    self.velocidad = velocidad
    self.cilindrada = cilindrada

  def __str__(self):
    return "Color : {}\nN° de Ruedas: {}\nN° de Puertas: {}\nVelocidad km/h: {}\nTanque: {}".format(self.color, self.ruedas, self.puertas, self.velocidad, self.cilindrada)

prueba = Coche(500,40,'rojo',4,4)
print(prueba)
