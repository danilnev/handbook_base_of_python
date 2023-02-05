class Cell:
    def __init__(self, status):
        self.cell_status = status

    def status(self):
        return self.cell_status


class Checkers:
    def __init__(self):
        self.desk = []
        for i in range(1, 9):
            if i in [4, 5]:
                self.desk.append([Cell('X') for j in range(8)])
            else:
                row = []
                if i % 2 == 1:
                    count = 1
                else:
                    count = 0
                for j in range(1, 9):
                    if j % 2 == count:
                        if i <= 3:
                            row.append(Cell('W'))
                        else:
                            row.append(Cell('B'))
                    else:
                        row.append(Cell('X'))
                self.desk.append(row)

    def move(self, f, t):
        letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
        self.get_cell(t).cell_status = self.get_cell(f).status()
        self.get_cell(f).cell_status = 'X'

    def get_cell(self, p):
        letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
        row = self.desk[int(p[1]) - 1]
        return row[letters[p[0]] - 1]


# checkers = Checkers()
# checkers.move('C3', 'D4')
# checkers.move('H6', 'G5')
# for row in '87654321':
#     for col in 'ABCDEFGH':
#         print(checkers.get_cell(col + row).status(), end='')
#     print()
