import sys, collections

# inputs = list(map(lambda x: (int(x[0]), int(x[1])),
#                   map(lambda x: x.rstrip().split(","), sys.stdin.readlines())))

inputs = list(map(lambda x: (int(x[0]), int(x[1])),
                  map(lambda x: x.rstrip().split(","), open('example.dat'))))

print(inputs)

minX, minY = sorted(inputs, key=lambda x: x[0], reverse=False)[0][0], \
             sorted(inputs, key=lambda x: x[1], reverse=False)[0][1]
maxX, maxY = sorted(inputs, key=lambda x: x[0], reverse=True)[0][0], \
             sorted(inputs, key=lambda x: x[1], reverse=True)[0][1]


print (minX, minY, maxX, maxY)


rows = [] # * ((maxX+1) * (maxY+1) + 1) # labels round
for row in range(maxY+1):
    newRow = []
    for column in range(maxX+1):
        newRow.append(([], (maxY * maxX) + 1))
    pass
    rows.append(newRow)
pass
queue = collections.deque()
deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]


for i in range(len(inputs)): queue.appendleft((i, 0, inputs[i])) # label, round, coordinate
while len(queue) > 0:
    activepoint = queue.pop()
    field = rows[activepoint[2][1]][activepoint[2][0]]
    print ("Considering (%d,%d) for %d at stept %d" % (activepoint[2][0], activepoint[2][1], activepoint[0], activepoint[1]))
    if field[1] < activepoint[1]:
        print "\t Was already colered sooner .. "
        continue  # already colored
    field[0].append(activepoint[0])
    rows[activepoint[2][1]][activepoint[2][0]] = (field[0], activepoint[1])
    for delta in deltas:
        np = (activepoint[2][0] + delta[0], activepoint[2][1] + delta[1])
        if np[0] > maxX or np[0] < minX or np[1] > maxY or np[1] < minY:
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

print("Done ..")





