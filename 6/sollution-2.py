import sys, collections, math
import numpy as np

range = 10000

inputs = list(map(lambda x: (int(x[0]) + range, int(x[1]) + range),
                  map(lambda x: x.rstrip().split(","), sys.stdin.readlines())))

minX, minY = sorted(inputs, key=lambda x: x[0], reverse=False)[0][0] - range, \
             sorted(inputs, key=lambda x: x[1], reverse=False)[0][1] - range
maxX, maxY = sorted(inputs, key=lambda x: x[0], reverse=True)[0][0] - range, \
             sorted(inputs, key=lambda x: x[1], reverse=True)[0][1] - range

def calculateDistance(x, y):
    return sum(map(lambda input: abs(x - input[0]) + abs(y - input[1]), inputs))
pass

todo = collections.deque()
board = np.zeros((maxX + (range *2), maxY + (range*2)))
deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]

start = (math.floor(((minX + range) + (maxX + range)) / 2),
         math.floor(((minY + range) + (maxY + range)) / 2))

if not calculateDistance(start[0], start[1]) < range:
    print ("Yo fucked now!")
    sys.exit(1)
pass

todo.append(start)

while len(todo) > 0:
    activepoint = todo.pop()
    for delta in deltas:
        newPoint = (activepoint[0] + delta[0], activepoint[1] + delta[1])
        x, y = newPoint[0], newPoint[1]
        if calculateDistance(x, y) < range and board[x][y] == 0:
            board[x][y] = 1
            todo.appendleft((x,y))
        pass
    pass
pass

print("Done %d .. " % board.sum())


