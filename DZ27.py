class Fraction:
    
    count = 0
    
    def __init__(self, dividend, divisor) -> None:
        self.dividend = dividend
        self.divisor = divisor
        Fraction.count += 1
        
        
    @staticmethod
    def counter():
        return Fraction.count
    
    def show_fraction(self):
        print(f'{self.dividend}/{self.divisor}')
    
    

while True:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))

    res = Fraction(a, b)

    res.show_fraction()
    
    c = input('Повторить? y/n: ')
    
    if c == 'n':
        print('Кол-во повторений:', Fraction.counter())
        break
    
    
    
    
    
class TempConvert:
    
    count = 0
    
    @staticmethod
    def FtoC(temp):
        TempConvert.count += 1
        return int((temp - 32) * (5 / 9))
    
    @staticmethod
    def CtoF(temp):
        TempConvert.count += 1
        return int(temp / (5 / 9) + 32)
    
    @staticmethod
    def showCount():
        return TempConvert.count
    
    

a1 = TempConvert.FtoC(100)
print('100 Фаренгейтов в Цельсиях равно', a1)

a2 = TempConvert.CtoF(100)
print('100 Цельсиев в Фаренгейтах равно', a2)

a3 = TempConvert.showCount()

print('Количество подсчетов:', a3)





class EngMeterRus:
    
    @staticmethod
    def InchToM(value):
        return value * 0.0254
    
    @staticmethod
    def FootToM(value):
        return value * 0.3048
    
    @staticmethod
    def YardToM(value):
        return value * 0.9144
    
    @staticmethod
    def MileToM(value):
        return value * 1609
    
    @staticmethod
    def MtoInch(value):
        return value / 0.0254
    
    @staticmethod
    def MtoFoot(value):
        return value / 0.3048
    
    @staticmethod
    def MtoYard(value):
        return value / 0.9144
    
    @staticmethod
    def MtoMile(value):
        return value / 1609
    
    

num1 = int(input('Введите значение в М: '))
num2 = input('В какой единице измерения Вы хотите получить ответ? (Inch, Foot, Yard, Mile): ')

if num2 == 'Inch':
    res = EngMeterRus.MtoInch(num1)
    print(res)
elif num2 == 'Foot':
    res = EngMeterRus.MtoFoot(num1)
    print(res)
elif num2 == 'Yard':
    res = EngMeterRus.MtoYard(num1)
    print(res)
elif num2 == 'Mile':
    res = EngMeterRus.MtoMile(num1)
    print(res)
    
    
num1 = int(input('Введите значение: '))
num2 = input('Из какой единицы измерения Вы хотите получить ответ в М? (Inch, Foot, Yard, Mile): ')

if num2 == 'Inch':
    res = EngMeterRus.InchToM(num1)
    print(res, 'м')
elif num2 == 'Foot':
    res = EngMeterRus.FootToM(num1)
    print(res, 'м')
elif num2 == 'Yard':
    res = EngMeterRus.YardToM(num1)
    print(res, 'м')
elif num2 == 'Mile':
    res = EngMeterRus.MileToM(num1)
    print(res, 'м')