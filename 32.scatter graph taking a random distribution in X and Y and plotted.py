#Parthibhan R
#192224275
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42) 
num_points = 50
x_values = np.random.rand(num_points)
y_values = np.random.rand(num_points)

plt.scatter(x_values, y_values, color='blue', marker='o', s=50, alpha=0.8)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Random Scatter Plot')

plt.show()
