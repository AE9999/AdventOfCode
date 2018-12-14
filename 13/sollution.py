import sys

input = sys.stdin
#input =  open('input.dat')
rows = list(map(lambda x: list(x.rstrip()),  input.readlines()))
carts = []

def replaceCart(x, y):
    global rows
    up = None if  y < 1 else rows[y-1][x]
    down = None if (y + 1) == len(rows) else rows[y+1][x]
    left = None if (x < 1) else rows[y][x-1]
    right = None if (x+1) == len(rows[y]) else rows[y][x+1]
    if not set(['^', '>', 'v', '>']).isdisjoint(set([up, down, left, right])): raise Exception('invalid assumption')

    canGoUp = up is not None and up in "|/\\+"
    canGoDown = down is not None and down in "|+\\/"
    canGoLeft = left is not None and left in "+-\\/"
    canGoRight = right is not None and right in "+-\\/"
    if canGoUp + canGoDown + canGoLeft + canGoRight == 1 \
       or canGoUp + canGoDown + canGoLeft + canGoRight == 3:
        raise Exception('invalid assumption')
    if canGoUp and canGoDown and canGoLeft and canGoRight:
        return '+'
    elif canGoLeft and canGoRight:
        return '-'
    elif canGoUp and canGoDown:
        return '|'
    elif (canGoLeft and canGoDown) or (canGoRight and canGoUp):
        return '\\'
    elif (canGoRight and canGoDown) or (canGoUp and canGoLeft):
        return '/'
    else:
        raise Exception('invalid assumption')
    pass
pass

def handleDirection(direction, turn):
    t = turn % 3
    if direction == '>':
        if t == 0: return '^', (0, -1)
        if t == 1: return '>', (1, 0)
        if t == 2: return 'v', (0, 1)
    if direction == '<':
        if t == 0: return 'v', (0, 1)
        if t == 1: return '<', (-1, 0)
        if t == 2: return '^', (0, -1)
    if direction == 'v':
        if t == 0: return '>', (1, 0)
        if t == 1: return 'v', (0, 1)
        if t == 2: return '<', (-1, 0)
    if direction == '^':
        if t == 0: return '<', (-1, 0)
        if t == 1: return '^', (0, -1)
        if t == 2: return '>', (1, 0)
pass


def nextState(cart):
    global rows
    direction, x, y, turns = cart[0], cart[1][0], cart[1][1], cart[2]
    cc = rows[cart[1][1]][cart[1][0]]
    if cc == '-':
        if direction == '<': return (direction, (x-1, y), turns)
        if direction == '>': return (direction, (x+1, y), turns)
        raise Exception('invalid assumption')
        pass
    elif cc == '|':
        if direction == '^': return (direction, (x, y - 1), turns)
        if direction == 'v': return (direction, (x, y + 1), turns)
        raise Exception('invalid assumption')
        pass
    elif cc == '/':
        if direction == '<': return ('v', (x, y + 1), turns)
        if direction == '>': return ('^', (x, y - 1), turns)
        if direction == '^': return ('>', (x+1, y), turns)
        if direction == 'v': return ('<', (x-1, y), turns)
        raise Exception('invalid assumption')
        pass
    elif cc == '\\':
        if direction == '>': return ('v', (x, y+1), turns) # CORRECT
        if direction == '<': return ('^', (x, y-1), turns)
        if direction == '^': return ('<', (x-1, y), turns)
        if direction == 'v': return ('>', (x+1, y), turns)
        pass
    elif cc == '+':
        ndirection, delta = handleDirection(direction, turns)
        return (ndirection,(x + delta[0], y + delta[1]) ,turns +1)
    else:
        raise Exception('invalid assumption')
    pass
pass

for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] in "^<>v":
            carts.append((rows[y][x], (x,y), 0)) # direction, position, turnstaken
            rows[y][x] = replaceCart(x, y)
        pass
    pass
pass

turn = 1
while True:
    print ("Simulating turn %d .. " % turn)
    nextCarts = []
    carts = list(sorted(carts, key=lambda x: x[1]))
    for i in range(len(carts)):
        print ("\tStep %d .." % (i))
        nCart = nextState(carts[i])
        if nCart[1][0] < 0 or nCart[1][1] < 0: raise Exception('invalid assumption')
        if nCart[1][1] >= len(rows): raise Exception('invalid assumption')
        if nCart[1][0] >= len(rows[nCart[1][1]]): raise Exception('invalid assumption')
        if rows[nCart[1][1]][nCart[1][0]] is None or rows[nCart[1][1]][nCart[1][0]] not in "><^v+\\/|-":
            raise Exception('invalid assumption')
        nextState(nCart)
        collisions = list(filter(lambda x: x[1] == nCart[1], carts[i+1:])) + \
                     list(filter(lambda x: x[1] == nCart[1], nextCarts))
        if len(collisions) > 0:
            print("Collision at turn %d, between %s and %s" % (turn, nCart, collisions[0])) # sollution 1
            break
        pass
        nextCarts.append(nCart)
    pass
    if len(carts) != len(nextCarts): break
    carts = nextCarts
    turn += 1
pass