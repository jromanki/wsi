from solver import Solver
import numpy as np
from typing import Callable, Dict, Any

class GradientDescentSolver(Solver):
    def __init__(self, beta: float = 0.0001, eps: float = 0.0000001, max_iter: int = 10000):
        self.beta = beta
        self.eps = eps
        self.max_iter = max_iter

    def get_parameters(self) -> Dict[str, Any]:
        return {'beta': self.beta,
                'eps': self.eps,
                'max_iter': self.max_iter}

    def solve(self, x_init: np.ndarray, grad_func: Callable[[np.ndarray], np.ndarray]):
        x = x_init
        i = 0
        while True:
            last_x = x
            d = grad_func(x)
            x = x - self.beta * d
            if np.all(abs(x - last_x) < self.eps): # difference in position of both coordinates
                # print('Found a solution (change smaller than eps)')
                return x, i
            if i > self.max_iter:
                # print('Iterations exceeded max iteration number')
                return np.array(x), i
            i += 1