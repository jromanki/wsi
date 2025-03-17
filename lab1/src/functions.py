import numpy as np

def f1(x_args: np.ndarray) -> float:
    x = x_args[0]
    return 10*x**4 + 3*x**3 - 30*x**2 + 10*x

def f2(x_args: np.ndarray) -> float:
    x1, x2 = x_args[0], x_args[1]
    return (x1-2)**4 + (x2+3)**4 + 2 * (x1-2)**2 * (x2+3)**2

def grad_f1(x_args: np.ndarray) ->  np.ndarray:
    x = np.float64(x_args[0])
    return np.array([40*x**3 + 9*x**2 - 60*x + 10])

def grad_f2(x_args: np.ndarray) ->  np.ndarray:
    x1, x2 = x_args[0], x_args[1]
    g_1 = 4*(x1 - 2)**3 + 4*(x1 - 2)*((x2 + 3)**2)
    g_2 = 4*(x2 + 3)**3 + 4*(x2 + 3)*((x1 - 2)**2)
    return np.array([g_1, g_2])