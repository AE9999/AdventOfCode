import sys

input = str(sys.stdin.readline().rstrip())
recipes, elves = "37", [0, 1]

def newRecipies(a,b):
    return str(int(a) + int(b))

# Fuck Python and its string addition n^2 complexity.
while len(recipes) < len(input) or recipes.find(input) == -1:
    recipes += newRecipies(recipes[elves[0]], recipes[elves[1]])
    elves = [ (x + 1 + int(recipes[x])) % len(recipes) for x in elves ]
    print(recipes)
pass

print ("Found %s after %d recipes .." % (input, recipes.find(input)))

