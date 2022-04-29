class Square:

    def __init__(self, side_length, color="white"):
        self.side_length = side_length
        self.color = color

    def set_side(self, length):
        self.side_length = length

    def set_color(self, color):
        self.color = color

    def get_side(self):
        return self.side_length

    def get_color(self):
        return self.color

    def get_perimeter(self):
        return self.side_length * 4


square_1 = Square(2)
print(square_1.get_side())
print(square_1.get_perimeter())
print(square_1.get_color())
print("—-")
square_1.set_side(3)
square_1.set_color("red")
print(square_1.get_side())
print(square_1.get_perimeter())
print(square_1.get_color())
print("—-")
square_1 = Square(1, "black")
print(square_1.get_side())
print(square_1.get_perimeter())
print(square_1.get_color())
