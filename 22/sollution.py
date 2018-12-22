import sys
from collections import deque

#depth, target, modvalue = 11109, (9, 731), 20183
depth, target, modvalue = 510, (10, 10), 20183
additionalRatio = 1
maxInt = sys.maxint
gcache = [[ -1 for x in range(target[0] + 2) ] for y in range(target[1] + 2) ]
ecache = [[ -1 for x in range(target[0] + 2) ] for y in range(target[1] + 2) ]
# Neither, Torch, Climbing Gear
costTable = [[(maxInt - 1, maxInt - 1,  maxInt - 1) for x in range(target[0] + 1 + additionalRatio)] for y in range(target[1] + 1 + additionalRatio) ]
globalMin = maxInt

def geologicIndex(x,y):
    global target, gcache
    if gcache[y][x] != -1: v = gcache[y][x]
    elif x == 0 and y == 0: v = 0
    elif x == target[0] and y == target[1]: v =0
    elif y == 0: v = x * 16807
    elif x == 0: v = y * 48271
    else: v = erosionLevel(x-1, y) * erosionLevel(x, y-1)
    gcache[y][x] = v
    return v
pass

def erosionLevel(x,y):
    global depth, target, ecache
    if ecache[y][x] != -1: v = ecache[y][x]
    else: v = (geologicIndex(x,y) + depth) % modvalue
    ecache[y][x] = v
    return v % 3
pass

def printValue((x,y)):
    global target
    if x == 0 and y == 0: return 'M'
    if x == target[0] and y == target[1]: return 'T'
    e = erosionLevel(x, y) % 3
    if e == 0: return '.'  # Rocky
    if e == 1: return '='  # Wet
    if e == 2: return '|'  # Narrow
pass

def printCavern():
    for y in range(target[1] + 1):
        print("".join(list(map(printValue, [(x,y) for x in range(target[0] + 1)]))))
    pass
pass

def sol1(): return sum(erosionLevel(x, y) % 3 for x in range(target[0] + 1) for y in range(target[1] + 1))

def cost(source, destination):
    if destination[0] < 0 or \
       destination[0] >= target[0] + additionalRatio or \
       destination[1] < 0 or \
       destination[1] >= target[1] + additionalRatio:
        return (maxInt, maxInt, maxInt)
    pass
    baseCost = costTable[source[1]][source[0]]
    dSource = erosionLevel(destination[0], destination[1])
    if dSource == 0: # Rocky
        neitherCost = baseCost[0] + 8
        climbingCost = baseCost[1] + 1
        torchCost = baseCost[2] + 1
    elif dSource == 1: # Wet
        neitherCost = baseCost[0] + 1
        climbingCost = baseCost[1] + 1
        torchCost = baseCost[2] + 8
    elif dSource == 2: # Narrow
        neitherCost = baseCost[0] + 1
        climbingCost = baseCost[1] + 1
        torchCost = baseCost[2] + 8
    if destination[0] == target[0] and destination[1] == target[1]:
        climbingCost += 7
    # Neither, Torch, Climbing Gear
    return (neitherCost,  # Neither
            climbingCost,  # Torch
            torchCost)  # Climbin gear
pass

def sol2():
    global costTable, globalMin
    deltas = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    costTable[target[1]][target[0]] = (0, 0, 0)
    queue = deque()
    queue.appendleft((target[0], target[1]))
    while len(queue) > 0:
        x1, y1 = queue.pop()
        print("Analyzing %d,%d .." % (x1, y1))
        for delta in deltas:
            x2, y2 = x1 + delta[0], y1 + delta[1]
            currentCosts = costTable[y2][x2]
            potentialCosts = cost((x1,y1), (x2, y2))
            newCosts = (min(currentCosts[0], potentialCosts[0]),
                        min(currentCosts[1], potentialCosts[1]),
                        min(currentCosts[2], potentialCosts[2]))
            costTable[y2][x2] = newCosts
            print("\tConsidering (%d,%d) => currentCosts:%s, potentialCosts:%s newCosts:%s" % (x2,
                                                                                             y2,
                                                                                             str(currentCosts),
                                                                                             str(potentialCosts),
                                                                                             str(newCosts)))
            if x2 == 0 and y2 == 0: # Beginning
                globalMin = min(globalMin, min(newCosts))
                print("Current global Min: %d .." % globalMin)
            if (newCosts[0] < currentCosts[0] or newCosts[1] < currentCosts[1] or newCosts[2] < currentCosts[2]) \
                and (x2 != 0 or y2 != 0) \
                and min(newCosts) <= globalMin:
                print("\t\tAppending %d,%d .." % (x2,y2))
                queue.appendleft((x2, y2))
        pass
    pass
pass

print("Total risk level for the smallest rectangle is %d .." % sol1())

sol2()
print("Shortest path is %s .." % str(costTable[0][0]))
