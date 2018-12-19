import sys

#acres = list(map(lambda x: list(x.rstrip()), sys.stdin.readlines()))
acres = list(map(lambda x: list(x.rstrip()), open('input.dat').readlines()))

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

def calculateStuff(minutes, findPhase = False):
    global acres
    pstates = dict()  # state, turn
    for turn in range(minutes):
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

        woods = len(filter(lambda x: x == '|', [item for sublist in acres for item in sublist]))
        lumberjacks = len(filter(lambda x: x == '#', [item for sublist in acres for item in sublist]))
        fingerprint = woods * lumberjacks
        if findPhase:
            if fingerprint not in pstates.keys(): pstates[fingerprint] = []
            for pstate in pstates[fingerprint]:
                if pstate[0] == acres:
                    print "Found a previous state matching current state at turn %d vs %d .." % (pstate[1], turn)
                    return pstate[1], turn
                pass
            pass
            pstates[fingerprint].append((acres, turn))
        pass
        print ("(turn:%d) %d x %d => %d .. " % (turn, woods, lumberjacks, fingerprint))
    pass
pass

#calculateStuff(10, False)  # Answer1
pstate, currentstate = calculateStuff(20000, True)
phaselenght = currentstate - pstate
todo = 1000000000 - pstate
todo %= phaselenght
print("Working with a phaselenght of %d. Need to simulate an additional %d turns. " % (phaselenght, todo))
calculateStuff(pstate + todo, False)  # Answer 2 100466 too low 101840? 103224 102366 105183

