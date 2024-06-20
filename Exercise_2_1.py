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

# Calculate angle phi, in degrees, between x-axis and v_propelled
# Reference: https://numpy.org/doc/stable/reference/generated/numpy.arctan2.html
phi = np.degrees(np.arctan2(v_propelled[1], v_propelled[0]))

# Print the results
print(f"Speed of the propelled boat: {norm_v_propelled:.2f} km/h")
print(f"Direction: {phi:.2f} degrees counter-clockwise from the riverbank")

# Plot axes and labels
plt.figure(figsize=(6, 6))  # Adjust figure size in inches 
plt.xlim(-15, 45)  # Set x-axis limits
plt.ylim(-5, 45)  # Set y-axis limits
plt.xlabel("X-axis (km/h)")
plt.ylabel("Y-axis (km/h)")
plt.title("River, Boat, and Propelled Velocities")
plt.grid(True) # Turn on the grid lines

# Plot vectors as arrows
plt.arrow(0, 0, *v_river, head_width=0.2, head_length=0.3, label="River Velocity", color='blue', 
          length_includes_head=True)
plt.arrow(0, 0, *v_boat, head_width=0.2, head_length=0.3, label="Boat Velocity", color='green', 
          length_includes_head=True)
plt.arrow(0, 0, *v_propelled, head_width=0.2, head_length=0.3, label="Propelled Velocity", color='red', 
          length_includes_head=True)

# Place angle text
plt.text(v_propelled[0] / 2, v_propelled[1] / 2, f"{phi:.0f} degrees", ha='center', va='center')

# Create and draw the angle arc
fig, ax = plt.subplots()
arc = matplotlib.patches.Arc(xy=(0, 0), 
                             width=2 * radius,  # Diameter of the arc
                             height=2 * radius,
                             angle=0,  # Starting angle from 0 degrees (optional)
                             theta1=0,  # Starting angle of the arc is at x-axis
                             theta2=phi,   # Ending angle of the arc is phi; calculated earlier
                             linewidth=2)
ax.add_patch(arc)
ax.set_aspect('equal')  # Ensure equal aspect ratio for circle

# Display the plot
plt.legend()
plt.show()
