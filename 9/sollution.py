import sys

class MyNode:
    def __init__(self, stone=0, l=None, r=None):
        self.stone = stone
        self.l = l if l is not None else self
        self.r = r if r is not None else self
        if l is not None: l.r = self
        if r is not None: r.l = self
    pass

    def right(self, index):
        return self if (index == 0) else self.r.right(index - 1)
    pass

    def left(self, index):
        return self if (index == 0) else self.l.left(index - 1)
    pass

    def remove(self):
        self.l.r, self.r.l = self.r, self.l
    pass
pass

input = list(map(lambda x: int(x),
                 filter(lambda x: x.isdigit(), sys.stdin.readline().split(' '))))
stone, players, circle = 0, [0] * int(input[0]), MyNode()

for stone in range(1, input[1] + 1):
    if stone % 23 != 0:
        next = circle.right(2)
        circle = MyNode(stone, next.l, next)
    else:
        toRemove = circle.left(7)
        circle = toRemove.r
        toRemove.remove()
        players[(stone % len(players)) - 1] = players[(stone % len(players)) - 1] + stone + toRemove.stone
    pass
pass

print("Game Over. Max Score %d .." % sorted(players, reverse=True)[0])
# Solved part 2 by adding to zeros to my input
