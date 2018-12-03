from collections import Counter
boxes = list(map(lambda x: Counter(x.rstrip()), open('input1.dat').readlines()))
twos = []
threes = []
for box in boxes:
    seen2 = False
    seen3 = False
    for k in box.keys():
        if box[k] == 3 and not seen3:
            threes.append(k)
            seen3 = True
        if box[k] == 2 and not seen2:
            twos.append(k)
            seen2 = True
    pass
pass
print ("2s: " + str(len(twos)) + "  3s: " + str(len(threes)) + "  => " + str(len(threes) * len(twos)))






