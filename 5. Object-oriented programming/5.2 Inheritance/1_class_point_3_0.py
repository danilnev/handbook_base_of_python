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


# first_point = PatchedPoint((2, -7))
# second_point = PatchedPoint(7, 9)
# print(first_point.length(second_point))
# print(second_point.length(first_point))

