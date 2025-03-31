import numpy as np
from solver import Solver
from typing import Callable, Dict, Any

class GeneticSolver(Solver):
    """ A solver that uses genetic algorythm to solve the problem with variable
    hyperparameters """
    def __init__(self, t_max: int, mu: int, pc: float, pm: float):
        self.t_max = t_max
        self.mu = mu
        self.pc = pc
        self.pm = pm

    def get_parameters(self) -> Dict[str, Any]:
        return {'t_max': self.t_max,
                'mu': self.mu,
                'pc': self.pc,
                'pm': self.pm}

    def initialize_population(self, init_func, gain_func):
        p, o = [], []
        for _ in range(self.mu):
            x = init_func()
            p.append(x)
            o.append(gain_func(x))
        return p, o

    def find_best(self, p, o):
        o_max = np.max(o)
        return p[o.index(o_max)], o_max

    def solve(self, init_func: Callable[[int], np.ndarray],
            gain_func: Callable[[np.ndarray], int],) -> np.ndarray:
        t = 0
        p, o = self.initialize_population(init_func, gain_func)
        p_max, o_max = self.find_best(p, o)
        return p_max, o_max
