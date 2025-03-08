import matplotlib.pyplot as plt
import numpy as np
import solver

def f1(xf):
    return 10*xf**4 + 3*xf**3 - 30*xf**2 + 10*xf

def f2(x,y):
    return (x-2)**4 + (y+3)**4 + 2 * (x-2)**2 * (y+3)**2

x = np.linspace(-2.2, 2, 100)
# plt.plot(xf, f1(xf))



x = np.linspace(-10, 15, 1000)
y = np.linspace(-15, 10, 1000)
xx, yy = np.meshgrid(x, y)
zz = f2(xx, yy)

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx, yy, zz, cmap='viridis')

# contour plot
# plt.contourf(xx, yy, zz)
# plt.colorbar(label='Function value')
# plt.title('f(x, y)')

plt.show()