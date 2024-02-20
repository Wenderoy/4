class Transport:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
    def beep(self):
        print('beep')
        
        
class Car(Transport):
    def __init__(self, speed, color, owner):
        super().__init__(speed, color)
        self.owner = owner
        
    def say_owner(self):
        print(f'Владелец машины: {self.owner}')
    
    def beep(self):
        print('beep beep')
            
car1 = Car(100, 'yellow', 'Василий')
print(car1.speed)
print(car1.color)
print(car1.owner)
car1.beep()
car1.say_owner()


class Bus(Transport):
    def __init__(self, speed, color, seeds):
        super().__init__(speed, color)
        self.seeds = seeds
    def say_seeds(self):
        print(f'Количество мест: {self.seeds}')
        
        
bus1 = Bus(60, 'blue', 40)
bus1.say_seeds()


class SportCar(Car, Transport):
    pass

car1 = SportCar(100, 'yellow', 'Иван')
car1.beep()
car1.say_owner()


class Tractor(Transport):
    def __init__(self, speed, color, owner, weight):
        super().__init__(speed, color)
        self.owner = owner
        self.weight = weight
    def say_weight(self):
        print(f'Вес: {self.weight} кг')
        
tractor1 = Tractor(80, 'green', 'Василий', 1000)
print('скорость:', tractor1.speed)
print('цвет:', tractor1.color)
print('Владелец:', tractor1.owner)
tractor1.beep()
tractor1.say_weight()



class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def say_name(self):
        print(f'Имя: {self.name}')
    def say_age(self):
        print(f'Возраст: {self.age}')
    def say_height(self):
        print(f'Рост: {self.height}')
        
human1 = Human('Василий', 20, 180)
human1.say_name()
human1.say_age()
human1.say_height()



class Pupil(Human):
    def __init__(self, name, age, height, school):
        self.name = name
        self.age = age
        self.height = height
        self.school = school
    def say_school(self):
        print(f'Школа: {self.school}')
        
pupil1 = Pupil('Василий', 20, 180, 'Московский Государственный Университет')
pupil1.weight = 70

print('Имя:', pupil1.name)
print('Возраст:', pupil1.age)
print('Рост:', pupil1.height)
print('Школа:', pupil1.school)




class Salesman(Human):
    def __init__(self, name, age, height, sales, buyers):
        self.name = name
        self.age = age
        self.height = height
        self.sales = sales
        self.buyers = buyers
    def say_sales(self):
        print(f"Продажи: {self.sales}")
        
        
        
salesman1 = Salesman('Иван', 20, 180, 50, 100)

print('Кол-во продаж:')
salesman1.say_sales()
print('Кол-во покупателей:', salesman1.buyers)
print('Имя:', salesman1.name)
print('Возраст:', salesman1.age)
print('Рост:', salesman1.height)




class PrimaryPupil(Pupil):
    def __init__(self, name, age, height, school):
        super().__init__(name, age, height, school)
    def say_primary(self):
        print ('Я учусь в младших группах')
        
        
        
prpupil1 = PrimaryPupil('Василий', 20, 180, 'Московский Государственный Университет')


print('Имя:', prpupil1.name)
print('Возраст:', prpupil1.age)
print('Рост:', prpupil1.height)
print('Школа:', prpupil1.school)
prpupil1.say_primary()