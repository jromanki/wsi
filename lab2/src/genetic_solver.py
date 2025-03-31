import numpy as np
from solver import Solver
from typing import Callable, Dict, Any

class GeneticSolver(Solver):
    """ A solver that uses genetic algorythm to solve the problem with variable
    hyperparameters """
    def __init__(self, size: int = 20):
        self.size = size

    def get_parameters(self) -> Dict[str, Any]:
        return {'size': self.size}

    def solve(self, init_func: Callable[[], np.ndarray], gain_func: Callable[[np.ndarray], int],
            t_max: int, mu: int, pc: float, pm: float) -> np.ndarray:
        t = 0
