def f1(args):
    x = args[0]
    return 10*x**4 + 3*x**3 - 30*x**2 + 10*x

def f2(args):
    x1, x2 = args[0], args[1]
    return (x1-2)**4 + (x2+3)**4 + 2 * (x1-2)**2 * (x2+3)**2

def g1(args):
    x = args[0]
    return [40*x**3 + 9*x**2 - 60*x + 10]

def g2(args):
    x1, x2 = args[0], args[1]
    g_1 = 4*(x1 - 2)**3 + 4*(x1 - 2)*(x2 + 3)*2
    g_2 = 4*(x2 + 3)**3 + 4*(x2 + 3)*(x1 + 2)*2
    return [g_1, g_2]


