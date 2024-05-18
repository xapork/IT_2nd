class Soda:
    def __init__(self, dobavka=None):
        self.dobavka = dobavka

    def show_my_drink(self):
        return f'Газировка и {self.dobavka}' if self.dobavka else 'Обычная газировка'

cola = Soda('')
print(cola.show_my_drink())