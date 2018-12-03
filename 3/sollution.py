import numpy as np

fabric = np.zeros((1000, 1000))
# #1 @ 335,861: 14x10
inputs = list(map(lambda x: x.rstrip().split(' '), open('input.dat').readlines()))

# https://www.programiz.com/python-programming/matrix
for input in inputs:
    l,r = map(int, input[2].replace(':','').split(','))
    w,h = map(int, input[3].split('x'))
    fabric[l:l+w,r:r+h] = fabric[l:l+w,r:r+h] + 1
pass

print (len(fabric[fabric > 1])) # Solution 1

for input in inputs:
    l,r = map(int, input[2].replace(':','').split(','))
    w,h = map(int, input[3].split('x'))
    if fabric[l:l+w,r:r+h].sum() ==  w * h:
        print (input[0]) # Solution 2
        break
    pass
pass


