# solution for one was obtained by `cat input | awk '{s+=$1; print s;} END {print s}'`

frequency = list(map(lambda x : int(x.rstrip()), open('input').readlines()))
seen = {}
f = 0
i = 0
while True:
    if not seen.has_key(f):
        print "Not seen " + str(f)
        seen[f] = 1
        f = f + frequency[i % len(frequency)]
        i = i + 1
    else:
        print "Already seen " + str(f)
        break
    pass
pass
