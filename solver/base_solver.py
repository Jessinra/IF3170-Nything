from solver.state_evaluator import StateEvaluator

class BaseSolver:

    def __init__(self):

        self.evaluator = StateEvaluator()
        pass

    def next_step(self):
        pass
