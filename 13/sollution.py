import sys

rows = list(map(lambda x: list(x.rstrip()),  sys.stdin.readlines()))

carts = []

def replaceCart(x, y):
    global rows
    pass
pass

def nextStateCarte(cart):
    global rows
    direction, x, y, turns = cart[0], cart[1][0], cart[1][1], cart[2]
    cc = rows[cart[1][1]][cart[1][0]]
    if cc == '-':
        if direction == '<':
            return (direction, (x-1, y), turns)
        if direction == '>':
            return (direction, (x+1, y), turns)
        pass
    if cc == '/':
        if direction == '<':
            return ('v', (x, y - 1), turns)
        if direction == '^':
            return ('>', (x+1, y), turns)
        pass
    if cc == '+':
        pass
    if cc == '\\':
        if direction == '>':
            return ('v', (x, y - 1), turns)
        if direction == '^':
            return ('<', (x+1, y), turns)
        pass
    if cc == '|':
        if direction == '^':
            return (direction, (x, y - 1), turns)
        if direction == 'v':
            return (direction, (x, y + 1), turns)
        pass
    pass
pass

for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] in "^<>v":
            carts.append((rows[y][x], (x,y), 0)) # direction, position turnstaken
            rows[y][x] = replaceCart(x, y)
        pass
    pass
pass

turn = 0
while True:
    carts = [ nextState(cart) for cart in carts ]
    turn += 1
pass


