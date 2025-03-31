import numpy as np
import matplotlib.pyplot as plt

# Kod ewaluacji osobnika
def shift_r(x):
    return np.concatenate((np.zeros_like(x[..., :, -1:]), x[..., :, :-1]), axis=-1)

def shift_l(x):
    return np.concatenate((x[..., :, 1:], np.zeros_like(x[..., :, :1])), axis=-1)

def shift_t(x):
    return np.concatenate((np.zeros_like(x[..., -1:, :]), x[..., :-1, :]), axis=-2)

def shift_b(x):
    return np.concatenate((x[..., 1:, :], np.zeros_like(x[..., :1, :])), axis=-2)

def evaluate(x, size=20):
    assert np.shape(x)[-1] == size * size
    grid = np.cast[np.int_](np.reshape(x, (-1, size, size)))
    points = np.minimum(
    shift_r(grid) + shift_l(grid) + shift_t(grid) + shift_b(grid),
    1 - grid
    )
    return points.reshape(np.shape(x)).sum(-1)

def heatmap(x, size=20):
    assert np.shape(x)[-1] == size * size
    grid = np.cast[np.int_](np.reshape(x, (-1, size, size)))
    heatmap = 1-(0.5*(shift_r(grid) + shift_l(grid) + shift_t(grid) + shift_b(grid)) + grid)[0]
    return heatmap

def visualize(x, size=20):
    colors = heatmap(x)
    plt.imshow(colors, cmap="viridis")
    plt.title(f"Gain value = {evaluate(x)}")
    plt.xticks(range(size))
    plt.yticks(range(size))
    plt.show()

x = np.zeros(400)
x[0] = 1
x[23] = 1
visualize(x)
