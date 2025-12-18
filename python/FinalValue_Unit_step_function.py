import numpy as np
import matplotlib.pyplot as plt


a = 2.0          
b = 4.0          
tau = 1 / a      


t = np.linspace(0, 5, 500)

u = np.ones_like(t)


y = (b / a) * (1 - np.exp(-a * t))


plt.figure()
plt.plot(t, u, label="Input u(t) = 1")
plt.plot(t, y, label="Output y(t)")
plt.axvline(tau, linestyle="--", label="Time constant τ")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.title("First-Order System Step Response")
plt.legend()
plt.grid(True)
plt.show()
