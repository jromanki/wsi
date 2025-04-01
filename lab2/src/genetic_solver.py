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

    def __initialize_population(self, init_func):
        return [init_func() for _ in range(self.mu)]

    def __evaluate_population(self, p, gain_func):
        return [gain_func(p[i]) for i in range(self.mu)]

    def __find_best(self, p, gain_func):
        q = []
        for i in range(self.mu):
            q.append(gain_func(p[i]))
        q_best = np.max(q)
        return p[q.index(q_best)], q_best

    def __roulette_select(self, p, q):
        selected = []
        quality_sum = np.sum(q)
        probabilities = np.array(q) / quality_sum
        for _ in range(self.mu):
            p_index = np.random.choice(len(p), p=probabilities)
            selected.append(p[p_index])
        return np.array(selected)

    def __crossover(self, s):
        offsprings = []
        temp_pair = []
        for individual in s:
            if np.random.rand() < self.pc:
                temp_pair.append(individual)
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
            offsprings.append(temp_pair[0]) # fixed bug that shortened list if the last individual was unpaired
        return np.array(offsprings)

    def __mutate(c):
        for individual in c:
            for gene in individual:
                if np.random.rand() < self.pm:
                    print(gene)


    def solve(self, init_func: Callable[[int], np.ndarray], gain_func: Callable[[np.ndarray], int],) -> np.ndarray:
        t = 0
        p = self.__initialize_population(init_func)
        q = self.__evaluate_population(p, gain_func)
        p_best, q_best = self.__find_best(p, gain_func)
        
        s = self.__roulette_select(p, q)
        c = self.__crossover(s)
        self.__mutate(c)

        t += 1
        return p_best, q_best


