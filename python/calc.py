import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m = 1.0
k = 2.0
b = 0.1
dt = 0.02
t = np.arange(0, 10, dt)
x = 0.0
v = 0.0

positions = []
velocities = []

def force(t):
    return 2.0


for ti in t:
    a = (force(ti) - b*v - k*x) / m
    v += a * dt
    x += v * dt
    positions.append(x)
    velocities.append(v)

fig, ax = plt.subplots()
ax.set_xlim(-2, 2)
ax.set_ylim(-1, 1)
ax.set_title("mass spring damping")
ax.set_yticks([])

spring_line, = ax.plot([], [], lw=2, color='blue')
mass, = ax.plot([], [], 'ro', markersize=15)
trail, = ax.plot([], [], 'orange', lw=2, alpha=0.5)


vel_quiver = ax.quiver(0, 0, 0, 0, color='green', scale=1, scale_units='xy')

def zigzag(start, end, n=20, amplitude=0.1):
    xs = np.linspace(start, end, n)
    ys = amplitude * np.sin(np.linspace(0, 2*np.pi, n))
    return xs, ys


def update(frame):
    x_pos = positions[frame]
    v_now = velocities[frame]


    xs, ys = zigzag(0, x_pos)
    spring_line.set_data(xs, ys)


    mass.set_data([x_pos], [0])

    start_trail = max(0, frame-50)
    trail.set_data(positions[start_trail:frame+1], [0]*len(positions[start_trail:frame+1]))

    vel_quiver.set_offsets([[x_pos, 0]])
    vel_quiver.set_UVC([0.2*v_now], [0])  

    return spring_line, mass, trail, vel_quiver


ani = FuncAnimation(
    fig,
    update,
    frames=len(t),
    interval=dt*1000,
    blit=True
)

plt.show()
