import sys

def list2int(list): return int("".join(str(i) for i in list), 2)

def printState(state, generation = 0):
    low = state.index(1)
    high = len(state) - 1 - state[::-1].index(1)

    base = - ((generation) * 4)

    print("(%d, %d) => %s (%d)" % (low,
                                   high,
                                   "".join(["." if x == 0 else '#' for x in state[low:high+1]]),
                                   sum([state[x] * (x + base) for x in range(len(state))])))
pass

state =  list(map(lambda x: 0 if x == '.' else 1,
                  list(sys.stdin.readline().rstrip().split(' ')[2])))

transfers = dict(map(lambda x: (list2int(map(lambda x: 0 if x == '.' else 1, list(x[0]))), 0 if x[2] == '.' else 1),
                     map(lambda x: x.rstrip().split(' '),
                         filter(lambda x: len(x) > 2, sys.stdin.readlines()))))

for x in range(32):
    if x not in transfers.keys():
        transfers[x] = 0

def nextState(state):
    global transfers
    return state[0:2] + [transfers[list2int(state[(x-2):(x+3)])] for x in range(2, len(state) - 2)] + state[-2:]
pass

passes = 20
printState(state)
for generation in range(passes):
    state = nextState([0,0,0,0] + state + [0,0,0,0])
    printState(state, generation)
pass
