class Rectangle:
    length = 0
    width = 0

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.width * self.length


if __name__ == "__main__":
    rectangle = Rectangle(4, 14)
    print("Length of rectangle: %s" % rectangle.length);
    print("Width of rectangle: %s" % rectangle.width);
    print("Area of rectangle: %s" % rectangle.area());
