import sys

input = int(sys.stdin.readline().rstrip())

recipes, elves = [3, 7], [0, 1]

def newRecipies(a,b):
    return list(map(lambda x: int(x), list(str(a+b))))

while len(recipes) <= input + 9:
    recipes += newRecipies(recipes[elves[0]], recipes[elves[1]])
    elves = [ (x + 1 + recipes[x]) % len(recipes) for x in elves ]
pass

print ("".join(map(lambda x: str(x), recipes[input:input+10])))  # Solution 1
