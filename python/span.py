import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def get_vector(name):
    x = float(input(f"Enter {name} x-component: "))
    y = float(input(f"Enter {name} y-component: "))
    z = float(input(f"Enter {name} z-component: "))
    return np.array([x, y, z])


v1 = get_vector("Vector 1")
v2 = get_vector("Vector 2")
v3 = get_vector("Vector 3")


a_vals = np.linspace(-1, 1, 10)  
b_vals = np.linspace(-1, 1, 10)
c_vals = np.linspace(-1, 1, 10)


points = []

for a in a_vals:
    for b in b_vals:
        for c in c_vals:
            vec = a*v1 + b*v2 + c*v3
            points.append(vec)

points = np.array(points)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.scatter(points[:,0], points[:,1], points[:,2], color='purple', alpha=0.5, s=20)
origin = np.array([0,0,0])
ax.quiver(*origin, *v1, color='red', linewidth=2, arrow_length_ratio=0.1, label='v1')
ax.quiver(*origin, *v2, color='green', linewidth=2, arrow_length_ratio=0.1, label='v2')
ax.quiver(*origin, *v3, color='blue', linewidth=2, arrow_length_ratio=0.1, label='v3')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')


ax.view_init(elev=20, azim=30)

ax.legend()
plt.show()