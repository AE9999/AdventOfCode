import sys

input = list(map(lambda x: int(x), sys.stdin.readline().rstrip().split(' ')))

class MyTree:
    def __init__(self, children, metaData):
        self.children = children
        self.metaData = metaData
    pass
pass

def parseTree(index):
    global input
    children, nextIndex = [], index + 2
    for x in range(input[index]):
        child, nextIndex = parseTree(nextIndex)
        children.append(child)
    pass
    metaData = input[nextIndex:nextIndex + input[index+1]]
    return (MyTree(children, metaData), nextIndex + input[index+1])
pass

def countMetaData(node):
    return sum(node.metaData) + sum(map(countMetaData, node.children))
pass

def calculateMetaDataValue(node, metaData):
    if metaData == 0 or metaData > len(node.children): return 0
    return calculateValue(node.children[metaData-1])
pass

def calculateValue(node):
    if len(node.children) == 0: return sum(node.metaData)
    return sum([calculateMetaDataValue(node, node.metaData[x]) for x in range(len(node.metaData))])
pass

tree = parseTree(0)[0]

print("Metadata sum %d .." % countMetaData(tree))
print("Value tree %d .." % calculateValue(tree))
