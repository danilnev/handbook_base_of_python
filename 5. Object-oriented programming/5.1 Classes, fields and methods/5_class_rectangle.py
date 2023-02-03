class Point:
    def __init__(self, crd_x, crd_y):
        self.x = crd_x
        self.y = crd_y


class Rectangle:
    def __init__(self, point1, point2):
        self.first_point = Point(point1[0], point1[1])
        self.second_point = Point(point2[0], point2[1])

    def perimeter(self):
        return round(2 * (abs(self.first_point.x - self.second_point.x) +
                          abs(self.first_point.y - self.second_point.y)), 2)

    def area(self):
        return round(abs(self.first_point.x - self.second_point.x) * abs(self.first_point.y - self.second_point.y), 2)


# rect = Rectangle((3.2, -4.3), (7.52, 3.14))
# print(rect.perimeter())
# rect = Rectangle((7.52, -4.3), (3.2, 3.14))
# print(rect.area())
