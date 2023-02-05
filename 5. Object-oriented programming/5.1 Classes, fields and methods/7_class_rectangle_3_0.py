class Point:
    def __init__(self, crd_x, crd_y):
        self.x = crd_x
        self.y = crd_y

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def length(self, point):
        return round(((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5, 2)


class Rectangle:
    def __init__(self, point1, point2):
        if point1[0] <= point2[0] and point1[1] >= point2[1]:
            self.first_point = Point(point1[0], point1[1])
            self.second_point = Point(point2[0], point2[1])
        elif point1[0] <= point2[0] and point1[1] <= point2[1]:
            self.first_point = Point(point1[0], point1[1] + (point2[1] - point1[1]))
            self.second_point = Point(point2[0], point2[1] - (point2[1] - point1[1]))
        elif point1[0] >= point2[0] and point1[1] <= point2[1]:
            self.first_point = Point(point2[0], point2[1])
            self.second_point = Point(point1[0], point1[1])
        elif point1[0] >= point2[0] and point1[1] >= point2[1]:
            self.first_point = Point(point2[0], point1[1])
            self.second_point = Point(point1[0], point2[1])

    def perimeter(self):
        return round(2 * (abs(self.second_point.x - self.first_point.x) +
                          abs(self.first_point.y - self.second_point.y)), 2)

    def area(self):
        return round(abs(self.second_point.x - self.first_point.x) * abs(self.first_point.y - self.second_point.y), 2)

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
        self.second_point.x = self.first_point.x + width
        self.second_point.y = self.first_point.y - height

    def turn(self):
        point1 = self.first_point.x, self.first_point.y
        point2 = self.second_point.x, self.second_point.y
        self.first_point.x = point2[1]
        self.first_point.y = point2[0]
        self.second_point.x = point1[1]
        self.second_point.y = point1[0]

    def scale(self, factor):
        width, height = self.get_size()
        self.first_point.x -= round(width / factor, 2)
        self.first_point.y += round(height / factor, 2)
        self.second_point.x += round(width / factor, 2)
        self.second_point.y -= round(height / factor, 2)


rect = Rectangle((3.14, 2.71), (-3.14, -2.71))
print(rect.get_pos(), rect.get_size(), sep='\n')
rect.scale(2.0)
print(rect.get_pos(), rect.get_size(), sep='\n')

