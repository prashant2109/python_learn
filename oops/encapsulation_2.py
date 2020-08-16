class Shape:
    def __init__(self):
        self._height = 10
        self.__width = 30

    def area(self):
        area = self._height * self.__width
        return area

class Square(Shape):
    def print_parent_elems(self):
        print(self._height)
        print(self.__width)

if __name__ == '__main__':
    sq_Obj = Square()
    sq_Obj.print_parent_elems()