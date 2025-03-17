import matplotlib.pyplot as plt
import numpy as np
import functions
from gradient_solver import GradientDescentSolver

x = np.linspace(-2.2, 2, 100)
plt.plot(x, functions.f1([x]))


x1 = np.array([1.9]) # test point
plt.scatter(x1, functions.f1(x1), color='green')

solver = GradientDescentSolver()
x_min = solver.solve(x1, functions.grad_f1)

print(x_min)
plt.scatter(x_min, functions.f1(x_min), color='red')

plt.show()