class Car():
    def __init__(self, model, year, manufacturer, capacity, color, cost):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.capacity = capacity
        self.color = color
        self.cost = cost
        
    def say_model(self):
        print('Модель автомобиля:', self.model)
        
    def say_year(self):
        print('Год выпуска автомобиля:', self.year)
        
    def say_manufacturer(self):
        print('Производитель автомобиля:', self.manufacturer)
        
    def say_capacity(self):
        print('Объем двигателя:', self.capacity)
        
    def say_color(self):
        print('Цвет автомобиля:', self.color)
        
    def say_cost(self):
        print('Стоимость автомобиля:', self.cost)
        

car1 = Car('m8', '2017', 'BMW', '4.4 л', 'brown', '153 580 USD')

car1.say_model()
car1.say_year()
car1.say_manufacturer()
car1.say_capacity()
car1.say_color()
car1.say_cost()


print('====================================================================')


class Book():
    def __init__(self, name, year, manufacturer, genre, author, cost):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.genre = genre
        self.author = author
        self.cost = cost
        
    def say_name(self):
        print('Название книги:', self.name)
        
    def say_year(self):
        print('Год издательства книги:', self.year)
        
    def say_manufacturer(self):
        print('Издательство книги:', self.manufacturer)
        
    def say_genre(self):
        print('Жанр книги:', self.genre)
        
    def say_author(self):
        print('Автор книги:', self.author)
        
    def say_cost(self):
        print('Цена книги:', self.cost)
        

book1 = Book('Робинзон Крузо', '2021', 'Азбука, Азбука-Аттикус', 'Приключения', 'Дефо Д.', '1400 руб.')

book1.say_name()
book1.say_year()
book1.say_manufacturer()
book1.say_genre()
book1.say_author()
book1.say_cost()


print('====================================================================')