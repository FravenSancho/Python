class B():
    def __init__(self):
        self.__contador = 0

    def incrementar(self):
        self.__contador +=1

    def cuenta(self):
        return self.__contador


b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())