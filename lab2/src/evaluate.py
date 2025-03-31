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
    points = np.minimum(
    shift_r(grid) + shift_l(grid) + shift_t(grid) + shift_b(grid),
    1 - grid
    )
    heatmap = grid[0] + 0.5*points[0] # 0.5 added ONLY FOR VISUALIZATION
    # to differente between objects and points scored
    return points.reshape(np.shape(x)).sum(-1), heatmap

def visualize(x, size=20):
    gain, colors = heatmap(x, size)
    plt.imshow(colors, cmap="viridis")
    # plt.imshow(colors, cmap="plasma")
    plt.title(f"Solver's final score = {gain}")
    plt.suptitle("Yellow tiles - object (0 pts); Green tiles - object's \n neighbors (1 pts); Purple tiles - free (0 pts)", y=0, fontsize=10)
    plt.tight_layout()
    plt.xticks(range(size))
    plt.yticks(range(size))
    plt.show()