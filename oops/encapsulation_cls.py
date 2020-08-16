class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self._width  = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height
        return
    
    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width
        return 

if __name__ == '__main__':
    r_Obj = Rectangle(10, 15)
    # r_Obj.__height = 20  # cannot access outside the class
    # r_Obj.set_height(5)
    # print(r_Obj.get_height())
    # print(r_Obj.__height)
    # print(r_Obj._width)  # protected method can be accessed even outside the class, it is just convention to follow
    # r_Obj._width = 20
    # print(r_Obj._width)