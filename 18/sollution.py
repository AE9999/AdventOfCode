import sys

#
myInput = sys.stdin
acres = list(map(lambda x: list(x.rstrip()), myInput.readlines()))

deltas = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

def ajacent(x,y):
    global acres, deltas
    return [acres[y + delta[1]][x + delta[0]] for delta in
            (filter(lambda d: x + d[0] >= 0
                           and y + d[1] >= 0 \
                           and x + d[0] < len(acres[0]) \
                           and y + d[1] < len(acres),  deltas))]
pass

def printAcres():
    global acres
    print("")
    for line in acres:
        print "".join(line)
pass

printAcres()
for turn in range(10):
    nextAcres = []
    for y in range(len(acres)):
        nrow = []
        for x in range(len(acres[0])):
            acre, nacre = acres[y][x], None
            if acre == '.':
                nacre = '|' if len(filter(lambda x: x == '|', ajacent(x, y))) >= 3 else '.'
            elif acre == '|':
                nacre = '#' if len(filter(lambda x: x == '#', ajacent(x, y))) >= 3 else '|'
            elif acre == '#':
                nacre = '#' if len(filter(lambda x: x == '|', ajacent(x, y))) >= 1 \
                               and len(filter(lambda x: x == '#', ajacent(x, y))) >= 1 else '.'
            pass
            nrow.append(nacre)
        pass
        nextAcres.append(nrow)
    pass
    acres = nextAcres
    printAcres()
pass

woods = len(filter(lambda x: x == '|', [item for sublist in acres for item in sublist]))
lumberjacks = len(filter(lambda x: x == '#', [item for sublist in acres for item in sublist]))
print ("%d x %d => %d .. " % (woods, lumberjacks, woods * lumberjacks))


