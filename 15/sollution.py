# assumes we use python 3
import sys
from collections import deque

myInput = open('input-test.dat')

rows = list(map(lambda x: list(x.rstrip()), myInput.readlines()))
units, attack, hp  = [], 3, 200
deltas = [(0, -1), (-1, 0), (1, 0), (0, 1)]

def printState():
    global rows
    print()
    print("*" * len(rows[0]))
    for row in rows:
        print("".join(list(map(lambda x: x if not isinstance(x, Unit) else x.type, row))))
    pass
    print("*" * len(rows[0]))
pass

class Unit:
    def __init__(self, type, location, attack, hp):
        self.type = type
        self.location = location
        self.attack = attack
        self.hp = hp
    pass

    def move(self, delta):
        self.location[0] += delta[0]
        self.location[1] += delta[1]
    pass
pass

class Path:
    def __init__(self, location, previousStep = None, delta = None):
        self.location = location
        self.previousStep = previousStep
        self.delta = delta
        self.length = 0 if previousStep is None else previousStep.length + 1
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

    def isBetterThan(self, otherPath):
        if self.length == otherPath.length:
            return self.firstStepInPath() < otherPath.firstStepInPath()
        return self.length < otherPath.length
    pass
pass

def breathFirstSearch(myRows, unit):
    global deltas
    queue = deque()
    root = Path(unit.location)
    bestPath = None
    for delta in deltas: queue.appendleft(root.nextStep(delta))
    while len(queue):
        currentPath = queue.pop()

        # Best path already found continue
        if bestPath is not None and bestPath.isBetterThan(currentPath): continue

        c = myRows[currentPath.location[1]][currentPath.location[0]]
        if isinstance(c, Unit) and c.type != unit.type:
            bestPath = currentPath  # path found!
        elif c == '#' \
            or (isinstance(c, Unit) and c.type == unit.type):
            continue  # blocked!
        elif c == '.' or (isinstance(c, Path) and currentPath.isBetterThan(c)):
            myRows[currentPath.location[1]][currentPath.location[0]] = c
            for delta in deltas: queue.appendleft(root.nextStep(delta))
        else:
            continue
        pass
    pass
    return bestPath.firstStepInPath()
pass

for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] in 'GE':
            unit = Unit(rows[y][x], (x,y), attack, hp)
            rows[y][x] = unit
            units.append(unit) # type, location, attack, hp
        pass
    pass
pass

printState()
for x in range(10):
    units = sorted(units, key=lambda x: x.location)
    for unit in units:
        if unit.hp <= 0: continue  # dead
        delta = breathFirstSearch(rows.copy(), unit)
        x,y = unit.location[0] + delta[0], unit.location[1] + delta[1]
        target = rows[y][x]
        if isinstance(target, Unit): #attack target
            target.hp -= unit.attack
            if target.hp < 0: rows[y][x] = '.'
        else: # move unit
            rows[unit.location[1]][unit.location[0]] = '.'
            rows[y][x] = unit
            unit.move(delta)
        pass
    pass
    printState()
pass
