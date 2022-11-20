class Parallelogram:
    @staticmethod
    def get_area(width, length):
        return width * length


first = Parallelogram.get_area(10, 12)
print(first)


class Square(Parallelogram):
    @staticmethod
    def get_area(width):
        return width ** 2


second = Square.get_area(10)
print(second)