from math import exp


class ThresholdGenerator:
    def __init__(self):
        pass
    
    def calculate_threshold(self, **kwargs):
        pass


class ConstantGenerator(ThresholdGenerator):
    def __init__(self, threshold):
        super().__init__()
        self.threshold = threshold

    def calculate_threshold(self):
        return self.threshold


class BoltzmannGenerator(ThresholdGenerator):
    def __init__(self, initial_temperature, ratio):
        super().__init__()
        self.temperature = initial_temperature
        self.ratio = ratio

    def calculate_threshold(self, value_differences):
        if self.temperature <= 0:
            return 0
        threshold = exp(-value_differences / self.temperature)
        self.temperature /= self.ratio

        return threshold 