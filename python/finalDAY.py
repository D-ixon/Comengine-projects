import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

np.random.seed(1)

n = 30
x = np.random.uniform(-5, 5, (n, 2))
v = np.zeros((n, 2))

pbest = x.copy()
gbest = x[np.argmin(np.sum(x**2, axis=1))]

w = 0.7
c1 = 1.4
c2 = 1.4

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_title("Particle Swarm Optimization")

particles = ax.scatter(x[:, 0], x[:, 1], c="red")
best, = ax.plot(gbest[0], gbest[1], "bo")

def update(frame):
    global x, v, pbest, gbest

    r1, r2 = np.random.rand(), np.random.rand()

    v = w*v + c1*r1*(pbest - x) + c2*r2*(gbest - x)
    x += v

    values = np.sum(x**2, axis=1)
    better = values < np.sum(pbest**2, axis=1)
    pbest[better] = x[better]

    gbest = pbest[np.argmin(np.sum(pbest**2, axis=1))]

    particles.set_offsets(x)
    best.set_data(gbest[0], gbest[1])
    return particles, best

ani = FuncAnimation(fig, update, frames=200, interval=50, blit=False)
plt.show()
