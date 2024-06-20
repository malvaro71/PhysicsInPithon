# Find the scalar product of the vectors (5, −3, 2), (−2, 1, 3) and the angle they form. 

# Import numpy
import numpy as np

# Input data
a = np.array([5, -3, 2])
b = np.array([-2, 1, 3])

# Calculate the scalar product of vectors a and b
scalar_product = np.dot(a, b)

# Calculate the angle in radians formed by a and b
angle = np.arccos(scalar_product/(np.linalg.norm(a)*np.linalg.norm(b)))

# Print the results
print(f'The scalar product of the vectors (5, −3, 2), (−2, 1, 3) is {scalar_product}')
print(f'the angle in radians formed by (5, −3, 2) and (−2, 1, 3) is {angle:.2f} radians')
