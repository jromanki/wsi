import numpy as np
from solver import Solver
from typing import Callable, Dict, Any

class RandomSolver(Solver):
    """ A solver that draws n random points and returns the one with lowest goal function value"""
    def __init__(self, size: int = 20):
        self.size = size

    def get_parameters(self) -> Dict[str, Any]:
        return {'size': self.size}

    def solve(self, init_func: Callable[[np.ndarray], int] gain_func: Callable[[np.ndarray], int], 