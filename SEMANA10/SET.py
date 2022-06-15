class A():
    def __init__(self):
        self._cuenta = 0
        self._contador = 0

    #decorador
    #metodo que llama al atributo
    @property
    def cuenta(self):
        return self._cuenta

    @cuenta.setter
    #metodo que modifique el atributo
    def cuenta(self, cuenta):
        self._cuenta = cuenta    

    @property
    def contador(self):
        return self._contador

    @contador.setter
    def contador(self, contador):
        self._contador = contador

a = A()
a.contador = 26
print(a.contador)
print(a.cuenta)
