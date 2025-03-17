import matplotlib.pyplot as plt
import numpy as np
import functions
from gradient_solver import GradientDescentSolver

x = np.linspace(-5, 5, 100)
plt.plot(x, functions.f1([x]))


x1 = np.array([-3]) # test point
plt.scatter(x1, functions.f1(x1), color='green')

solver = GradientDescentSolver()
x_min, i = solver.solve(x1, functions.grad_f1)

print(x_min, i)
plt.scatter(x_min, functions.f1(x_min), color='red')

plt.show()