#Parthibhan R
#192224275
import matplotlib.pyplot as plt
import numpy as np
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
x_values_men = np.arange(len(groups))
x_values_women = x_values_men + 0.4  

plt.bar(x_values_men, means_men, width=0.4, label='Men', color='blue')
plt.bar(x_values_women, means_women, width=0.4, label='Women', color='pink')

plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(x_values_men + 0.2, groups)
plt.legend()

plt.show()
