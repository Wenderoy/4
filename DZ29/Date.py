from datetime import datetime
from datetime import timedelta

class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        

    def __sub__(self, other):
        days1 = datetime.strptime(f'{other.year}-{other.month}-{other.day}', '%Y-%m-%d')
        days2 = datetime.strptime(f'{self.year}-{self.month}-{self.day}', '%Y-%m-%d')
        
        return (days2 - days1).days

    
    def __add__(self, other):
        start_date = datetime.strptime(f'{self.year}-{self.month}-{self.day}', '%Y-%m-%d')
        end_date = start_date + timedelta(days=other)
        
        return f'{end_date.day} / {end_date.month} / {end_date.year}'
        
    
    
d = Date(10, 10, 2022)
d2 = Date(5, 5, 2020)

print(d - d2)

print(d + 5)