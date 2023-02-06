class Point:
    def __init__(self, crd_x, crd_y):
        self.x = crd_x
        self.y = crd_y

    def move(self, move_x, move_y):
        self.x += move_x
        self.y += move_y

    def length(self, point):
        return round(((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 2:
            super().__init__(*args)
        elif len(args) == 1:
            super().__init__(*args[0])
        else:
            super().__init__(0, 0)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'


# first_point = PatchedPoint((2, -7))
# second_point = PatchedPoint(7, 9)
# print(*map(str, (first_point, second_point)))
# print(*map(repr, (first_point, second_point)))
