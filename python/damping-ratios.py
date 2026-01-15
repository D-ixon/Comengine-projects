import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

t = np.linspace(0, 10, 600)
wn = 2.0
zeta_vals = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
time_shift = 2.0

def step_response(t, wn, z):
    if z < 1:
        wd = wn * np.sqrt(1 - z**2)
        return 1 - np.exp(-z * wn * t) * (
            np.cos(wd * t) + (z / np.sqrt(1 - z**2)) * np.sin(wd * t)
        )
    else:
        return 1 - np.exp(-wn * t) * (1 + wn * t)

responses = [step_response(t, wn, z) for z in zeta_vals]

fig = plt.figure(figsize=(11, 7))
ax = fig.add_subplot(111, projection="3d")

ax.set_xlim(time_shift, 10 + time_shift)
ax.set_ylim(0, 1.0)
ax.set_zlim(0, 1.6)

ax.set_xlabel("Time")
ax.set_ylabel("Damping Ratio")
ax.set_zlabel("Response")

ax.view_init(elev=25, azim=40)

lines = []
for _ in zeta_vals:
    line, = ax.plot([], [], [], linewidth=2)
    lines.append(line)

def animate(frame):
    for i, z in enumerate(zeta_vals):
        lines[i].set_data(t[:frame] + time_shift, np.full(frame, z))
        lines[i].set_3d_properties(responses[i][:frame])
    return lines

ani = FuncAnimation(fig, animate, frames=len(t), interval=30)

plt.show()
