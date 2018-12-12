import sys

state = [0,0] + list(map(lambda x: 0 if x == '.' else 1,
                     list(sys.stdin.readline().rstrip().split(' ')[2])))

print (state)

transfers = list(map(lambda x: (map(lambda x: 0 if x == '.' else 1, list(x[0])), 0 if x[2] == '.' else 1),
                     map(lambda x: x.rstrip().split(' '),
                         filter(lambda x: len(x) > 2, sys.stdin.readlines()))))

print (transfers)