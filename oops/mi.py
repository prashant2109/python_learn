class Rectangle:
    def __init__(self, length, width):
        print('Rectangle Initiated')
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (2*self.length) + (2*self.width)

class Square(Rectangle):
    def __init__(self, length):
        print('Square Initiated')
        super(Square, self).__init__(length, length)
        # Rectangle.__init__(self, length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        # face_area = super(Square, self).area() # look for area a level above hierarchy
        return face_area * 6

    def volume(self):
        face_area = super().area()
        # face_area = super(Square, self).area() # look for area a level above hierarchy
        return face_area * self.length

class Diamond:
    pass

class Parallelogram(Diamond):
    pass

class Rhombus:
    pass

class Triangle(Parallelogram, Rhombus):
    def __init__(self, base, height):
        print('Triangle Initiated')
        self.base    = base
        self.height  = height

    # def area(self):
    #     return 0.5 * self.base * self.height

    def tri_area(self):
        # print(self.base)
        return 0.5 * self.base * self.height

# class RightPyramid(Triangle, Square):
class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height):
        print('RightPyramid initiated')
        self.base = base    
        self.slant_height = slant_height
        super().__init__(base)
    
    def area(self):
        base_area = super().area()
        perimeter = super().perimeter()
        return 0.5 * perimeter * self.slant_height + base_area

    def area_2(self):
        base_area = super().area()
        triangle_area = super().tri_area()
        return triangle_area * 4 + base_area

if __name__ == '__main__':
    rp = RightPyramid(5,  7)
    print(RightPyramid.__mro__)
    # print(rp.area())
    # print(rp.area_2())
