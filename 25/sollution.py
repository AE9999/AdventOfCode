import sys, re, uuid

class FourDPoint:
    def __init__(self, line):
        self.point = list(map(lambda x: int(x), re.findall(r'-?\d+', line)))

    def __str__(self): return "(FourDPoint: %s )" % (str(self.point))

    def distance(self, other):
        return sum([abs(self.point[i] - other.point[i]) for i in range(len(self.point))])
pass

class Constellation:
    def __init__(self, points):
        self.id = str(uuid.uuid4())
        self.points = points

    def add(self, point): self.points.append(point)

    def distance(self, point): return sorted(self.points, key=lambda x: x.distance(point))[0].distance(point)

    def merge(self, other): return Constellation(self.points + other.points)

    def __eq__(self, other): return self.id == other.id
pass


fourDpoints = list(map(FourDPoint, open('input.dat').readlines()))
constellations = [Constellation([fourDpoints[0]])]
for fourDpoint in fourDpoints[1:]:
    neighbours = list(filter(lambda x: x.distance(fourDpoint) <= 3, constellations))
    result = Constellation([fourDpoint])
    if neighbours:
        for neighbour in neighbours: result = result.merge(neighbour)
        constellations = [result] + list(filter(lambda x: x not in neighbours,
                                                constellations))
    else:
        constellations.append(result)
pass

print("%d constellations are formed by the fixed points in space time .." % (len(constellations)))