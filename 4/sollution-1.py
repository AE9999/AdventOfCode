#[1518-08-20 00:16] falls asleep

from dateutil.parser import parse
import numpy as np

def processShift(shift):
    start = shift[0]
    hours = np.zeros(60)
pass

inputs = list(sorted(map(lambda x: (parse(x[1:1 + len('1518-08-20 00:16')]), x.rstrip()),
                open('input.dat').readlines()),
                key = lambda x: x[0]))
shifts, shift = [], (0, [])

for input in inputs:
    if 'begins shift' in input[1]:
        shifts.append(shift)
        shift = (int(input[1].split(' ')[3][1:]), [])
    else:
        shift[1].append(input[1])
pass


