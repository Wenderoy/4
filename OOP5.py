class Calculator:
    def __init__(self):
        pass
    
    def add(self, a, b):
        return a + b
    
    def add_numbers(self, a, b):
        return self.__add(a, b)
    
    
# Создание объекта

calc = Calculator()

# Попытка вызвать закрытый метод вызовет ошибку

# calc.__add(3, 5)

# Доступ к закрытому методу через публичный метод класса

result = calc.add(3, 5)

print(result)