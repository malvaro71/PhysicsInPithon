# Draw, one after the other, the vectors a=<2, 3>, b=<4, -2>, c=<3, -2>
# and d= <-9, 1>.
# Calculate the vector resulting from the sum of all of them and its magnitude.

# Import matplotlib to plot problem vectors
import matplotlib.pyplot as plt
# Import numpy for vector calculations
import numpy as np

# Exercise data (vector values)
v_a = np.array([2, 3])
v_b = np.array([4, -2])
v_c = np.array([3, -2])
v_d = np.array([-9, 1])

# Plot the sum of the vectors
# Plot axes and labels
plt.figure(figsize=(6, 4))  # Adjust figure size in inches
plt.xlim(-2, 10)  # Set x-axis limits
plt.ylim(-3, 5)  # Set y-axis limits
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sum of vectors a, b, c and d")
plt.grid(True)  # Turn on the grid lines

# Initialize a variable to store the sum
sum_vector = np.zeros_like(v_a)  # Same shape and data type as v_a

# Tuples of vectors and their names
vectors = (v_a, v_b, v_c, v_d)
vector_names = ('a', 'b', 'c', 'd')
vector_colors = ('red', 'blue', 'green', 'brown')

# Calculate the sum of all the vectors
for v, name, color in zip(vectors, vector_names, vector_colors):
    plt.arrow(*sum_vector, *v, head_width=0.2, head_length=0.3, label=name,
              color=color, length_includes_head=True)
    sum_vector += v

# Calculate the magnitude of the sum
norm_sum = np.linalg.norm(sum_vector)

# Print the results
print('The sum of vectors a, b, d and d is:', sum_vector)
print('The magnitude of this sum is:', norm_sum)

# Display the plot
plt.legend()
plt.show()
