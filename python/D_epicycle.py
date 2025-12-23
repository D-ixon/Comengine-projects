import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------- Exact geometric F ----------
def letter_F(N=1200):
    x_left = -0.7
    h = 1.4
    top = 0.7
    mid = 0.1
    bar_len = 1.0
    mid_len = 0.7

    # vertical stem
    y = np.linspace(-h/2, h/2, N//3)
    stem = x_left + 1j * y

    # top bar
    x1 = np.linspace(x_left, x_left + bar_len, N//6)
    top_bar = x1 + 1j * top

    # middle bar
    x2 = np.linspace(x_left, x_left + mid_len, N//6)
    mid_bar = x2 + 1j * mid

    return np.concatenate([stem, top_bar, mid_bar])

z = letter_F()
N = len(z)

# ---------- Fourier (epicycles only) ----------
coeffs = np.fft.fft(z) / N
freqs = np.fft.fftfreq(N)

# ---------- Figure ----------
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect("equal")
ax.axis("off")
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

epicycles, = ax.plot([], [], 'k-', lw=1)
trace_line, = ax.plot([], [], 'r', lw=3)

NUM_VECTORS = 18
trace = []

# ---------- Animation ----------
def update(frame):
    t = frame / N

    pos = 0 + 0j
    xs, ys = [0], [0]

    for k in range(-NUM_VECTORS, NUM_VECTORS + 1):
        idx = k % N
        prev = pos
        pos += coeffs[idx] * np.exp(2j * np.pi * k * t)
        xs += [prev.real, pos.real]
        ys += [prev.imag, pos.imag]

    epicycles.set_data(xs, ys)

    trace.append(z[frame])
    trace_line.set_data(
        [p.real for p in trace],
        [p.imag for p in trace]
    )

    return epicycles, trace_line

ani = FuncAnimation(
    fig,
    update,
    frames=N,
    interval=20,
    blit=False
)

plt.show()
