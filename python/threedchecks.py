import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

theta = np.linspace(0, 6*np.pi, 400)

plt.ion()
fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_zlim(0, 6*np.pi)

ax.set_xlabel("Cosine (Real) also X axis")
ax.set_ylabel("Sine (Imagimary) also Y axis")
ax.set_zlabel("θ (Time)also Z axis")
ax.set_title("Euler's Identity")

helix_line, = ax.plot([], [], [], 'b', linewidth=2)
moving_point, = ax.plot([0], [0], [0], 'ro')

xs, ys, zs = [], [], []

for t in theta:
    x = np.cos(t)
    y = np.sin(t)
    
    xs.append(x)
    ys.append(y)
    zs.append(t)

    helix_line.set_data(xs, ys)
    helix_line.set_3d_properties(zs)

    moving_point.set_data([x], [y])
    moving_point.set_3d_properties([t])

    ax.plot([0, x], [0, 0], [t, t], 'r--', alpha=0.2)  
    ax.plot([x, x], [0, y], [t, t], 'g--', alpha=0.2)  

    plt.pause(0.03)

plt.ioff()
plt.show()
