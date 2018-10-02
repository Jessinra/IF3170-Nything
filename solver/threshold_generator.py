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

    def calculate_threshold(self, score_difference, step):
        return self.threshold


class BoltzmannGenerator(ThresholdGenerator):
    def __init__(self, initial_temperature, ratio):
        super().__init__()
        self.initial_temperature = initial_temperature
        self.ratio = ratio

    def calculate_threshold(self, value_difference, step):
        current_temperature = self.initial_temperature / self.ratio ** step

        if current_temperature <= 0:
            return 0

        return exp(-value_difference / current_temperature)
