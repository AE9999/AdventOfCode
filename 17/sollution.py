import sys, re

class Clay:
    def __init__(self, line):
        self.x = [int(d) for d in re.findall(r'-?\d+', sorted(line.rstrip().split(' '))[0])]
        self.y = [int(d) for d in re.findall(r'-?\d+', sorted(line.rstrip().split(' '))[1])]
    pass

    def __str__(self):
        return "(Clay x:%s, y:%s)" % (str(self.x), str(self.y))
    pass

    def minX(self): return sorted(self.x)[0]

    def maxX(self): return sorted(self.x, reverse=True)[0]

    def minY(self): return sorted(self.y)[0]

    def maxY(self): return sorted(self.y, reverse=True)[0]

    def squares(self):
        if len(self.x) == 1: return [(self.x[0], y, self) for y in range(self.y[0], self.y[1] + 1)]
        else: return [(x, self.y[0], self) for x in range(self.x[0], self.x[1] + 1)]
    pass
pass

class SearchNode:
    def __init__(self, state, x, y, rows):
        self.state = state
        self.x = x
        self.y = y
        self.rows = rows
        self.rows[self.y][self.x] = self
        printRows()
    pass

    def spread(self):
        if not self.spreadDown():
            s = self.spreadLeft() + self.spreadRight() == 0
            self.state = '~' if not s else self.state
            return s
        pass
        return True
    pass

    def spreadDown(self):
        if self.y + 1 >= len(rows): return True
        return self.rows[self.y+1][self.x] == '.' \
               and SearchNode('|', self.x, self.y + 1, self.rows).spread()

    def spreadLeft(self):
        left, surface = self.rows[self.y][self.x -1], self.rows[self.y +1][self.x]
        return left == '.' \
                   and (surface == '#' or (isinstance(surface, SearchNode) and surface.state == '~')) \
                   and SearchNode('|', self.x - 1, self.y, self.rows).spread()

    def spreadRight(self):
        right, surface = self.rows[self.y][self.x+ 1], self.rows[self.y +1][self.x]
        return right == '.' \
                   and (surface == '#' or (isinstance(surface, SearchNode) and surface.state == '~')) \
                   and SearchNode('|', self.x + 1, self.y, self.rows).spread()
pass

myInput = open('input-test.dat')

clays = list(map(Clay, myInput.readlines()))
minX = sorted(list(map(lambda x: x.minX(), clays)))[0]
maxX = sorted(list(map(lambda x: x.maxX(), clays)), reverse=True)[0]
minY = sorted(list(map(lambda x: x.minY(), clays)))[0]
maxY = sorted(list(map(lambda x: x.maxY(), clays)), reverse=True)[0]

normalization = [(minX -1), 0]

rows = []
for y in range(maxY + 1): rows.append(["."] * ((maxX + 1) - normalization[0]))

for square in [square for clay in clays for square in clay.squares()]:
    rows[square[1] - normalization[1]][square[0] - normalization[0]] = square[2]

def printRows():
    print("")
    global rows
    def printValue(value):
        if value == '.': return '.'
        if isinstance(value, Clay): return '#'
        if isinstance(value, SearchNode): return value.state
    for row in rows: print("".join(list(map(printValue, row))))
    print("")

printRows()

SearchNode('+', 500 - normalization[0], 0 - normalization[1], rows).spread()