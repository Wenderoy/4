import random

num = int(input('Введите число: '))

res = 1
for i in range(1, num + 1):
    res = res * i
print (res)



num = random.randint(1, 10)
print(num)
p = 3
while p > 0:
    a = int(input('Введите число от 1 до 10: '))
    if a == num:
        print('Вы выиграли!')
        break
    print('Не угадали!')
    p = p - 1
    
    

max = 0
for i in range(1000):
    inp = int(input('Введите число: '))
    if inp == 0:
        print(max)
        break
    if inp > max:
        max = inp