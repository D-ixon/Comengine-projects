import numpy as np
import matplotlib.pyplot as plt

T = 2 * np.pi
t = np.linspace(-T, T, 1000)
N = 5
f = 1 / T

square_wave_approx = np.zeros_like(t)

plt.figure(figsize=(10, 6))

colors = plt.cm.get_cmap('tab10', N)

for i, k in enumerate(range(1, 2 * N, 2)):  
    bn = 4 / (np.pi * k)
    harmonic = bn * np.sin(k * 2 * np.pi * f * t)
    
    plt.plot(t, harmonic, label=f'Harmonic {i+1}', linewidth=1.5)
    
    square_wave_approx += harmonic

plt.title('Fourier Series Harmonics for a Square Wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()