# class Stars:
#     def __init__(self, n):
#         self.qty = '*' * n
        
#     def __add__(self, n):
#         return self.qty + '$' * n
    

# a = Stars(5)
# b = a + 3


# print(b)



# class Number:
#     def __init__(self, value):
#         self.value = value
        
#     def __add__(self, other):
#         return self.value + other.value
    
#     def __sub__(self, other):
#         return self.value - other.value
    
#     def __mul__(self, other):
#         return self.value * other.value
    
#     def __truediv__(self, other):
#         if other.value != 0:
#             return self.value / other.value
#         else:
#             raise ZeroDivisionError('На ноль делить нельзя')


# num1 = Number(10)
# num2 = Number(5)

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)



# class A:
#     def __init__(self, arg):
#         self.arg = arg
        
#     def __str__(self):
#         return str(self.arg)
    

# class B:
    
#     def __init__(self, *args):
#         self.aList = []
#         for i in args:
#             self.aList.append(A(i))     
            
            
#     def __getitem__(self, i):
#         return self.aList[i]
            
            
# group = B(4, 6, 'abc')

# print(group.aList[1])
# print(group[1])
# print(group[0])

# a = A(2)

# print(a)

# print(type(a))



# class Changebale:
    
#     def __init__(self, color):
#         self.color = color
#     def __call__(self, newcolor):
#         self.color = newcolor
#     def __str__(self):
#         return self.color
    
    
# canvas = Changebale('red')
# frame = Changebale('blue')


# canvas('green')
# frame('black')


# print(canvas)
# print(frame)



