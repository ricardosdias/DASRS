class DasrsAnomalyDetector(object):

    def __init__(
        self,
        minValue,
        maxValue,
        probationaryPeriod,
        normValue,
        memoryWindow):

        self.minValue = minValue
        self.maxValue = maxValue
        self.probationaryPeriod = probationaryPeriod
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

    def computeFinalScore(self, currentScore, inputValue, inputTimestamp):
        return currentScore

    def getAnomalyScore(self, inputValue, inputTimestamp=None):

        normInpVal = int((inputValue - self.minValue) / self.valueStep)
        self.normInputWindow.append(normInpVal)

        if len(self.normInputWindow) < self.memoryWindow:
            return 0.0

        window = tuple(self.normInputWindow)
        windowHash = window.__hash__()
        occurrences = self.windows.setdefault(windowHash, 0) + 1
        self.windows[windowHash] += 1

        currentAnomalyScore = self.computeScoreFromOccurrences(occurrences)
        returnedAnomalyScore = self.computeFinalScore(
            currentAnomalyScore,
            inputValue,
            inputTimestamp)

        self.normInputWindow.pop(0)

        return returnedAnomalyScore