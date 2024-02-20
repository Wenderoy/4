class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year
        
print('Car:')
car1 = Car('red', 'bmw', 2020)
print(car1.color, car1.model, car1.year)



class Wardrobe:
    color = 'brown'
    height = 200
    width = 1000
    
print('Wardrobe:')
print(Wardrobe.color)
print(Wardrobe.height)
print(Wardrobe.width)



class Telephone:
    def __init__(self, color, model, width, height):
        self.color = color
        self.model = model
        self.width = width
        self.height = height
        
    def pr(self):
        print(self.color, self.model, self.width, self.height)
        
        
telephone1 = Telephone('black', 'samsung', 100, 200)

telephone1.pr()


class Android:
    def __init__(self, power, version):
        self.power = power
        self.version = version

    def ret(self):
        return ('Android', self.version, self.power)
    
    
android1 = Android('9.0', '100%')
    
print(android1.ret())