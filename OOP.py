# class Person:
#     name = 'Иван'
#     age = '20'
    
#     def say(self):
#         print('Привет')
        
# person1 = Person()
# print(person1.name)
# person1.say()


# person2 = Person()
# person2.name = 'Василий'
# print(person2.name)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def say(self):
#         print('Привет')
        
# person1 = Person('Иван', 20)
# print(person1.name)
# person1.say()


# class Person():
#     def __init__(self):
#         print('Метод init')
        

# person1 = Person()



# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
# person1 = Person('Иван', 15)
# person2 = Person('Петр', 14)
# print (person1.name)
# print(person1.age)
# print(person2.name)
# print(person2.age)


from typing import Any


class Person():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return(f'Меня зовут {self.name}')
    
person1 = Person('Иван')
print(person1)