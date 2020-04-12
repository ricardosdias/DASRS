from dasrs.detectors.base import DasrsAnomalyDetector

class DasrsRest(DasrsAnomalyDetector):

    def __init__(
        self,
        minValue,
        maxValue,
        restPeriod=10,
        normValue=7,
        memoryWindow=2):
        super(DasrsRest, self).__init__(
            minValue, maxValue, normValue, memoryWindow
        )

        self.restPeriod = restPeriod
        self.restWeakenFactor = 0
        self.baseThreshold = 1.0

    def computeFinalScore(self, currentScore):
        finalScore = currentScore
        if self.restWeakenFactor > 0:
            finalScore = round(currentScore / self.restWeakenFactor, 2)
            self.restWeakenFactor -= 1
        elif currentScore >= self.baseThreshold:
            self.restWeakenFactor = self.restPeriod
        return finalScore