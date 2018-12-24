import re

class Group:
    def __init__(self, id, line, side, offset):
        self.id = id
        self.units = int(re.findall(r"(\d+) units", line)[0])
        self.hp = int(re.findall(r"(\d+) hit points", line)[0])
        self.weaknesses = []
        self.immunities = []
        self.side = side
        specials = re.findall(r"\((.*)\)", line)
        if len(specials) > 0:
            specials = specials[0].split(';')
            for special in specials:
                if 'weak to' in special:
                    self.weaknesses = special.lstrip().replace('weak to ', '').replace(',', '').split(' ')
                if 'immune to' in special:
                    self.immunities = special.lstrip().replace('immune to ', '').replace(',', '').split(' ')
        pass
        self.damage = re.findall(r"with an attack that does (\d+) (.+) damage", line)[0]  # damage,  type
        self.initative = int(re.findall(r"at initiative (\d+)", line)[0])
        self.offset = offset
    pass

    def __str__(self):
        return "%s group %d => Power: %d, Units: %d, Hp: %d, weaknesses:%s, immunities:%s, damage:(%s,%s), initative:%d, offset:%d" \
               % (self.side, self.id, self.power(),
                  self.units, self.hp, str(self.weaknesses), str(self.immunities),
                  self.damage[0], self.damage[1], self.initative, self.offset)
    pass

    def power(self): return self.units * (int(self.damage[0]) + self.offset)

    def death(self): return self.units == 0

    def attack(self, other):
        o = other.units
        other.units = other.units - int(self.potentialDammage(other) / other.hp)  # Fuck Python
        if other.units < 0: other.units = 0
        return o - other.units
    pass

    def potentialDammage(self, other):
        if self.damage[1] in other.immunities: return 0
        return (2 if self.damage[1] in other.weaknesses else 1) * self.power()

    def __eq__(self, other): return self.id == other.id and self.side == other.side

    def __hash__(self): return hash("%s-%d" % (self.side, self.id))
pass

def simulateBattle(offset):
    units, isID, ifId, readingImmune = [], 0, 0, True
    for line in open('input.dat').readlines():
        if line.rstrip() == 'Immune System:': continue
        if line.rstrip() == 'Infection:':
            readingImmune = False
            continue
        if line.rstrip() == '': continue
        if readingImmune:
            isID += 1
            units.append(Group(isID, line, 'Immune System', offset))
        else:
            ifId += 1
            units.append(Group(ifId, line, 'Infection', 0))
        pass
    pass

    def printState():
        print("Immune System:")
        for unit in filter(lambda x: x.side == 'Immune System',
                           sorted(units, key=lambda x: x.id)):
            print("Group %d contains %d units" % (unit.id, unit.units))
        pass
        print("Infection:")
        for unit in filter(lambda x: x.side == 'Infection',
                           sorted(units, key=lambda x: x.id)):
            print("Group %d contains %d units" % (unit.id, unit.units))
        pass
        print("")

    pass

    while len(set(map(lambda x: x.side,
                      filter(lambda x: not x.death(), units)))) > 1:
        # printState()
        units2targets = []
        currentTargets = set()
        for unit in sorted(list(filter(lambda x: not x.death(), units)),
                           key=lambda x: (x.power(), x.initative),
                           reverse=True):
            targets = sorted(list(filter(lambda x: x.side != unit.side and not x.death() and x not in currentTargets
                                         and unit.potentialDammage(x) > 0,
                                         units)),
                             key=lambda x: (unit.potentialDammage(x), x.power(), x.initative),
                             reverse=True)
            # for target in targets:
            #     print("%s %d would deal defending group %d %s damage" %
            #           (unit.side, unit.id, target.id, unit.potentialDammage(target)))
            # pass
            if len(targets) > 0:
                units2targets.append((unit, targets[0]))
                currentTargets.add(targets[0])
            pass
        pass

        # print("")
        deaths = 0
        for unit, target in sorted(units2targets,
                                   key=lambda x: x[0].initative,
                                   reverse=True):
            if unit.death(): continue
            deaths += unit.attack(target)
            # print("%s %d attacks defending group %d, killing %d units" %
            #       (unit.side, unit.id, target.id, deaths))
        pass
        if deaths == 0:
            print("Tie!, count as loss")
            return False, 0

    pass
    winner = list(set(map(lambda x: x.side, filter(lambda x: not x.death(), units))))[0]
    print("With offset:%d the winner is %s .." % (offset, winner))
    return winner == 'Immune System', sum(map(lambda x: x.units,
                                              list(filter(lambda x: not x.death(), units))))
pass

upperbound = 10
lowerbound = 1
while not simulateBattle(upperbound)[0]:
    lowerbound = upperbound
    upperbound *= 100
pass

def binary_search(lo, hi):
    # stolen from https://stackoverflow.com/questions/28389065/difference-between-basic-binary-search-for-upper-bound-and-lower-bound
    while lo < hi:
        mid = lo + (hi - lo) / 2
        print("Testing for bound %d .."  % mid)
        if simulateBattle(mid)[0]:
            hi = mid
        else:
            lo = mid + 1
    pass
    return lo
pass

result = binary_search(lowerbound, upperbound)

print("Lower bound is %d, %d .." % (result, simulateBattle(result)[1]))





