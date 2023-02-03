class Point:
    def __init__(self, crd_x, crd_y):
        self.x = crd_x
        self.y = crd_y


class Rectangle:
    def __init__(self, point1, point2):
        if point1[0] < point2[0] and point1[1] > point2[0]:
            self.first_point = Point(point1[0], point1[1])
            self.second_point = Point(point2[0], point2[1])
        elif point1[0] < point2[0] and point1[1] < point2[1]:
            pass

    def perimeter(self):
        return round(2 * (abs(self.first_point.x - self.second_point.x) +
                          abs(self.first_point.y - self.second_point.y)), 2)

    def area(self):
        return round(abs(self.first_point.x - self.second_point.x) * abs(self.first_point.y - self.second_point.y), 2)

    def get_pos(self):
        return round(self.first_point.x, 2), round(self.first_point.y, 2)

    def get_size(self):
        return round(abs(self.first_point.x - self.second_point.x), 2), \
            round(abs(self.first_point.y - self.second_point.y), 2)

    def move(self, dx, dy):
        self.first_point.x += dx
        self.second_point.x += dx
        self.first_point.y += dy
        self.second_point.y += dy

    def resize(self, width, height):
        pass


rect = Rectangle((3.2, -4.3), (7.52, 3.14))
print(rect.get_pos(), rect.get_size())
rect.move(1.32, -5)
print(rect.get_pos(), rect.get_size())
