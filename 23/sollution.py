import sys, re
myInput = open('input-test.dat')

class Coordinate:
    def __init__(self, x, y, z): self.x, self.y, self.z = x, y, z

    def delta(self, delta): return Coordinate(self.x + delta, self.y + delta, self.z + delta)

    def plus(self, x, y, z): return Coordinate(self.x + x, self.y + y, self.z + z)

    def min(self, other): return Coordinate(min(self.x, other.x), min(self.y, other.y), min(self.z, other.z))

    def max(self, other): return Coordinate(max(self.x, other.x), max(self.y, other.y), max(self.z, other.z))
pass

class NanoBot:
    def __init__(self, line):
        ints = [int(d) for d in re.findall(r'-?\d+', line)]
        self.coordinate, self.r = Coordinate(ints[0:3]), ints[3]

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def toBoundingBox(self):
        bb = BoundingBox(self.coordinate.delta(- self.r), self.coordinate.delta(self.r))
        bb.nanoBots.append(self)
        return bb
pass

class BoundingBox:
    nanoBots = []
    def __init__(self, lower, upper): self.lower, self.upper = lower, upper

    def contains(self, point):
        return self.upper.x >= point.x >= self.lower.x and \
               self.upper.y >= point.y >= self.lower.y and \
               self.upper.z >= point.z >= self.lower.z

    def intersects(self, other):
        dx, dy, dz = self.upper.x - self.lower.x, self.upper.y - self.lower.y, self.upper.z - self.lower.z
        deltas = [(0,0,0), (dx, 0, 0), (0, dy, 0),  (0, 0, dz), (dx, 0, dz), (dx, dy, 0), (0, dy, dz), (dx, dy, dz)]
        return len(list(filter(other.contains, [self.lower.plus(delta) for delta in deltas])) > 0)

    def merges(self, other):
        self.lower, self.upper = self.lower.min(other.lower), self.upper.max(other.upper)
        self.nanoBots =  self.nanoBots + other.nanoBots
pass

nanobots = sorted(list(map(NanoBot, myInput)), key=lambda x: x.r, reverse=True)

print("In total, %d nanobots are in range of the nanobot with the largest signal radius." %
      len(filter(lambda x: nanobots[0].distance(x) <= nanobots[0].r, nanobots))) # Sollution 1

boundingBoxes = []
for nanobot in nanobots:
    for boundingBox in boundingBoxes:
        if boundingBox.intersects(nanobot.toBoundingBox()):
            boundingBox.merges(nanobot.toBoundingBox())