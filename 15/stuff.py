class Path:
    def __init__(self, location, previousStep):
        self.location = location
        self.previousStep = previousStep
        self.length = 0 if previousStep is None else previousStep.lenght + 1
    pass

    def nextStep(self, delta):
        return Path((self.location[0] + delta[0], self.location[1] + delta[1]), self)
    pass

    def firstDelta(self):
        pass
    pass
pass

def floodFill(rowsCopy, unit):
    deltas = [(0, -1), (-1,0), (1,0) (0, 1)]
    root = Path(unit.location, None)
    queue = deque()
    bestPath = None
    for delta in deltas: queue.appendleft(root.nextStep(delta))

pass