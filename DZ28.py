class Point:
    
    color = 'red'
    circle = 2
    
    
a = Point()
b = Point()

print(isinstance(a, Point))

Point.circle = 3

print(Point.circle)

setattr(Point, 'prop', 1)
setattr(Point, 'type_pt', 'square')

print(Point.prop)
print(Point.type_pt)

print(Point.__dict__)

print(type(a))

print(type(a) == Point)

setattr(Point, 'test', 'тест')

print(Point.test)