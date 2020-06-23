from dasrs.detectors.base import DasrsAnomalyDetector

class DasrsRest(DasrsAnomalyDetector):

    def __init__(
        self,
        minValue,
        maxValue,
        probationaryPeriod=50,
        normValue=7,
        memoryWindow=2):
        super(DasrsRest, self).__init__(
            minValue, maxValue, probationaryPeriod, normValue, memoryWindow
        )

        self.restPeriod = probationaryPeriod / 5.0
        self.restWeakenFactor = 0
        self.baseThreshold = 1.0

    def computeFinalScore(self, currentScore, inputValue, inputTimestamp):
        finalScore = currentScore
        if self.restWeakenFactor > 0:
            finalScore = round(currentScore / self.restWeakenFactor, 2)
            self.restWeakenFactor -= 1
        elif currentScore >= self.baseThreshold:
            self.restWeakenFactor = self.restPeriod
        return finalScore