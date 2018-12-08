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

# list(string.ascii_uppercase).index('Z')

h,r = [], []
for x in sorted(set(list('ABCDEF')) - set(task2antecedents.keys())): heapq.heappush(h, x)

while len(h) > 0:
    antecedent = heapq.heappop(h)
    r.append(antecedent)
    if antecedent not in antecedent2tasks.keys(): continue
    for task in antecedent2tasks[antecedent]:
        task2antecedents[task].remove(antecedent)
        if len (task2antecedents[task]) == 0: heapq.heappush(h, task)
    pass
pass

print("".join(r))
