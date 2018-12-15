import sys, re

def parseline(line):
    r = [int(d) for d in re.findall(r'-?\d+', line)]
    return (r[0], r[1], r[2], r[3])
pass

inputs = list(map(parseline, sys.stdin.readlines()))

minX = sorted(inputs, key=lambda x: x[0])[0][0]
minY = sorted(inputs, key=lambda x: x[1])[0][1]
maxX = sorted(inputs, key=lambda x: x[0], reverse=True)[0][0]
maxY = sorted(inputs, key=lambda x: x[1], reverse=True)[0][1]

delta = (0 if minX > 0 else -1 * minX, 0 if minY > 0 else -1 * minY)

def addDelta(input):
    global delta
    return (input[0] + delta[0], input[1] + delta[1], input[2], input[3])
pass

def nextIter(input):
    return (input[0] + input[2], input[1] + input[3], input[2], input[3])
pass

def calculateBoundingBox(inputs):
    minX = sorted(inputs, key=lambda x: x[0])[0][0]
    minY = sorted(inputs, key=lambda x: x[1])[0][1]
    maxX = sorted(inputs, key=lambda x: x[0], reverse=True)[0][0]
    maxY = sorted(inputs, key=lambda x: x[1], reverse=True)[0][1]
    return ((maxX - minX) * (maxY - minY))
pass

def printBoundingBox(inputs):
    minX = sorted(inputs, key=lambda x: x[0])[0][0]
    minY = sorted(inputs, key=lambda x: x[1])[0][1]
    maxX = sorted(inputs, key=lambda x: x[0], reverse=True)[0][0]
    maxY = sorted(inputs, key=lambda x: x[1], reverse=True)[0][1]
    rows = list()
    for y in range(maxY - minY + 1): rows.append(['.'] * (maxX - minX + 1))
    for input in inputs: rows[input[1] - minY][input[0] - minX] = '#'
    for row in rows: print("".join(row))
pass

normalized = list(map(addDelta, inputs))
boundingBox = calculateBoundingBox(normalized)
for turn in range(maxX * maxY):
    print("Bounding box of size %d at turn %d" % (boundingBox, turn))
    next = list(map(nextIter, normalized))
    nextBoundingBox = calculateBoundingBox(next)
    if (nextBoundingBox > boundingBox):
        print ("Reached a local minimum at %d .." % turn)
        printBoundingBox(normalized)
        break
    pass
    boundingBox = nextBoundingBox
    normalized = next
pass