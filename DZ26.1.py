class Animal:
    def __init__(self, name, shout):
        self.name = name
        self.shout = shout
        print('Имя:', self.name, 'Звук:', self.shout)

class Dog(Animal):
    dg = Animal('Bobik', 'Woof')
    

class Cat(Animal):
    cat = Animal('Lissa', 'Meow')
    
    