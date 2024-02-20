class BankAccount():
    def __init__(self):
        self.__balance = 0
 
    def deposit(self, sum):
        self.__balance += sum
        return self.__balance
 
    def withdraw(self, sum):
        self.__balance < sum
        self.__balance -= sum
        return self.__balance

    def get_balance(self):
        return self.__balance
    
bank = BankAccount()

a = input('Введите "+" для прибавления и "-" для убавления: ')
b = int(input('Введите сумму: '))
bank = BankAccount()

if a == '+':
    c = bank.deposit(b)
else:
    c = bank.withdraw(b)
    
c = bank.get_balance()
print('На счете', c)