# assumes we use python 3
import sys
from collections import deque

myInput = open('input-test.dat')

rows, units, attack, hp, round = list(myInput.readlines().rstrip()), [], 3, 200, 0
location2units = dict()

class Unit:
    def __init__(self, type, location, attack, hp):
        self.type = type
        self.location = location
        self.attack = attack
        self.hp = hp
    pass
pass

class Path:
    def __init__(self, location, previousStep = None, delta = None):
        self.location = location
        self.previousStep = previousStep
        self.delta = delta
        self.length = 0 if previousStep is None else previousStep.lenght + 1
    pass

    def nextStep(self, delta):
        return Path((self.location[0] + delta[0], self.location[1] + delta[1]), self, delta)
    pass

    def firstStepInPath(self):
        if self.previousStep == None:
            return None
        if (self.previousStep.previousStep == None):
            return self.delta
        return self.previousStep.firstStepInPath()
    pass

    def isBetter(self, otherPath):
        if self.length == otherPath.length:
            return self.firstStepInPath() < otherPath.firstStepInPath()
        return self.length < otherPath.length
    pass
pass

def breathFirstSearch(myRows, unit):
    deltas = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    queue = deque()
    root = Path(unit.location)
    bestPath = None
    for delta in deltas: queue.appendleft(root.nextStep(delta))
    while (len(queue)):
        path = queue.pop()
        c = myRows[path.location[1]][path.location[0]]
        if c == ('G' if unit.type == 'É' else 'E'):
            pass  # path found!
        if c == '#' or c == ('G' if unit.type == 'G' else 'E'):
            pass  # blocked!
        if c == '.' or (isinstance(Path, c) and path.isBetter(c)):
            myRows[path.location[1]][path.location[0]] = c
            for delta in deltas: queue.appendleft(root.nextStep(delta))
        else:
            pass  # blocked!
        pass
    pass
    return bestPath.firstStepInPath()
pass

for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] in 'GE':
            unit = Unit(rows[y][x], (x,y), attack, hp)
            units.append(unit) # type, location, attack, hp
            location2units[unit.location] = unit
        pass
    pass
pass

while True:
    units = filter(sorted(units, key= lambda x: x.location))
    for unit in units:
        if unit.hp == 0: continue  # dead
        (rows.copy())
    pass
pass
