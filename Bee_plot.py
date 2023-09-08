# To plot the path of the bee in 3D space based on the given dynamical system equations.
# We can use Python and the Matplotlib library. 
# Here's a Python program to do that

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters
a, b, c = 10, 28, 2.667

# Define the initial conditions
x0, y0, z0 = 0, 1, 1.05

# Define the time parameters
t_start, t_end, num_points = 0, 30, 10000
t = np.linspace(t_start, t_end, num_points)
dt = (t_end - t_start) / num_points

# Initialize arrays to store the positions over time
x_values, y_values, z_values = [x0], [y0], [z0]

# Implement the dynamical system equations using Euler's method
for i in range(1, num_points):
    dot_x = a * (y_values[-1] - b)
    dot_y = b * x_values[-1] - y_values[-1] - x_values[-1] * z_values[-1]
    dot_z = x_values[-1] * y_values[-1] - c * z_values[-1]

    x_new = x_values[-1] + dot_x * dt
    y_new = y_values[-1] + dot_y * dt
    z_new = z_values[-1] + dot_z * dt

    x_values.append(x_new)
    y_values.append(y_new)
    z_values.append(z_new)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the path taken by the bee
ax.plot(x_values, y_values, z_values, label='Bee Path')

# Set labels for the axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Show the plot
plt.legend()
plt.show()




# This program will calculate the positions of the bee over time based on the given dynamical system equations and then plot the path taken by the bee in 3D space using Matplotlib.
