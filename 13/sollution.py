import sys

rows, carts = list(map(lambda x: list(x.rstrip()),  sys.stdin.readlines())), []

def replaceCart(x, y):
    global rows
    up = None if y < 1 else rows[y-1][x]
    down = None if (y + 1) == len(rows) else rows[y+1][x]
    left = None if (x < 1) else rows[y][x-1]
    right = None if (x+1) == len(rows[y]) else rows[y][x+1]

    canGoUp = up is not None and up in "|/\\+"
    canGoDown = down is not None and down in "|+\\/"
    canGoLeft = left is not None and left in "+-\\/"
    canGoRight = right is not None and right in "+-\\/"

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
    pass
pass

def handleDirection(direction, turn):
    if direction == '>':
        if turn % 3 == 0: return '^', (0, -1)  # Delta return stuff is actually superflous
        if turn % 3 == 1: return '>', (1, 0)
        if turn % 3 == 2: return 'v', (0, 1)
    elif direction == '<':
        if turn % 3 == 0: return 'v', (0, 1)
        if turn % 3 == 1: return '<', (-1, 0)
        if turn % 3 == 2: return '^', (0, -1)
    elif direction == 'v':
        if turn % 3 == 0: return '>', (1, 0)
        if turn % 3 == 1: return 'v', (0, 1)
        if turn % 3 == 2: return '<', (-1, 0)
    elif direction == '^':
        if turn % 3 == 0: return '<', (-1, 0)
        if turn % 3 == 1: return '^', (0, -1)
        if turn % 3 == 2: return '>', (1, 0)
    pass
pass

def nextState(cart):
    global rows
    direction, x, y, turns, cc = cart[0], cart[1][0], cart[1][1], cart[2], rows[cart[1][1]][cart[1][0]]
    if cc == '-':
        if direction == '<': return (direction, (x-1, y), turns)
        if direction == '>': return (direction, (x+1, y), turns)
        pass
    elif cc == '|':
        if direction == '^': return (direction, (x, y - 1), turns)
        if direction == 'v': return (direction, (x, y + 1), turns)
        pass
    elif cc == '/':
        if direction == '<': return ('v', (x, y + 1), turns)
        if direction == '>': return ('^', (x, y - 1), turns)
        if direction == '^': return ('>', (x+1, y), turns)
        if direction == 'v': return ('<', (x-1, y), turns)
        pass
    elif cc == '\\':
        if direction == '>': return ('v', (x, y+1), turns)
        if direction == '<': return ('^', (x, y-1), turns)
        if direction == '^': return ('<', (x-1, y), turns)
        if direction == 'v': return ('>', (x+1, y), turns)
        pass
    elif cc == '+':
        ndirection, delta = handleDirection(direction, turns)
        return (ndirection,(x + delta[0], y + delta[1]) ,turns +1)
    pass
pass

for y in range(len(rows)):
    for x in range(len(rows[y])):
        if rows[y][x] in "^<>v":
            carts.append((rows[y][x], (x,y), 0))  # direction, position, turnstaken
            rows[y][x] = replaceCart(x, y)
        pass
    pass
pass

while len(carts) != 1:
    nextCarts = []
    carts = list(sorted(carts, key=lambda x: x[1]))
    for i in range(len(carts)):
        if carts[i] is None: continue
        nCart = nextState(carts[i])
        oldCollisions = list(filter(lambda x: x[1] == nCart[1], carts[i + 1:]))
        newCollisions = list(filter(lambda x: x[1] == nCart[1], nextCarts))
        if len(oldCollisions) > 0:
            print("Collision between %s and %s" % (nCart, oldCollisions[0]))  # sollution 1
            carts[carts.index(oldCollisions[0])] = None
        elif len(newCollisions) > 0:
            print("Collision between %s and %s" % (nCart, newCollisions[0])) # sollution 1
            nextCarts.remove(newCollisions[0])
        else:
            nextCarts.append(nCart)
        pass
    pass
    carts = nextCarts
pass
print ("Only one cart remains %s .." % str(carts[0]))