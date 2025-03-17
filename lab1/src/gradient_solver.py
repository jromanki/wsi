from solver import Solver
import numpy as np
from typing import Callable, Dict, Any

class GradientDescentSolver(Solver):
    def __init__(self, beta: float = 0.001, eps: float = 0.00001, max_iter: int = 10000):
        self.beta = beta
        self.eps = eps
        self.max_iter = max_iter

    def get_parameters(self) -> Dict[str, Any]:
        return {'beta': self.beta,
                'eps': self.eps,
                'max_iter': self.max_iter}

    def solve(self, x_init: np.ndarray, grad_func: Callable[[np.ndarray], np.ndarray]):
        x = x_init
        for _ in range(100): # change to while !stop later
            d = grad_func(x)
            x = x - self.beta * d
        return x