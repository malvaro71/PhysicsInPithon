# A rigid body rotates with an angular velocity w given by the vector
# w = [1, 1, 1] rad/s.
# Calculate the linear velocity v with which a point P of the body moves,
# whose position vector is r = [2, −2, 1] m, knowing that v = w × r (vector
# cross product).

# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# Input data
w = np.array([1, 1, 1])
r = np.array([2, -2, 1])

# Calculate v = w x r
# https://numpy.org/doc/stable/reference/generated/numpy.linalg.cross.html#numpy.linalg.cross
v = np.linalg.cross(w, r)

# Print the result
print(f'The lineal velocity vector of the point P is ({v[0]:.2f}, {v[1]:.2f},'
      f' {v[2]:.2f})')

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# set axis limits
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(-5, 5)

# Plot the origin
ax.scatter(0, 0, 0, c='r', marker='o', label='Origin')

# Create labels for each vector
vector_labels = ['Angular Velocity', 'Position Vector', 'Linear Velocity']

# Plot origin and vectors using quiver
X, Y, Z = [0, 0, r[0]], [0, 0, r[1]], [0, 0, r[2]]  # Starting points
u, v, w = w, r, v  # Directions (vector components)

# Customize colors
arrow_collection = ax.quiver(X, Y, Z, u, v, w, color=['b', 'g', 'r'])

# Add labels at arrow endpoints (adjust offsets as needed)
for i in range(3):
    ax.text(u[i] + 0.2, v[i] + 0.2, w[i] + 0.2, vector_labels[i], color=arrow_collection.get_colors()[i])

# Add labels to legend (use the 'label' keyword in quiver is not recommended for this approach)
ax.legend(handles=[arrow_collection], labels=vector_labels)  # Use arrow_collection for all arrows

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
plt.show()
