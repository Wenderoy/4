# class Person:
#     def __init__(self, name, age):
#         self.__name = name #закрытый атрибут
#         self.age = age
        
#     def get_name(self):
#         return self.__name
    
    
#     def set_name(self, name):
#         self.__name = name
        

# # Создание объекта

# person = Person('Alice', 30)

# # Попытка получить доступ к закрытому атрибуту вызывает ошибку

# # print(person.__name)

# # Доступ к закрытому атрибуту через методы класса

# print(person.get_name())

# # Изменение закрытого атрибута через метод

# person.set_name('Bob')
# print(person.get_name())


# print('========================================================')


class Person:
    count = 0
    def __init__(self, name, age):
        self.__name = name #закрытый атрибут
        self.age = age
        
        
    @staticmethod
    def get_name(self):
        Person.count += 1
        return self.__name
    
    
    @staticmethod
    def set_name(self, name):
        self.__name = name
        Person.count += 1


person = Person('Alice', 30)

print(person.get_name())

person.set_name('Bob')
print(person.get_name())

print('Количество вызовов:', Person.count)