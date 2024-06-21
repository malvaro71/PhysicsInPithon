# An airplane is moving with a speed of 600 km/h in the NE direction. 
# Find the projection of its velocity onto the east direction.

import math

# Imput data
airplane_speed = 600 # Km/h

# Calculate the proyection using the scalar product
speed_proy_E = airplane_speed * math.cos(math.pi / 4) # Angle from E to NE is PI/4 radians

# Print the result
print(f'The projection of airplane velocity onto the east direction is {speed_proy_E:.2f} Km/h')
