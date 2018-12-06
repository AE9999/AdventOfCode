import sys, collections, itertools
from itertools import groupby

inputs = list(map(lambda x: (int(x[0]), int(x[1])),
                  map(lambda x: x.rstrip().split(","), sys.stdin.readlines())))

minX, minY = sorted(inputs, key=lambda x: x[0], reverse=False)[0][0], \
             sorted(inputs, key=lambda x: x[1], reverse=False)[0][1]
maxX, maxY = sorted(inputs, key=lambda x: x[0], reverse=True)[0][0], \
             sorted(inputs, key=lambda x: x[1], reverse=True)[0][1]


#print (minX, minY, maxX, maxY)


rows = [] # * ((maxX+1) * (maxY+1) + 1) # labels round
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
    #print ("Considering (%d,%d) for %d at stept %d" % (activepoint[2][0], activepoint[2][1], activepoint[0], activepoint[1]))
    if field[1] < activepoint[1] or (activepoint[0] in field[0]):
        #print "\t Was already colered sooner .. "
        continue  # already colored
    #print ("\t Coloring it %d .. " % activepoint[0])
    field[0].append(activepoint[0])
    rows[activepoint[2][1]][activepoint[2][0]] = (field[0], activepoint[1])
    for delta in deltas:
        np = (activepoint[2][0] + delta[0], activepoint[2][1] + delta[1])
        if np[0] > maxX or np[0] < minX or np[1] > maxY or np[1] < minY:
            #infs.append(activepoint[0])
            continue
        queue.appendleft((activepoint[0], activepoint[1]+1, np))
    pass
pass

for y in range(maxY+1):
    row = []
    for x in range(maxX+1):
        field = rows[y][x]
        if (len(field[0]) == 0):
            row.append('x')
        elif (len(field[0]) > 1):
            row.append('.')
        else:
            c = chr(ord('a') + field[0][0])
            if field[1] == 0: c = c.upper()
            row.append(c)
        pass
    pass
    print row
pass

r = list((k, list(v)) for k, v in groupby(sorted(map(lambda x: x[0],
                                                     filter(lambda x: len(x) == 1,
                                                            map(lambda x: x[0],
                                                                list(itertools.chain(*rows))))))))

print("Done => %d .." % sorted(map(lambda x: len(x[1]), r), reverse=True)[0])





