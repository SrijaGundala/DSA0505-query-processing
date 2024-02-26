#Parthibhan R
#192224275

import matplotlib.pyplot as plt
import numpy as np

x_values = np.linspace(0, 10, 100)
y_values_1 = np.sin(x_values)
y_values_2 = np.cos(x_values)

plt.plot(x_values, y_values_1, label='Line 1', color='blue', linewidth=3, linestyle='-', marker='D', markersize=8, markeredgecolor='blue', markerfacecolor='none')
plt.plot(x_values, y_values_2, label='Line 2', color='green', linewidth=5, linestyle='-', marker='D', markersize=8, markeredgecolor='green', markerfacecolor='none')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Lines with Diamond-like Appearance')
plt.legend()
plt.show()
