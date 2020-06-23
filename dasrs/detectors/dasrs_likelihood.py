from dasrs.detectors.base import DasrsAnomalyDetector
from nupic.algorithms import anomaly_likelihood
import math
SPATIAL_TOLERANCE = 0.05

class DasrsLikelihood(DasrsAnomalyDetector):

    def __init__(
        self,
        minValue,
        maxValue,
        probationaryPeriod=50,
        normValue=7,
        memoryWindow=2):
        super(DasrsLikelihood, self).__init__(
            minValue, maxValue, probationaryPeriod, normValue, memoryWindow
        )

        numentaLearningPeriod = int(math.floor(self.probationaryPeriod / 1.0))
        self.anomalyLikelihood = anomaly_likelihood.AnomalyLikelihood(
            learningPeriod=numentaLearningPeriod,
            estimationSamples=self.probationaryPeriod-numentaLearningPeriod,
            reestimationPeriod=100
        )

        self.minVal = None
        self.maxVal = None

    def computeFinalScore(self, currentScore, inputValue, inputTimestamp):
        anomalyScore = self.anomalyLikelihood.anomalyProbability(
            inputValue, currentScore, inputTimestamp)
        finalScore = self.anomalyLikelihood.computeLogLikelihood(anomalyScore)

        spatialAnomaly = False
        if self.minVal != self.maxVal:
            tolerance = (self.maxVal - self.minVal) * SPATIAL_TOLERANCE
            maxExpected = self.maxVal + tolerance
            minExpected = self.minVal - tolerance
            if inputValue > maxExpected or inputValue < minExpected:
                spatialAnomaly = True
        if self.maxVal is None or inputValue > self.maxVal:
            self.maxVal = inputValue
        if self.minVal is None or inputValue < self.minVal:
            self.minVal = inputValue

        if spatialAnomaly:
            finalScore = 1.0

        return finalScore
