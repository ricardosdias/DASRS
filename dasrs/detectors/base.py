class DasrsAnomalyDetector(object):

    def __init__(
        self,
        minValue,
        maxValue,
        normValue,
        memoryWindow):

        self.minValue = minValue
        self.maxValue = maxValue
        self.normValue = normValue
        self.memoryWindow = memoryWindow
        self.fullValueRange = self.maxValue - self.minValue
        if self.fullValueRange == 0.0:
            self.fullValueRange = self.normValue
        self.valueStep = self.fullValueRange / self.normValue
        self.normInputWindow = []
        self.windows = {}

    def computeScoreFromOccurrences(self, occurrences):
        score = round(1.0 / occurrences, 2)
        return score

    def computeFinalScore(self, currentScore):
        return currentScore

    def getAnomalyScore(self, inputValue):
        normInpVal = int((inputValue - self.minValue) / self.valueStep)
        self.normInputWindow.append(normInpVal)

        if len(self.normInputWindow) < self.memoryWindow:
            return 0.0

        window = tuple(self.normInputWindow)
        windowHash = window.__hash__()
        occurrences = self.windows.setdefault(windowHash, 0) + 1
        self.windows[windowHash] += 1

        currentAnomalyScore = self.computeScoreFromOccurrences(occurrences)
        returnedAnomalyScore = self.computeFinalScore(currentAnomalyScore)

        self.normInputWindow.pop(0)

        return returnedAnomalyScore