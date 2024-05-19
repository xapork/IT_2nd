class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def change_quantity(self, amount):
        if self.quantity + amount >= 0:
            self.quantity += amount
        else:
            print("Ошибка: Недостаточное количество товара.")

    def calculate_total_price(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantity}, total_price={self.calculate_total_price()})"

product1 = Product("john lennon", 8, 40)
product1.change_quantity(30)
print(product1.calculate_total_price())  
print(product1)  