class FabricaTelefonos():
    def __init__(self, marca,color):
        self.marca=marca
        self.color=color

    def __del__(self):
        pass
telefono = FabricaTelefonos("Nokia","Negro")
print(telefono.marca)
