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

def deepCopyOfRows():
    global rows
    newRows = []
    for row in rows:
        newRow = []
        for column in row:
            newRow.append(column)
        pass
        newRows.append(newRow)
    pass
    return newRows
pass

class Unit:
    def __init__(self, type, location, attack, hp):
        self.type = type
        self.location = location
        self.attack = attack
        self.hp = hp
    pass

    def move(self, delta):
        self.location = (self.location[0] + delta[0], self.location[1] + delta[1])
    pass

    def __str__(self):
        return "(Unit type:%s location:%s, attack:%d health:%d)" \
                % (self.type, str(self.location), self.attack, self.hp)
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

    def __str__(self):
        return "(Path location:%s lenght:%d)" % (str(self.location), self.length)
    pass
pass

def breathFirstSearch(myRows, unit):
    global deltas
    queue = deque()
    root = Path(unit.location)
    myRows[unit.location[1]][unit.location[0]] = root
    bestPath = None
    for delta in deltas: queue.appendleft(root.nextStep(delta))
    while len(queue):
        currentPath = queue.pop()
        c = myRows[currentPath.location[1]][currentPath.location[0]]
        print("\tConsidering %s => %s .."  % (currentPath, str(c)))

        # Best path already found continue
        if bestPath is not None and bestPath.isBetterThan(currentPath): continue

        if isinstance(c, Unit) and c.type != unit.type:
            bestPath = currentPath  # path found!
        elif c == '#' \
            or (isinstance(c, Unit) and c.type == unit.type):
            continue  # blocked!
        elif c == '.' or (isinstance(c, Path) and currentPath.isBetterThan(c)):
            myRows[currentPath.location[1]][currentPath.location[0]] = currentPath
            for delta in deltas: queue.appendleft(currentPath.nextStep(delta))
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
        print ("Working with unit %s .." % unit)
        if unit.hp <= 0: continue  # dead
        delta = breathFirstSearch(deepCopyOfRows(), unit)
        x,y = unit.location[0] + delta[0], unit.location[1] + delta[1]
        target = rows[y][x]
        if isinstance(target, Unit): #attack target
            print("Attacking %s .." % str(target))
            target.hp -= unit.attack
            if target.hp < 0: rows[y][x] = '.'
        else: # move unit
            print("Moving to (%d,%d) .." % (x,y))
            rows[unit.location[1]][unit.location[0]] = '.'
            rows[y][x] = unit
            unit.move(delta)
        pass
    pass
    printState()
pass
