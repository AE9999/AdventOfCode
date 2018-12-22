#depth, target, modvalue = 11109, (9, 731), 20183
depth, target, modvalue = 510, (10, 10), 20183
gcache = [[ -1 for x in range(target[0] + 1) ] for y in range(target[1] + 1) ]
ecache = [[ -1 for x in range(target[0] + 1) ] for y in range(target[1] + 1) ]

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
    return v
pass

def printValue((x,y)):
    global target
    if x == 0 and y == 0: return 'M'
    if x == target[0] and y == target[1]: return 'T'
    e = erosionLevel(x, y) % 3
    if e == 0: return '.'
    if e == 1: return '='
    if e == 2: return '|'
pass

def printCavern():
    for y in range(target[1] + 1):
        print("".join(list(map(printValue, [(x,y) for x in range(target[0] + 1)]))))
    pass
pass

def sol1(): return sum(erosionLevel(x, y) % 3 for x in range(target[0] + 1) for y in range(target[1] + 1))

print("Total risk level for the smallest rectangle is %d .." % sol1())
