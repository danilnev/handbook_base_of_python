class Point:
    def __init__(self, crd_x, crd_y):
        self.x = crd_x
        self.y = crd_y

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def length(self, point):
        return round(((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5, 2)


# point = Point(3, 5)
# print(point.x, point.y)
# point.move(2, -3)
# print(point.x, point.y)
#
# first_point = Point(2, -7)
# second_point = Point(7, 9)
# print(first_point.length(second_point))
# print(second_point.length(first_point))
