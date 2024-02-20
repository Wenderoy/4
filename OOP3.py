# def get_name(name='Иван'):
#     print(name)
    

# get_name()
# get_name('Петр')



# class Car:
#     def __init__(self, speed, color='Yellow'):
#         self.speed = speed
#         self.color = color
        
# car1 = Car(100)
# car2 = Car(90, 'Blue')
# print(f'{car1.color}')
# print(f'{car2.color}')


# class Car:
#     def __init__(self, speed, color='Yellow', owner = None) -> None:
#         self.speed = speed
#         self.color = color
#         self.owner = owner
        
#     def say_owner(self):
#         if self.owner:
#             print(f'Владелец машины: {self.owner}, цвет машины: {self.color}')
#         else:
#             print('Владелец неизвестен')
            
            
# car1 = Car(100, 'green', 'Иван')
# car2 = Car(90, 'Blue')
# car1.say_owner()
# car2.say_owner()
# car3 = Car(80, 'Yellow', 'Иван')
# car3.say_owner()


# class Person:
#     _age = 15
#     def __say_hello():
#         print('Привет')
    
# person1 = Person
# print(person1._age)
# person1._age = 20
# print(person1._age)
# # person1.__say_hello()

# person1._Person__say_hello()


class MyClass:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
a = MyClass('Иван')

a.name = 'Сергей'
print(a.name)



# class Loch_Ness_Monster:
#     _age = 150
#     def __init__(self, height, weight, name='Лохнесский Монстр'):
#         self.height = height
#         self.weight = weight
#         self.name = name
        
#     def shout(self):
#         print('Кви Кви Кви!')
        

# monster = Loch_Ness_Monster(150, 200, 'Лохнесский Монстр')
# print('Возраст Лохнесского чудовища:', monster._age)
# print('Вес лохнесского чудовища:', monster.weight)
# print('Рост лохнесского чудовища:', monster.height)
# monster.shout()



# class Parent:
#     def say_hello():
#         print('Привет, я метод родительского класса')
        

# class Children(Parent):
#     def say_hello():
#         print('Привет, я метод дочернего класса')
        
# child = Children
# child.say_hello()



# class Test(list):
#     def append(self, object) -> None:
#         for i in range(len(self)):
#             self[i] **= object
        
        
# a = Test([1, 2, 3])
# print(a)
# a.append(2)
# print(a)



class Test(int):
    def __init__ (self, num) -> None:
        super().__init__()
        self.num = num
    def __add__ (self, num2):
        return self.num * num2
    
a = Test(13.4)
print(a + 10)