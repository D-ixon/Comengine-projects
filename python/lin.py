import numpy as np
import matplotlib.pyplot as plt

# Your data generation
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)


plt.figure(figsize=(8, 6))
plt.scatter(X, y, color='blue', alpha=0.6, label='Data points')


plt.title('Visualization of Generated Linear Data')
plt.xlabel('X (Feature)')
plt.ylabel('y (Target)')
plt.legend()
plt.grid(True)


plt.show()