import sys
import numpy as np

serial = 18 # int(sys.stdin.readline().rstrip())

def powerLevel(x,y,serial):
    rackId = (x + 10)
    powerLevel = rackId * (y)
    powerLevel = powerLevel + serial
    powerLevel = powerLevel * rackId
    powerLevel = int(str(powerLevel)[-3])
    return powerLevel - 5
pass

xdim, ydim = 300, 300
grid = np.zeros((300, 300))
for y in range(ydim):
    for x in range(xdim):
        grid[x][y] = powerLevel(x + 1, y + 1, serial)
    pass
pass

def doStuff(squaresize):

    candidateSquares = []
    for y in range(ydim - squaresize):
        for x in range(xdim - squaresize):
            candidateSquares.append((grid[x:x + squaresize, y:y + squaresize].sum(),
                                    (x, y)))  # (sum, (coordinates))
        pass
    pass

    result = sorted(candidateSquares, key=lambda x: x[0], reverse=True)[0]
    print("Best spot for square %d: is (%d, %d) with power %d"
          % (squaresize, result[1][0] + 1, result[1][1] + 1, result[0]))
    return (result, squaresize)
pass

all = []
for x in range(300):
    all.append(doStuff(x))

result = sorted(all, key=lambda x: x[0][0], reverse=True)[0]

print("Answer: %d,%d,%d" % (result[0][1][0] + 1,  result[0][1][1] + 1, result[1]))








