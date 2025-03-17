import matplotlib.pyplot as plt
import numpy as np
import functions

x = np.linspace(-2.2, 2, 100)
plt.plot(x, functions.f1([x]))

x = np.linspace(-10, 15, 1000)
y = np.linspace(-15, 10, 1000)
xx, yy = np.meshgrid(x, y)
zz = functions.f2([xx, yy])

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(xx, yy, zz, cmap='viridis')

# contour plot
# plt.contourf(xx, yy, zz)
# plt.colorbar(label='Function value')
# plt.title('f(x, y)')

plt.show()