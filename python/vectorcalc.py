import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def get_vector(name):
    x = float(input(f"Enter {name} x-component: "))
    y = float(input(f"Enter {name} y-component: "))
    z = float(input(f"Enter {name} z-component: "))
    return [x, y, z]


v1 = get_vector("Vector 1")
v2 = get_vector("Vector 2")
v3 = get_vector("Vector 3")


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

origin = [0, 0, 0]

ax.quiver(*origin, *v1, color='red', linewidth=2, arrow_length_ratio=0.1, label='Vector 1')
ax.quiver(*origin, *v2, color='green', linewidth=2, arrow_length_ratio=0.1, label='Vector 2')
ax.quiver(*origin, *v3, color='blue', linewidth=2, arrow_length_ratio=0.1, label='Vector 3')

ax.set_xlabel('X axis', color='red', fontsize=12)
ax.set_ylabel('Y axis', color='green', fontsize=12)
ax.set_zlabel('Z axis', color='blue', fontsize=12)

all_vectors = [v1, v2, v3]
max_val = max(max(abs(comp) for vec in all_vectors for comp in vec), 1)
ax.set_xlim([0, max_val])
ax.set_ylim([0, max_val])
ax.set_zlim([0, max_val])

ax.grid(True, linestyle='--', alpha=0.3)

ax.legend()

ax.view_init(elev=20, azim=30)

plt.show()