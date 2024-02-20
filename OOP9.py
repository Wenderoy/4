class Kolesa:
    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

class Dvigatel:
    def __init__(self, power):
        self.power = power

class Dveri:
    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

# Класс "Автомобиль" наследует свойства от классов "Колеса", "Двигатель", "Двери"
class Avtomobil(Kolesa, Dvigatel, Dveri):
    def __init__(self, number_of_wheels, power, number_of_doors, brand):
        Kolesa.__init__(self, number_of_wheels)
        Dvigatel.__init__(self, power)
        Dveri.__init__(self, number_of_doors)
        self.brand = brand

    def info(self):
        print(f"Марка: {self.brand}")
        print(f"Количество колес: {self.number_of_wheels}")
        print(f"Мощность двигателя: {self.power} л.с.")
        print(f"Количество дверей: {self.number_of_doors}")

# Создание экземпляра класса "Автомобиль"
my_car = Avtomobil(number_of_wheels=4, power=150, number_of_doors=4, brand="Toyota")
my_car.info()