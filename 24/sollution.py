import sys, re

class Unit:
    def __init__(self, line):
        self.units = int(re.findall(r"(\d+) units", line)[0])
        self.hp = int(re.findall(r"(\d+) hit points", line)[0])
        self.weaknesses = []
        self.immunities = []
        specials = re.findall(r"\((.*)\)", line)
        if len(specials) > 0:
            specials = specials[0].split(';')
            for special in specials:
                if 'weak to' in special:
                    self.weaknesses = list(re.findall(r"weak to (\w+)(, \w+)*", special)[0])
                if 'immune to' in special:
                    self.immunities = list(re.findall(r"immune to (\w+)(, \w+)*", special)[0])
        pass
        self.damage = re.findall(r"with an attack that does (\d+) (.+) damage", line)[0]
        self.initative = int(re.findall(r"at initiative (\d+)", line)[0])
    pass

    def __str__(self):
        return "Units: %d, Hp: %d, weaknesses:%s, immunities:%s, damage:(%d,%s), initative:%d" \
               % (self.units, self.hp, str(self.weaknesses), str(self.immunities), self.damage[0], self.damage[1],
                  self.initative)
    pass
pass

immuneSystem, infection, readingImmune = [], [], True

for line in open('input-test.dat').readlines():
    if line.rstrip() == 'Immune System:': continue
    if line.rstrip() == 'Infection:':
        readingImmune = False
        continue
    if line.rstrip() == '': continue
    (immuneSystem if readingImmune else infection).append(Unit(line))
pass



