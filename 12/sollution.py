import sys

def list2int(list): return int("".join(str(i) for i in list), 2)

def calculateSum(state, generation):
    base = - ((generation) * 4)
    return sum([state[x] * (x + base) for x in range(len(state))])
pass

def getActiveState(state):
    low = state.index(1)
    high = len(state) - 1 - state[::-1].index(1)
    return state[low:high+1]
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

passes = 20000
for generation in range(passes):
    pstate = state
    pactiveState = getActiveState(state)
    state = nextState([0,0,0,0] + state + [0,0,0,0])
    if generation + 1 == 20:
        print ("Current score at generation 20 => %d .." % calculateSum(state, generation + 1))  # Solution 1
    if pactiveState == getActiveState(state):
        ngen = 50000000000 - (generation + 1)
        currentScore = calculateSum(state, generation + 1)
        increment = (calculateSum(state, generation + 1) - calculateSum(pstate, generation))
        print ("Equilibrium reached at Generation: %d, current score %d, increment %d .. "
               % ((generation + 1), currentScore, increment))
        print ("Expected score at 50000000000 => %s  .." % ((ngen * increment) + currentScore))  # Solution 2
        break
    pass
pass
