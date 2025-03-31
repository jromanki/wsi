import numpy as np
from solver import Solver

class RandomSolver(Solver):
    """ A solver that draws n random points and returns the one with lowest goal function value"""
    def __init__(self, size: int = 20):
        self.size = size

    def get_parameters(self) -> Dict[str, Any]:
        return {'n': self.n}

    def solve(