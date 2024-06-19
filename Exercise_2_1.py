# Exercise 2_1
# A boatman is rowing on the boat, wanting to always stay perpendicular to the
# river bank and crossing with an average speed of 36 km / h. The river water 
# flows with a speed of 9 km / h. How fast should the boat be propelled? 
# In what direction? 

# Import matplotlib to plot problem vectors
import matplotlib.pyplot as plt
# Import numpy for vector calculations
import numpy as np

# set the cartesian plane whith the river bank parallel to x-axis. 
# Exercise data
v_river = np.array([9, 0])  # Water velocity parallel to x-axis (km/h)
v_boat = np.array([0, 36])  # Speed of 36 km/h perpendicular to river bank; so parallel to y-axis.

# Velocity of the boat is the sum of water velocity and propelled velocity. 
# So, Propelled velocity is (boat velocity - water velocity)
v_propelled = v_boat - v_river

# Speed of the propelled boat (magnitude of propelled velocity)
norm_v_propelled = np.linalg.norm(v_propelled)

def angle_between_vectors_ccw(v1, v2):
  """
  Calculates the angle between two vectors in counter-clockwise direction.

  Args:
      v1 (numpy.ndarray): The first vector.
      v2 (numpy.ndarray): The second vector.

  Returns:
      float: The angle between the two vectors in radians.

  This function calculates the angle between two vectors `v1` and `v2` using the dot product 
  and arccosine formulas. The angle is measured in counter-clockwise direction from `v1` to `v2`.
  """
  dot_product = np.dot(v1, v2)
  mag_product = np.linalg.norm(v1) * np.linalg.norm(v2)
  radians = np.arccos(dot_product / mag_product)
  return radians

# Calculate angle phi
phi = angle_between_vectors_ccw(v_river, v_propelled)

# Convert angle to degrees (optional)
phi_deg = np.degrees(phi)

# Print the results
print(f"Speed of the propelled boat: {norm_v_propelled:.2f} km/h")
print(f"Direction: {phi_deg:.2f} degrees counter-clockwise from the riverbank")

# Plot axes and labels
plt.figure(figsize=(6, 6))  # Adjust figure size in inches 
plt.xlim(-15, 45)  # Set x-axis limits
plt.ylim(-5, 45)  # Set y-axis limits
plt.xlabel("X-axis (km/h)")
plt.ylabel("Y-axis (km/h)")
plt.title("River, Boat, and Propelled Velocities")
plt.grid(True) # Turn on the grid lines

# Plot vectors as arrows
plt.arrow(0, 0, *v_river, head_width=0.2, head_length=0.3, label="River Velocity", color='blue')
plt.arrow(0, 0, *v_boat, head_width=0.2, head_length=0.3, label="Boat Velocity", color='green')
plt.arrow(0, 0, *v_propelled, head_width=0.2, head_length=0.3, label="Propelled Velocity", color='red')

# Plot angle phi
plt.text(v_propelled[0] / 2, v_propelled[1] / 2, f"{phi_deg:.0f} degrees", ha='center', va='center')  # Place angle text

# Display the plot
plt.legend()
plt.show()