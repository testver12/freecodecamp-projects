import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = self.width * self.height
    def set_width(self, new_width):
        self.width = new_width
        self.area = self.width * self.height
    def set_height(self, new_height):
         self.height = new_height
         self.area = self.width * self.height
    def get_area(self):
        return self.area 
    def get_perimeter(self):
        self.perimeter = ((self.width * 2) + (self.height * 2))
        return self.perimeter
    def get_diagonal(self) -> float:
        square = (self.width ** 2) + (self.height **2)
        self.diagonal = math.sqrt(square)
        return self.diagonal
    def get_picture(self):
        picture = ''
        rows = self.height
        stars = '*' * self.width
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            for i in range(rows):
                picture += f"{stars}\n"
        return picture
    def get_amount_inside(self, shape_obj) -> int:
        shape_area = 0
        if type(shape_obj) == Rectangle:
            shape_area = shape_obj.area
        elif type(shape_obj) == Square:
            shape_area = shape_obj.side_length ** 2
        amount_inside = self.area / shape_area
        return int(amount_inside)
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
class Square(Rectangle):
    def __init__(self, side_length):
        self.side_length = side_length
        super().__init__(side_length,side_length)
        self.width = side_length
        self.height = side_length

    def set_width(self):
        self.width = side_length
        self.height = side_length

    def set_height(self):
        self.width = side_length
        self.height = side_length
    def set_side(self, new_length):
        self.side_length = new_length
    def set_width(self, new_length):
        self.side_length = new_length
    def set_height(self, new_length):
        self.side_length = new_length
    def __str__(self):
        return f"Square(side={self.side_length})"
    def get_area(self):
        return self.side_length ** 2
    def get_perimeter(self):
        return 4 * (self.side_length)
    def get_diagonal(self) -> float:
        return (2*self.side_length**2)**0.5
    def get_picture(self):
        picture = ''
        rows = self.side_length
        stars = '*' * self.side_length
        if self.side_length > 50:
            return 'Too big for picture.'
        else:
            for i in range(rows):
                picture += f"{stars}\n"
        return picture
rect = Rectangle(3, 6)
sq = Square(5)
rect.set_height(10)
rect.set_width(15)
print(rect.get_amount_inside(sq))
