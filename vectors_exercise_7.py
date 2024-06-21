# A rigid body rotates with an angular velocity w given by the vector
# w = [1, 1, 1] rad/s.
# Calculate the linear velocity v with which a point P of the body moves,
# whose position vector is r = [2, −2, 1] m, knowing that v = w × r (vector
# cross product).

# Import numpy
import numpy as np

# Input data
w = np.array([1, 1, 1])
r = np.array([2, -2, 1])

# Calculate v = w x r
# https://numpy.org/doc/stable/reference/generated/numpy.linalg.cross.html#numpy.linalg.cross
v = np.linalg.cross(w, r)

# Print the result
print(f'The lineal velocity vector of the point P is ({v[0]:.2f}, {v[1]:.2f},'
      f' {v[2]:.2f})')
