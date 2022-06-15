# Realizar un programa en el cual se 
# declaren dos valores enteros por 
# teclado utilizando el método __init__.
# Calcular después la suma, resta, multiplicación y división.
# Utilizar un método para cada una 
# e imprimir los resultados obtenidos.
# Llamar a la clase Calculadora.

class Calculadora():
    def __init__(self):
        self.num1 = (int(input("num1: ")))
        self.num2 = (int(input("num2: ")))

    def suma(self):
        self.resultado =self.num1+self.num2
        print("La suma es: ",self.resultado)
   
    def mult(self):
        self.resultado =self.num1*self.num2
        print("La multiplicación es: ",self.resultado)

    def div(self):
        self.resultado =self.num1/self.num2
        print("La división es: ",self.resultado)

prueba1=Calculadora()
prueba1.suma()
prueba1.mult()
prueba1.div()
