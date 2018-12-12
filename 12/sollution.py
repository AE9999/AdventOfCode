import sys

state = list(sys.stdin.readline().rstrip().split(' ')[2])

transfers = list(map(lambda x: (x[0], x[2]),
                     map(lambda x: x.rstrip().split(' '),
                         filter(lambda x: len(x) > 2, sys.stdin.readlines()))))