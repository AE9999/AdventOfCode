import sys, collections, itertools
from itertools import groupby

inputs = list(map(lambda x: (int(x[0]), int(x[1])),
                  map(lambda x: x.rstrip().split(","), sys.stdin.readlines())))

minX, minY = sorted(inputs, key=lambda x: x[0], reverse=False)[0][0], \
             sorted(inputs, key=lambda x: x[1], reverse=False)[0][1]
maxX, maxY = sorted(inputs, key=lambda x: x[0], reverse=True)[0][0], \
             sorted(inputs, key=lambda x: x[1], reverse=True)[0][1]

rows = [] # labels round
for row in range(maxY+1):
    newRow = []
    for column in range(maxX+1): newRow.append(([], (maxY * maxX) + 1))
    rows.append(newRow)
pass

queue = collections.deque()
deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]
infs = []

for i in range(len(inputs)): queue.appendleft((i, 0, inputs[i])) # label, round, coordinate
while len(queue) > 0:
    activepoint = queue.pop()
    field = rows[activepoint[2][1]][activepoint[2][0]]
    if field[1] < activepoint[1] or (activepoint[0] in field[0]): continue  # already colored
    field[0].append(activepoint[0])
    rows[activepoint[2][1]][activepoint[2][0]] = (field[0], activepoint[1])
    for delta in deltas:
        np = (activepoint[2][0] + delta[0], activepoint[2][1] + delta[1])
        if np[0] > maxX or np[0] < minX or np[1] > maxY or np[1] < minY:
            if field[0][0] not in infs: infs.append(field[0][0]) # infinate color
            continue
        queue.appendleft((activepoint[0], activepoint[1]+1, np))
    pass
pass

r = list((k, list(v)) for k, v in groupby(sorted(map(lambda x: x[0],
                                                     filter(lambda x: len(x) == 1 and x[0] not in infs,
                                                            map(lambda x: x[0],
                                                                list(itertools.chain(*rows))))))))

print("Done => %d .." % sorted(map(lambda x: len(x[1]), r), reverse=True)[0])