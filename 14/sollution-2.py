import sys

input = str(sys.stdin.readline().rstrip())
recipes, elves = [3, 7], [0, 1]

def newRecipies(a,b):
    return list(map(lambda x: int(x), list(str(a+b))))

while len(recipes) < len(input) or "".join(map(lambda x: str(x), recipes[-len(input):])) != input:
    nr = newRecipies(recipes[elves[0]], recipes[elves[1]])
    print ("(%s) %d, %d => %s .." % (str(elves), recipes[elves[0]], recipes[elves[1]], str(nr)))
    for x in nr: recipes.append(x)
    elves = [ (x + 1 + recipes[x]) % len(recipes) for x in elves ]
    if len(recipes) % 100000 == 0: print("%d .." % len(recipes))
pass

print ("Found %s after %d recipes .." % (input, len(recipes) - len(input)))

