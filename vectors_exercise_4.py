# An object moves in such a way that its velocity at a certain instant is 120 m/s and forms an
# angle of 30º with the horizontal. Find the horizontal and vertical components of the velocity.
# Express the velocity vector as a function of its components.

# Import numpy
import numpy as np

# Input data
magnitude = 120 # m/s
direction = 30 # degrees

# Calculate velocity components (cos and sin functions expect radians)
velocity_x = magnitude*np.cos(np.radians(direction))
velocity_y = magnitude*np.sin(np.radians(direction))

velocity = np.array([velocity_x, velocity_y])

# Print velocity components and velocity vector
print(f'The horizontal component of the object velocity is {velocity_x:.2f} m/s')
print(f'The vertical component of the object velocity is {velocity_y:.2f} m/s')
print(f'The object velocity vector is ({velocity[0]:.2f}, {velocity[1]:.2f}) m/s')
