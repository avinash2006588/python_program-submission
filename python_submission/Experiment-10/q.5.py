# 5.	WAP to draw the 3D-plot.
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create data
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)

X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Draw surface plot
ax.plot_surface(X, Y, Z)

# Add labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Surface Plot")

plt.show()
