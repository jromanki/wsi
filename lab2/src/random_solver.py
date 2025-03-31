import numpy as np
from solver import Solver
from typing import Dict, Any

class RandomSolver(Solver):
    """ A solver that returns random solution to the problem"""
    # note: this solver is used as initialization solver in GeneticSolver's solve method
    def __init__(self, size: int = 20):
        self.size = size

    def get_parameters(self) -> Dict[str, Any]:
        return {'size': self.size}

    def solve(self) -> np.ndarray:
        return np.random.randint(2, size=self.size*self.size)
