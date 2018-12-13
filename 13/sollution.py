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

def nextState(cart):
    global rows
    direction, x, y, turn, cc = cart[0], cart[1][0], cart[1][1], cart[2], rows[cart[1][1]][cart[1][0]]
    ndirection, delta = '', (0,0)
    if cc == '-' or cc == '|':
        ndirection = direction
    elif cc == '/':
        if direction == '<': ndirection = 'v'
        if direction == '>': ndirection = '^'
        if direction == '^': ndirection = '>'
        if direction == 'v': ndirection = '<'
        pass
    elif cc == '\\':
        if direction == '>': ndirection = 'v'
        if direction == '<': ndirection = '^'
        if direction == '^': ndirection = '<'
        if direction == 'v': ndirection = '>'
        pass
    elif cc == '+':
        if direction == '>':
            if turn % 3 == 0: ndirection = '^'
            if turn % 3 == 1: ndirection = '>'
            if turn % 3 == 2: ndirection = 'v'
        elif direction == '<':
            if turn % 3 == 0: ndirection = 'v'
            if turn % 3 == 1: ndirection = '<'
            if turn % 3 == 2: ndirection = '^'
        elif direction == 'v':
            if turn % 3 == 0: ndirection = '>'
            if turn % 3 == 1: ndirection = 'v'
            if turn % 3 == 2: ndirection = '<'
        elif direction == '^':
            if turn % 3 == 0: ndirection = '<'
            if turn % 3 == 1: ndirection = '^'
            if turn % 3 == 2: ndirection = '>'
        pass
    pass
    if ndirection == '>': delta = (1, 0)
    if ndirection == '<': delta = (-1, 0)
    if ndirection == 'v': delta = (0, 1)
    if ndirection == '^': delta = (0, -1)

    return (ndirection,(x + delta[0], y + delta[1]), turn +1 if cc == '+' else turn)
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