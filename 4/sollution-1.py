from dateutil.parser import parse
from itertools import zip_longest, groupby
import numpy as np
import sys

def processShift(shift):
    hours = np.zeros(60)
    # borrowed from https://stackoverflow.com/questions/1624883/alternative-way-to-split-a-list-into-groups-of-n
    for pair in zip_longest(*(iter(shift),) * 2):
        s = parse(pair[0][1:1 + len('1518-08-20 00:16')]).minute
        e = 60
        if (pair[1] != None):
            e = parse(pair[1][1:1 + len('1518-08-20 00:16')]).minute
        pass
        hours[s:e] = np.ones(e - s)
    pass
    return hours
pass

def calculateSameMinute(item):
    result = np.array(list(map(lambda x: x[1], item[1])))
    minutes = result.sum(axis=0)
    rvalue = minutes[np.argmax(minutes)]
    return rvalue
pass

def calculateWeight(item):
    return sum(map(lambda x: x[1].sum(), list(item[1])))
pass

inputs = list(sorted(map(lambda x: (parse(x[1:1 + len('1518-08-20 00:16')]), x.rstrip()),
                sys.stdin.readlines()),
                key = lambda x: x[0]))

shifts, rawLines = [], (-1, [])

for input in inputs:
    if 'begins shift' in input[1]:
        if rawLines[0] >= 0:
            hours = processShift(rawLines[1])
            a = (rawLines[0], hours)
            shifts.append(a)
        rawLines = (int(input[1].split(' ')[3][1:]), [])
    else:
        rawLines[1].append(input[1])
pass
hours = processShift(rawLines[1])
a = (rawLines[0], hours)
shifts.append(a)

# https://stackoverflow.com/questions/6236081/python-groupby-behaviour
shifts = sorted(shifts, key=lambda x: x[0])
byGuards = list((k, list(v)) for k, v in groupby(shifts,
                                                 key=lambda  x: x[0]))
s = sorted(byGuards, key=calculateWeight, reverse=True)
result = np.array(list(map(lambda x: x[1], s[0][1])))
minutes = result.sum(axis= 0)
print ("Done => " + str(np.argmax(minutes) * s[0][0]))

s = sorted(byGuards, key=calculateSameMinute, reverse=True)
result = np.array(list(map(lambda x: x[1], s[0][1])))
minutes = result.sum(axis= 0)
print ("Done => " + str(np.argmax(minutes) * s[0][0]))
