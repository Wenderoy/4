class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_coords(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left


    def __getattribute__(self, item):
        if item == 'x':
            raise ValueError('Доступ запрещен')
        else:
            return object.__getattribute__(self, item)


    def __setattr__(self, key, value):
        if key == 'z':
            raise ValueError('Недопустимое имя атрибута')
        else:
            self.__dict__[key] = value



    def __getattr__(self, item):
        return False


    def __delattr__(self, item):
        print('__delattr__', item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)
pt1.set_bound(-100)
#pt1.z = 1
pt2.y = 3
#a = pt1.x
a = pt1.y
del pt2.y
print(a)
print(pt1.MAX_COORD)
print(pt1.__dict__)
print(Point.__dict__)