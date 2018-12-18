import sys

#sys.stdin
myInput = open('input-test.dat')
acres = list(map(lambda x: list(x.rstrip()), myInput.readlines()))

deltas = [(-1, -1), (0,-1), (1,-1), (-1, 0), (1, 0), (-1, 1), (1, 0), (1, 1) ]

def ajacent(x,y):
    global acres, deltas
    return [acres[y + delta[1]][x + delta[0]] for delta in
            (filter(lambda d: x + d[0] >= 0 and y + d[1] >= 1,  deltas))]
pass

print ajacent(0,0)

