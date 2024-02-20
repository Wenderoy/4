class Point:
    color = 'red'
    circle = 2
    
Point.color = 'black'
print(Point.color)
print(Point.circle)

a = Point()

print(type(a))
print(type(a) == Point)

print(isinstance(a, Point))

Point.circle = 3

print (a.circle)

a.circle = 4

Point.circle = 5

print(a.circle, Point.circle)

print(a.__dict__)


setattr(Point, 'prop', 10)

print(Point.prop)


print(getattr(Point, 'a', False))


del Point.prop

print(hasattr(Point, 'prop'))


a = Point()
b = Point()

a.x = 3
a.y = 5


# ---------------------------------------------------------------------------


class Point1:
    color = 'red'
    circle = 5
    
    def set_coords(self, x, y):
        self.x = x
        self.y = y
        print('Вызов метода set_coords', str(self))
        print('x =', x)
        print('y =', y)
        
        
    def get_coords(self):
        return (self.x, self.y)    
    

pt = Point1()
pt2 = Point1()
pt.set_coords(1, 2)
print(pt.__dict__)
pt2.set_coords(10, 20)
print(pt2.__dict__)
print(pt.get_coords())
print(pt2.get_coords())

f = getattr(pt, 'get_coords')
print(f())



class Point3:
    
    def __init__(self):
        print('Вызов __init__')
        self.x = 0
        self.y = 0
        
pt = Point3()
print(pt.__dict__)


class Point4:
    
    def __init__(self):
        print('Вызов __init__')
        
    def __del__(self):
        print('Удаление экземпляра')
            
        
        self.x = 0
        self.y = 0
        
pt = Point4()
print(pt.__dict__)