import sys

def list2int(list): return int("".join(str(i) for i in list), 2)

def printState(state):
    print("".join(["." if x == 0 else '#' for x in state]))

state = [0,0] + list(map(lambda x: 0 if x == '.' else 1,
                     list(sys.stdin.readline().rstrip().split(' ')[2]))) + [0, 0]

transfers = dict(map(lambda x: (list2int(map(lambda x: 0 if x == '.' else 1, list(x[0]))), 0 if x[2] == '.' else 1),
                     map(lambda x: x.rstrip().split(' '),
                         filter(lambda x: len(x) > 2, sys.stdin.readlines()))))

for x in range(32):
    if x not in transfers.keys():
        transfers[x] = 0

print(transfers)

def nextState(state):
    global transfers
    return [0, 0] + [ transfers[list2int(state[(x-2):(x+2)])] for x in range(2, len(state) - 2)] + [0, 0]
pass

for generation in range(20):
    printState(state)
    state = nextState(state)
pass