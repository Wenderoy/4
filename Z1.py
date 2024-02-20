import string
import random
from math import sqrt


# a = string.ascii_letters

# c = int(input('Введите длину желаемого пароля: '))

# itogo = ''



# for i in range(c):
#     itogo += str(random.randint(0, 9))
#     num = random.randint(0, 52)
#     itogo += a[num::]

# itogo = itogo[0:c:1]

# print('Итоговый пароль:', itogo)


# ---------------------------------------------------------------------------

# str1 = input('Введите строку: ')

# colls = str1.split(' ')

# itogo = len(colls)

# print('Слов в строке:', itogo)


# ---------------------------------------------------------------------------


# f = int(input('Введите число: '))

# b = 0
# a = f

# while a > 0:
#     if f % a == 0: b += 1
#     a -= 1
    
# if b > 2:
#     print ('Число не простое')
# else:
#     print ('Число простое')



# ---------------------------------------------------------------------------


# txt1 = input('Введите строку 1: ')
# txt2 = input('Введите строку 2: ')

# a = 0

# for i in txt1:
#     if i.lower() not in txt1.lower():
#         print('Строки не являются анаграммами')
#     else:
#         a += 1
        
# for i in txt2:
#     if i.lower() not in txt2.lower():
#         print('Строки не являются анаграммами')
#     else:
#         a += 1
        
# if a >= 2:
#     print('Строки являются анаграммами')



# ---------------------------------------------------------------------------



# def nsymb(n, str1):
#     a = str1[0:n:1]
#     return a



# str1 = input('Введите строку: ')
# ns = int(input('Введите n символов для обрезания: '))

# itogo = nsymb(ns, str1)

# print(itogo)


# ---------------------------------------------------------------------------


# def multiplication(n):
#     for i in range(0, n):
#        print(i, ' * ', n, ' = ', i * n)
        
        
# multiplication(5)



# ---------------------------------------------------------------------------


# n = int(input("До какого диапазона нужно сгенерировать простые числа? "))
# lst = []
# for i in range(2, n+1):
#     for j in lst:
#         if j > int((sqrt(i)) + 1):
#             lst.append(i)
#             break
#         if (i % j == 0):
#             break
#     else:
#         lst.append(i)
# print (lst)