# class A:
#     def method_a(self):
#         print('Метод класса А')
        
        
# class B:
#     def method_b(self):
#         print('Метод класса B')
        

# class C(A, B):
#     def method_c(self):
#         print('Метод класса C')
        
# c = C()
# c.method_a()
# c.method_b()
# c.method_c()




# ==================================================================



class Wheels:
    def method_wheel(self):
        print('Wheeeeel!')
        
class Motor:
    def method_motor(self):
        print('Trrrrrr!')
        
class Doors:
    def method_open(self):
        print('Scrr, Scrr...')
        

class Auto(Wheels, Motor, Doors):
    def method_car(self):
        return super().method_car()
    

car = Auto()
car.method_wheel()
car.method_motor()
car.method_open()