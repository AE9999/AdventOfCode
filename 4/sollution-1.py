#[1518-08-20 00:16] falls asleep

from dateutil.parser import parse
from itertools import zip_longest, groupby
import numpy as np



def processShift(shift):
    hours = np.zeros(60)
    # borrowed from https://stackoverflow.com/questions/1624883/alternative-way-to-split-a-list-into-groups-of-n
    for pair in zip_longest(*(iter(shift),) * 2):
        #print(pair)
        s = parse(pair[0][1:1 + len('1518-08-20 00:16')]).minute
        e = 60
        if (pair[1] != None):
            e = parse(pair[1][1:1 + len('1518-08-20 00:16')]).minute - 1
        pass
        hours[s:e] = np.ones(e - s)
    pass
    return hours
pass

# def handleCounts(it):
#     map(lambdax x: x[2]  it[2])
# pass

def calculateWeight(item):
    return sum(map(lambda x: x[1].sum(), item[1]))
pass

def comp(l, r):
    return calculateWeight(l[1]) - calculateWeight(r[1])
pass

inputs = list(sorted(map(lambda x: (parse(x[1:1 + len('1518-08-20 00:16')]), x.rstrip()),
                open('input.dat').readlines()),
                key = lambda x: x[0]))
shifts, rawLines = [], (-1, [])

for input in inputs:
    if 'begins shift' in input[1]:
        if rawLines[0] >= 0: shifts.append((rawLines[0], hours))
        hours = processShift(rawLines[1])
        rawLines = (int(input[1].split(' ')[3][1:]), [])
    else:
        rawLines[1].append(input[1])
pass
for shift in shifts:
    print (shift)

byGuards = list(groupby(shifts, lambda  x: x[0]))
s = sorted(byGuards, key=calculateWeight)

#for byGuard in s:
#    print(s)






