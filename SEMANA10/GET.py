
class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    #metodo para llamar al atributo cuenta
    #decorador
    @property
    def cuenta(self):
        return self._cuenta

    #metodo para llamar al atributo contador
    @property
    def contador(self):
        return self._contador

a = A()
print(a.cuenta)

print(a.contador)
