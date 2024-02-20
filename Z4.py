import math

class Fraction:
    
    def __init__(self, c_den, denominator):
        self.c_den = c_den
        self.denominator = denominator
        
    def __floordiv__(self, denominator):
        if denominator != 0:
            return self.value / denominator
        else:
            raise ZeroDivisionError('На ноль делить нельзя')
        
    @staticmethod
    def least_common_multiple(b, d):
        return abs(b * d) // math.gcd(b, d)
    
    
    
a = 1
b = 4
c = 5
d = 6

c_den = Fraction.least_common_multiple(b, d)
print(c_den)

additional_multiplier1 = Fraction(c_den, b)
additional_multiplier2 = Fraction(c_den, d)

print(additional_multiplier1, additional_multiplier2)