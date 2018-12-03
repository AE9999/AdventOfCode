import itertools

for pair in itertools.combinations(list(map(lambda x: x.rstrip(), open('input1.dat').readlines())), 2):
    if len(list(filter(lambda x: x[0] != x[1], zip(pair[0], pair[1])))) ==1:
        print (''.join(list(map(lambda x: x[0], filter(lambda x: x[0] == x[1], zip(pair[0], pair[1]))))))
pass
