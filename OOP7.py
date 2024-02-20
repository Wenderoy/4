import math

class Kvadrat:
    def __init__ (self, side_length):
        self.side_length = side_length
        
    def area(self):
        return self.side_length ** 2
    
    
class Okruzhnost:
    def __init__ (self, radius):
        self.radius = radius
        
    def area2 (self):
        return math.pi * self.radius ** 2
    

class OkruzhnostVKvadrate(Kvadrat, Okruzhnost):
    def __init__(self, side_length):
        Kvadrat.__init__(self, side_length)
        Okruzhnost.__init__(self, side_length / 2) # половина стороны квадрата
        
    
    def info(self):
        print(f'Сторона квадрата: {self.side_length}')
        print(f'Площадь квадрата: {self.area():.2f}')
        print(f'Радиус окружности: {self.radius}')
        print(f'Площадь окружности {self.area2():.2f}')
        
        
kvadrat1 = Kvadrat(20)
okruzhnost1 = Okruzhnost(30)
okruzhnostvkvadrate = OkruzhnostVKvadrate(50)
OkruzhnostVKvadrate.info()