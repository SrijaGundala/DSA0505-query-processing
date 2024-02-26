#Parthibhan R
#192224275
import matplotlib.pyplot as plt
import numpy as np
group1_heights = np.random.normal(170, 10, 30)
group1_weights = np.random.normal(65, 5, 30)

group2_heights = np.random.normal(160, 8, 30)
group2_weights = np.random.normal(55, 4, 30)

group3_heights = np.random.normal(175, 12, 30)
group3_weights = np.random.normal(75, 6, 30)

plt.scatter(group1_weights, group1_heights, color='Blue', label='Group 1', marker='*', s=50, alpha=0.8)
plt.scatter(group2_weights, group2_heights, color='Blue', label='Group 2', marker='*', s=50, alpha=0.8)
plt.scatter(group3_weights, group3_heights, color='Blue', label='Group 3', marker='*', s=50, alpha=0.8)

plt.xlabel('Weights (kg)')
plt.ylabel('Heights (cm)')
plt.title('Scatter Plot for Three Different Groups (Weights vs. Heights)')

plt.legend()
plt.show()
