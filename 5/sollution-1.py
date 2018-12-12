import sys
import collections
import string

def doStuff(input):
    stack = collections.deque()
    for c in reversed(input):
        if len(stack) == 0:
            stack.appendleft(c)
            continue
        pass
        c_ = stack.popleft()
        if c.isupper() != c_.isupper() and c.upper() == c_.upper():
            pass
        else:
            stack.appendleft(c_)
            stack.appendleft(c)
        pass
    pass
    return len("".join(stack))
pass

def doMoreStuff(x):
    return (x[1], doStuff(x[0].replace(x[1], '').replace(x[1].upper(), '')))
pass

input = sys.stdin.readline().rstrip()

print("Sollution for 1: %d" % doStuff(input))

top = sorted(list(map(doMoreStuff, [(input, x) for x in string.ascii_lowercase])),
             key=lambda x: x[1])

print("Sollution for 2: %d" % top[0][1])

