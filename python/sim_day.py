import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

m = 1.5       # mass
k = 20.0      # spring constant
c = 0.1       # damping coefficient (smaller = slower decay)
y_top = -4.0   # fixed top position of spring
A = 1.0       # initial displacement below top
g = 9.8       # gravity

dt = 0.01
t_total = 20
steps = int(t_total/dt)

# Arrays to store simulation
y = np.zeros(steps)  # position of mass
v = np.zeros(steps)  # velocity
time = np.linspace(0, t_total, steps)

# Initial conditions: mass displaced downward from top
y[0] = y_top + A
v[0] = 0

# Numerical integration (Euler)
for i in range(steps-1):
    # acceleration due to spring, damping, gravity
    a = (-k*(y[i]-y_top) - c*v[i] + m*g)/m
    v[i+1] = v[i] + a*dt
    y[i+1] = y[i] + v[i+1]*dt
    # mass cannot go above top
    if y[i+1] < y_top:
        y[i+1] = y_top
        v[i+1] = 0

# Plot setup
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5))

# Left: vertical spring
ax1.set_xlim(1, -1)
ax1.set_ylim(1, -5)
ax1.set_title("undamed Mass-Spring")
ax1.axis("off")

# Right: position vs time graph
ax2.set_xlim(0, t_total)
ax2.set_ylim(y_top-0.1, max(y)*1.1)
ax2.set_title("Position vs Time")
ax2.set_xlabel("Time [s]")
ax2.set_ylabel("y(t)")
line_pos, = ax2.plot([], [], c='red')
time_data, pos_data = [], []

# Draw spring with visible coils
n_coils = 15
coil_width = 0.3

def draw_spring(ypos):
    spring_y = np.linspace(y_top, ypos, n_coils*2)
    spring_x = np.zeros_like(spring_y)
    for i in range(1, len(spring_y)-1, 2):
        spring_x[i] = coil_width
        spring_x[i+1] = -coil_width
    return spring_x, spring_y

spring_x, spring_y = draw_spring(y[0])
spring_line, = ax1.plot(spring_x, spring_y, c='orange', lw=2)
mass_rect, = ax1.plot([0], [y[0]], 's', markersize=30, c='blue')


# Update function

def update(frame):
    ypos = y[frame]

    # Update spring
    spring_x_new, spring_y_new = draw_spring(ypos)
    spring_line.set_data(spring_x_new, spring_y_new)

    # Update mass
    mass_rect.set_data([0], [ypos])

    # Update graph
    time_data.append(time[frame])
    pos_data.append(ypos)
    line_pos.set_data(time_data, pos_data)

    return spring_line, mass_rect, line_pos


ani = FuncAnimation(fig, update, frames=steps, interval=dt*1000, blit=False)
plt.show()
