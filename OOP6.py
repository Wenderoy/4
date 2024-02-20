class Vehicle:
    
    def _init_(self, brand):
        self._brand = brand  # защищенный атрибут

class Car(Vehicle):
    def _init_(self, brand, model):
        super()._init_(brand)
        self.model = model

car = Car("Toyota", "Corolla")

# Доступ к защищенному атрибуту через наследование
print(car._brand)  # Toyota


print('=======================================================================')


class Calculator:
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# Использование статических методов
print(Calculator.add(5, 3))  # Вывод: 8
print(Calculator.multiply(4, 6))  # Вывод: 24


print('=======================================================================')



