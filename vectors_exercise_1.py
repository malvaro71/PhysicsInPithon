# Exercise 2_1
# A boatman is rowing on the boat, wanting to always stay perpendicular to the
# river bank and crossing with an average speed of 36 km / h. The river water
# flows with a speed of 9 km / h. How fast should the boat be propelled?
# In what direction?

# Import matplotlib to plot problem vectors
import matplotlib.pyplot as plt

# Import patches from matplotlib
from matplotlib import patches

# Import numpy for vector calculations
import numpy as np

# set the cartesian plane whith the river bank parallel to x-axis.
# Exercise data
v_r = np.array([9, 0])  # Water velocity parallel to x-axis (km/h).
v_b = np.array([0, 36])  # Speed of 36 km/h perpendicular to river bank.

# Velocity of the boat is the sum of water velocity and propelled velocity.
# So, Propelled velocity is (boat velocity - water velocity)
v_p = v_b - v_r

# Speed of the propelled boat (magnitude of propelled velocity)
norm_v_propelled = np.linalg.norm(v_p)

# Calculate angle phi, in degrees, between x-axis and v_propelled
phi = np.arctan2(v_p[1], v_p[0])
# Ref: https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html
phi_degrees = np.degrees(phi)

# Print the results
print(f"Speed of the propelled boat: {norm_v_propelled:.2f} km/h")
print(f"Direction: {phi_degrees:.2f} degrees"
      "counter-clockwise from the riverbank")

# Create a figure and axes object
fig, ax = plt.subplots(figsize=(6, 6))  # Adjust figure size in inches

# Set x and y axis limits
ax.set_xlim(-15, 45)
ax.set_ylim(-5, 45)

# Set axis labels
ax.set_xlabel("X-axis (km/h)")
ax.set_ylabel("Y-axis (km/h)")
ax.set_title("River, Boat, and Propelled Velocities")

# Turn on the grid lines
ax.grid(True)

# Plot vectors as arrows using object-oriented approach
# Plot the vectors
ax.arrow(0, 0, v_r[0], v_r[1], head_width=1, head_length=1, fc='blue', ec='blue',label='River Velocity')
ax.arrow(0, 0, v_b[0], v_b[1], head_width=1, head_length=1, fc='red', ec='red', label='Boat Velocity')
ax.arrow(0, 0, v_p[0], v_p[1], head_width=1, head_length=1, fc='green', ec='green', label='Propelled Velocity')

# Plot the arc using patches.Arc with object-oriented approach
arc = patches.Arc((0, 0), width=4, height=4, angle=0, 
                   theta1=0, theta2=phi_degrees, linewidth=2, color='red')
ax.add_patch(arc)  # Add arc to the axes

# Place angle text on the plot
ax.text(2*np.cos(phi/2), 2*np.sin(phi/2), f"{phi_degrees:.0f} degrees", ha='left', va='bottom')
ax.text(norm_v_propelled/2*np.cos(phi), norm_v_propelled/2*np.sin(phi), f"{norm_v_propelled:.0f} Km/h ", ha='right', va='bottom')

# Add legend
ax.legend()

# Display the plot
plt.show()
plt.legend()
