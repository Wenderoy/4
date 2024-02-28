class Library:

    def __init__(self, name, address, sum, *books):
        self.name = name
        self.address = address
        self.books = books
        self.sum = sum

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)
        
    def show_books(self):
        for book in self.books:
            print(book)
            
    def __add__(self, other):
        return self.sum + other.sum
    
    def __sub__(self, other):
        return self.sum - other.sum
    
    def __iadd__(self, other):
        self.sum += other.sum
        return self
    
    def __isub__(self, other):
        self.sum -= other.sum
        return self
    
    def __eq__(self, other):
        if isinstance(other, Library):
            return self.sum == other.sum
        else:
            return False
        
    def __ne__(self, other):
        if isinstance(other, Library):
            return self.sum != other.sum
        else:
            return False
        
    def __gt__(self, other):
        if isinstance(other, Library):
            return self.sum > other.sum
        else:
            return False
        
    def __lt__(self, other):
        if isinstance(other, Library):
            return self.sum < other.sum
        else:
            return False
        
    def __ge__(self, other):
        if isinstance(other, Library):
            return self.sum >= other.sum
        else:
            return False
        
    def __le__(self, other):
        if isinstance(other, Library):
            return self.sum <= other.sum
        else:
            return False
        

lib1 = Library('lib1', 'address1', 300, 'book1', 'book2', 'book3')

lib1.show_books()

lib2 = Library('lib2', 'address2', 200, 'book4', 'book5', 'book6')

lib2.show_books()

print(lib1 + lib2)
print(lib1 - lib2)
print(lib1 == lib2)
print(lib1 != lib2)
print(lib1 > lib2)
print(lib1 < lib2)
print(lib1 >= lib2)
print(lib1 <= lib2)