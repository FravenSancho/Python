#usar pelomorfimos cuando se manejan mas de 2 clases

class Colombia():
    
    def capital(self):
        print('Bogota')

    def idioma(self):
        print('Español')

class Peru():

    def capital(self):
        print('Lima')

    def idioma(self):
        print('Quechua')

peruano = Peru()
colombiano = Colombia()
for pais in (peruano,colombiano):
    pais.capital()
    pais.idioma()

print("###########################")
#POLIMORFISMO CON HERENCIA
class Aves():
    def volar(self):
        print("Las aves vuelan")


class Aguila(Aves):
    def volar(self):
        print("Las aguilas pueden volar y son carroñeras")

class Gallina(Aves):
    def volar(self):
        print("Las gallinas no pueden volar")

#llamando objetos
primera_ave=Aves()
primera_aguila= Aguila()
primera_gallina = Gallina()


#llamando metodos
primera_ave.volar()
primera_aguila.volar()
primera_gallina.volar()

print("#############################################")

class Cliente:
    def __init__(self):
        self.__codigo = 4321

    def __cuenta(self):
        print("Cuenta de procesamiento")

    def getcodigo(self):
        return self.__codigo

persona = Cliente()

print(persona._Cliente__codigo)

###################################################

class Perras():

    
    def __init__(self):
        self.__hembra=4

perras1 = Perras()
print(perras1.__hembra)

# class A():
#     def __init__(self):
#         self._cuenta = 0
#         self._contador = 0

#     #metodo para llamar al atributo cuenta
#     #decorador
#     @property
#     def cuenta(self):
#         return self._cuenta

#     #metodo para llamar al atributo contador
#     @property
#     def contador(self):
#         return self._contador

# a = A()
# print(a.cuenta)

# print(a.contador)

    