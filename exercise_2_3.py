# A sailboat is moving with a speed of 4 km/h in the NNE (north-northeast) direction. 
# What are the components of the speed of the ship in the North direction and in the East direction?

import math

# Data
sailboat_speed = 4 # Km/h

# If we place the x-axis in the easterly direction and the y-axis in the north direction, the NNE 
# (north-northeast) direction forms an angle of 67.5º (or 3PI/8 radians) with the east.Then, 
sailboat_speed_x = sailboat_speed * math.cos(3 * math.pi / 8) # x-component of the sailboat speed
sailboat_speed_y = sailboat_speed * math.sin(3 * math.pi / 8) # y-component of the sailboat speed

# Print results
print('The x-component of sailboat speed is:', sailboat_speed_x)
print('The y-component of sailboat speed is:', sailboat_speed_y)
