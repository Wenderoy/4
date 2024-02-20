import math
from pyexpat import model
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def say_length(self):
#         print(f'Длина круга:', self.radius * math.pi * 2)
        
#     def say_area(self):
#         print(f'Площадь круга:', (self.radius ** 2) * math.pi)
        
        

# new_circle = Circle(10)
# new_circle.say_length()
# new_circle.say_area()


# --------------------------------------------------------------------------


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def display_info(self):
#         print('Имя:', self.name)
#         print('Возраст:', self.age)
    
# class Employee(Person):
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def display_salary(self):
#        print('Зарплата человека:', self.salary)
       
       
# p1 = Employee('Иван', 20, 100000)
# p1.display_info()
# p1.display_salary()


# --------------------------------------------------------------------------

# class Shape:
    
#     def calculate_area(self):
#         pass       
     
# class Rectangle(Shape):

#     side_length1 = 2
#     side_length2 = 2
    
#     def calculate_area(self):
#         return self.side_length1 * self.side_length2
    
# class Circle(Shape):
#     pi = math.pi
#     rad = 10
        
#     def calculate_area(self):
#         return self.pi * (self.rad ** 2)

# def get_area(input_obj):
#     print(input_obj.calculate_area())

# shape_obj = Shape()
# rectangle_obj = Rectangle()
# circle_obj = Circle()


# get_area(shape_obj)
# get_area(rectangle_obj)
# get_area(circle_obj)

# --------------------------------------------------------------------------



# class Car:
#     def __init__(self, brand, model, speed):
#         self.__brand = 'BMW'
#         self.__model = 'M8'
#         self.__speed = '140 km/h'
    
#     def get_brand(self):
#         return self.__brand
    
#     def set_brand(self, brand):
#         self.__brand = brand
        
#     def get_model(self):
#         return self.__model
    
#     def set_model(self, model):
#         self.__model = model
        
#     def get_speed(self):
#         return self.__speed
    
#     def set_speed(self, speed):
#         self.__speed = speed    