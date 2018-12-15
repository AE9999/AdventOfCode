import sys, string, heapq
from itertools import groupby

rawLines = list(sys.stdin.readlines())

gb = groupby(sorted(map(lambda x: (x.rstrip().split()[7], x.rstrip().split()[1]), rawLines),
                    key=lambda x: x[0]),
             key=lambda x: x[0])
task2antecedents = dict((k, list(map(lambda x: x[1], v))) for k, v in gb)

gb = groupby(sorted(map(lambda x: (x.rstrip().split()[1], x.rstrip().split()[7]), rawLines),
                    key=lambda x: x[0]),
             key=lambda x: x[0])

antecedent2tasks = dict((k, list(map(lambda x: x[1], v))) for k, v in gb)

h, r, elves, maxElves, baseTime, ntasks = [], [], [], 5, 60, len(list(string.ascii_uppercase))

for x in sorted(set(list(string.ascii_uppercase)) - set(task2antecedents.keys())):
    heapq.heappush(h, (x, baseTime + list(string.ascii_uppercase).index(x) + 1)) # Name, Time

time = 0
while len(r) != ntasks:   
    while len(elves) < maxElves and len(h) > 0:        
        antecedent = heapq.heappop(h)
        elves.append(antecedent)
    pass
    
    elves = sorted(elves, key=lambda x: x[1], reverse=False)
    t = elves[0][1]
    time = time + t
    newElves = []
    for elf in elves:
        if elf[1] <= t:
            antecedent = elf[0]
            r.append(antecedent)
            if antecedent not in antecedent2tasks.keys(): continue
            for task in antecedent2tasks[antecedent]:
                task2antecedents[task].remove(antecedent)
                if len (task2antecedents[task]) == 0:
                    heapq.heappush(h, (task,
                                       baseTime + list(string.ascii_uppercase).index(task) + 1))
                pass
            pass
        else:
            newElves.append((elf[0], elf[1] - t))
        pass
    pass
    elves = newElves
pass

print("Done => Time: %d .." % time)
