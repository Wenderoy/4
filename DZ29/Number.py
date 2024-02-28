class Number:
    def __init__(self, value):
        self.value = value
        
    def __add__(self, other):
        return self.value + other.value
    
    def __sub__(self, other):
        return self.value - other.value
    
    def __mul__(self, other):
        return self.value * other.value
    
    def __truediv__(self, other):
        if other.value != 0:
            return self.value / other.value
        else:
            raise ZeroDivisionError('На ноль делить нельзя')


num1 = Number(10)
num2 = Number(5)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)