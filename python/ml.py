import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, ifft2, fftshift, ifftshift
from scipy.ndimage import gaussian_filter

# 1) Load and Prep
from skimage import data, color
I = data.camera() # Cameraman is built-in to skimage

# 2) FFT and Spectrum
F = fft2(I)
Fs = fftshift(F)
mag = np.log(1 + np.abs(Fs))

plt.imshow(mag, cmap='gray')
plt.title('Magnitude Spectrum')
plt.show()

# 3) Frequency Filtering
M, N = I.shape
u = np.arange(-N//2, N//2)
v = np.arange(-M//2, M//2)
U, V = np.meshgrid(u, v)
D = np.sqrt(U**2 + V**2)

D0 = 30
Hlp = (D <= D0).astype(float) # Ideal Low-Pass
I_lp = np.real(ifft2(ifftshift(Fs * Hlp)))

# 4) Convolution (FFT-based)
# Instead of manual kernel padding, SciPy handles this natively
sigma = 2.0
I_blur_fft = gaussian_filter(I, sigma=sigma) 

# If you need to perform the multiplication manually:
# Kf = fft2(kernel, s=I.shape)
# I_blur_fft = np.real(ifft2(fft2(I) * Kf))