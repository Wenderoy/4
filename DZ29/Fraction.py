class Fraction:
    
    def __init__(self, n, d):
        self.n = n
        self.d = d
        
    def __add__(self, other):
        return f'{self.n * other.d + other.n * self.d} / {self.n * other.d}'
    
    
    def __sub__(self, other):
        return f'{self.n * other.d - other.n * self.d} / {self.n * other.d}'
    
    
    def __mul__(self, other):
        return f'{self.n * other.n} / {self.d * other.d}'
    
    
    def __truediv__(self, other):
        if other.d != 0:
            return f'{self.n * other.d} / {self.d * other.n}'
        else:
            raise ZeroDivisionError('На ноль делить нельзя')
        
        
f = Fraction(2, 2)
f2 = Fraction(4, 5)

print(f + f2)
print(f - f2)
print(f * f2)
print(f / f2)