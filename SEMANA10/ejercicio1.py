class Estudiante():
    def __init__ (self, nombre, nota):
        self.nombre= nombre
        self.nota= nota

    def evaluar(self):
        if self.nota >=11:
            print("El estudiante: {}\nha sido aprobado".format(self.nombre))
        else:
            print("El estudiante {} NO ha aprobado".format(self.nombre))

perez = Estudiante('Fraven',20)
perez.evaluar()