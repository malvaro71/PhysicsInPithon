# An airplane is moving with a speed of 600 km/h in the NE direction.
# Find the projection of its velocity onto the east direction.

import math

# Imput data
airplane_speed = 600  # Km/h

# Calculate the proyection using the scalar product
# Angle from E to NE is PI/4 radians
speed_proy_E = airplane_speed * math.cos(math.pi / 4)

# Print the result
print('The projection of airplane velocity onto the east direction is'
      f' {speed_proy_E:.2f} Km/h')
