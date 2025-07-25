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

    def __initialize_population(self, init_solver):
        self.size = init_solver.get_parameters()['size']
        return np.array([init_solver.solve() for _ in range(self.mu)])

    def __evaluate_population(self, p, gain_func):
        return np.array([gain_func(p[i], self.size) for i in range(self.mu)])

    def __find_best(self, p, q):
        best_index = np.argmax(q)
        return p[best_index], q[best_index]

    def __roulette_select(self, p, q, offset=False):
        if offset:
            temp_q = q - min(q) # offset
        else:
            temp_q = q
        if not np.all(temp_q == 0):
            quality_sum = np.sum(temp_q)
        else:
            # handling edge case when all q's have the same value
            temp_q = np.ones(len(q)) # ensuring all p(q) sums to 1
            quality_sum = len(q)
        probabilities = np.array(temp_q) / quality_sum
        selected_indexes = np.random.choice(len(p), size=self.mu, p=probabilities)
        return p[selected_indexes]

    def __crossover(self, s):
        offsprings = []
        temp_pair = []
        for individual in s:
            if np.random.rand() < self.pc:
                temp_pair.append(individual.copy())
                if len(temp_pair) == 2:
                    cut = np.random.randint(len(individual))  # Random crossover point
                    temp1 = temp_pair[0].copy()
                    temp2 = temp_pair[1].copy()
                    temp_pair[0][:cut] = temp2[:cut]
                    temp_pair[1][:cut] = temp1[:cut]
                    offsprings.append(temp_pair[0])
                    offsprings.append(temp_pair[1])
                    temp_pair = []
            else:
                offsprings.append(individual)  # If no crossover, keep individual unchanged
        
        if len(temp_pair) == 1:
            offsprings.append(temp_pair[0]) # Fixed bug that shortened list if the last individual was unpaired
        return np.array(offsprings)

    def __mutate(self, c):
        for individual in c:
            for i in range(len(individual)):
                if np.random.rand() < self.pm:
                    individual[i] = (individual[i] + 1) % 2 # negate a bit
        return c

    def solve(self, init_solver, gain_func: Callable[[np.ndarray], int], offset: bool) -> np.ndarray:
        all_q = []
        t = 0
        p = self.__initialize_population(init_solver)
        q = self.__evaluate_population(p, gain_func)
        x_best, q_best = self.__find_best(p, q)
        while t < self.t_max:
            s = self.__roulette_select(p, q, offset)
            m = self.__mutate(self.__crossover(s))
            q = self.__evaluate_population(m, gain_func)
            x_offspring_best, q_offspring_best = self.__find_best(m, q)
            if (q_offspring_best > q_best):
                x_best = x_offspring_best
                q_best = q_offspring_best
            p = m
            all_q.append(q_best)
            t += 1
        return x_best, q_best, all_q


