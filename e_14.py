class Alumno():
  def __init__(self, nombre, nota):
    self.nombre = nombre
    self.nota = nota

  def calcular_Nota(self):
    if self.nota >=11:
      print("El estudiante ha aprobado")
      
    else:
      print("Estudiante desaprobado")

alumno1 = Alumno('Fraven',15)
alumno1.calcular_Nota()
