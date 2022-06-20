class Item():
    def __init__(self,name: str,price: float,quantity=0):
        # Run validations to the received arguments

        assert price >=0, f"Price {price} no es mayor que cero"
        assert quantity >=0, f"Quantity {quantity} no es mayor que cero"
        
        # Assign to self object
        self.price = price
        self.quantity = quantity
        

    def calcular_total_precio(self):
        return self.price * self.quantity

item1 = Item('Mouse',100,2)
item2 = Item('Perras',1000,3)

print(item1.calcular_total_precio())
print(item2.calcular_total_precio())