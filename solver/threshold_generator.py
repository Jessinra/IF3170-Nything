class ThresholdGenerator:

    def __init__(self):
        pass
    
    def calculate_threshold(self, **kwargs):
        pass

class ConstantGenerator(ThresholdGenerator):

    def __init__(self, threshold):
        self.threshold = threshold

    def calculate_threshold(self):
        return self.threshold

from math import exp
class BoltzmannGenerator(ThresholdGenerator):

    def __init__(self, initial_temperature, ratio):
        
        self.temperature = initial_temperature
        self.ratio = ratio

    def calculate_threshold(self, value_differences):
        
        threshold = exp(-value_differences / self.temperature)
        self.temperature /= self.ratio

        return threshold 