from accessify import private, protected

class Point:


    def __init__(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Координаты должны быть числами")



    @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)


    def get_coord(self):
        return self.__x, self.__y



pt = Point(1, 2)
print(pt.get_coord())
print(dir(pt))