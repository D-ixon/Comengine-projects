import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# =========================
# USER INPUT
# =========================
print("Enter Vector 1")
v1 = np.array([
    float(input("v1 x: ")),
    float(input("v1 y: ")),
    float(input("v1 z: "))
])

print("\nEnter Vector 2")
v2 = np.array([
    float(input("v2 x: ")),
    float(input("v2 y: ")),
    float(input("v2 z: "))
])

print("\nEnter Vector 3")
v3 = np.array([
    float(input("v3 x: ")),
    float(input("v3 y: ")),
    float(input("v3 z: "))
])

M = np.column_stack((v1, v2, v3))
rank = np.linalg.matrix_rank(M)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot vectors (color coded)
ax.quiver(0,0,0, *v1, color='red', linewidth=2, label='v1')
ax.quiver(0,0,0, *v2, color='blue', linewidth=2, label='v2')
ax.quiver(0,0,0, *v3, color='green', linewidth=2, label='v3')

t = np.linspace(-5,5,20)

if rank == 1:
    # Span is a line
    span_line = np.outer(t, v1)
    ax.plot(span_line[:,0], span_line[:,1], span_line[:,2],
            linestyle='dashed', color='black', label='Span (Line)')

elif rank == 2:
    # Span is a plane
    s = np.linspace(-3,3,10)
    t = np.linspace(-3,3,10)
    S, T = np.meshgrid(s,t)

    plane = (np.outer(S.flatten(), v1) +
             np.outer(T.flatten(), v2))

    X = plane[:,0].reshape(S.shape)
    Y = plane[:,1].reshape(S.shape)
    Z = plane[:,2].reshape(S.shape)

    ax.plot_surface(X,Y,Z, alpha=0.3, color='purple')

elif rank == 3:
    # Span is all R^3
    # Show a translucent cube as indicator
    r = [-3,3]
    for s in r:
        for t in r:
            ax.plot([s,s], [t,t], r, color='gray', alpha=0.3)
            ax.plot([s,s], r, [t,t], color='gray', alpha=0.3)
            ax.plot(r, [s,s], [t,t], color='gray', alpha=0.3)

    ax.text(0,0,3,"Span = R^3", color='black')

# =========================
# Labels
# =========================
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title(f'Span Dimension = {rank}')
ax.legend()

plt.show()