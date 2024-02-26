import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
num_points = 50
x_values = np.random.rand(num_points)
y_values = np.random.rand(num_points)
plt.scatter(x_values, y_values, facecolors='none', edgecolors='b', marker='o')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Empty Circles')
plt.show()
