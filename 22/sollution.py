#depth, target, modvalue = 11109, (9, 731), 20183
depth, target, modvalue = 510, (10, 10), 20183

def geologicIndex(x,y):
    global target
    if x == 0 and y == 0: return 0
    if x == target[0] and y == target[1]: return 0
    if y == 0: return x * 16807
    if x == 0: return y * 48271
    return erosionLevel(x-1, y) * erosionLevel(x, y-1)
pass

def erosionLevel(x,y):
    global depth, target
    return (geologicIndex(x,y) + depth) % modvalue
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
        print("".join(list(map(printValue, [(x,y) for x in range(16)]))))
    pass
pass

printCavern()
#erosionLevel(1,1)
