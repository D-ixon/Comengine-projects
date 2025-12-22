import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots(figsize=(10, 4))
ax.set_xlim(0, 10)
ax.set_ylim(-3, 3)
ax.axis("off")
ax.set_title("Battery Simulation: Electrons & Ions")

ax.axvspan(0, 1, color='gray', alpha=0.4)   
ax.axvspan(9, 10, color='gray', alpha=0.4)  
ax.axhspan(-1, 1, color='lightblue', alpha=0.3)  

ax.text(0.2, 0, "Anode (-)", fontsize=12)
ax.text(8.2, 0, "Cathode (+)", fontsize=12)
ax.text(4.2, -2.3, "Electrolyte", fontsize=11)


N_e = 30     
N_p = 20     
N_n = 20     


ex = np.linspace(1.2, 8.8, N_e)
ey = np.ones(N_e) * 2


px = np.random.uniform(2, 8, N_p)
py = np.random.uniform(-0.8, 0.8, N_p)

nx = np.random.uniform(2, 8, N_n)
ny = np.random.uniform(-0.8, 0.8, N_n)

electrons = ax.scatter(ex, ey, c='blue', s=40, label="Electrons")
pos_ions  = ax.scatter(px, py, c='red',  s=60, label="Positive ions")
neg_ions  = ax.scatter(nx, ny, c='green',s=60, label="Negative ions")


def update(frame):
    global ex, px, nx


    ex += 0.08
    ex[ex > 8.8] = 1.2


    px -= 0.03
    px[px < 2] = 8

    nx += 0.03
    nx[nx > 8] = 2

    electrons.set_offsets(np.c_[ex, ey])
    pos_ions.set_offsets(np.c_[px, py])
    neg_ions.set_offsets(np.c_[nx, ny])

    return electrons, pos_ions, neg_ions

ani = FuncAnimation(fig, update, frames=600, interval=30, blit=False)
plt.show()
