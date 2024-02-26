#Parthibhan R
#192224275
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
num_points = 50
x_values = np.random.rand(num_points)
y_values = np.random.rand(num_points)
ball_sizes = np.random.randint(10, 100, num_points)  
ball_colors = np.random.rand(num_points, 3) 

plt.scatter(x_values, y_values, c=ball_colors, s=ball_sizes, alpha=0.8)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Balls of Different Sizes and Colors')
plt.show()
