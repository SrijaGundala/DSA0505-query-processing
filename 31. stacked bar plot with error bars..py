#Parthibhan R
#192224275
import matplotlib.pyplot as plt
import numpy as np
groups = ['Group 1', 'Group 2', 'Group 3', 'Group 4', 'Group 5']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
std_dev_men = [4, 3, 4, 1, 5]
std_dev_women = [3, 5, 2, 3, 3]

x_values = np.arange(len(groups))

plt.bar(x_values, means_men, yerr=std_dev_men, label='Men', color='blue', alpha=0.7)
plt.bar(x_values, means_women, yerr=std_dev_women, bottom=means_men, label='Women', color='pink', alpha=0.7)

plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Stacked Bar Plot with Error Bars')
plt.xticks(x_values, groups)
plt.legend()
plt.show()
