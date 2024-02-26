#Parthibhan R
#192224275

import matplotlib.pyplot as plt
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))

axes[0, 0].add_patch(plt.Rectangle((0.1, 0.1), 0.8, 0.8, fill=None, edgecolor='blue'))
axes[0, 0].set_title('Square 1')

axes[0, 1].add_patch(plt.Rectangle((0.1, 0.1), 0.8, 0.8, fill=None, edgecolor='green'))
axes[0, 1].set_title('Square 2')

axes[1, 0].add_patch(plt.Rectangle((0.1, 0.1), 0.8, 0.8, fill=None, edgecolor='red'))
axes[1, 0].set_title('Square 3')

axes[1, 1].add_patch(plt.Rectangle((0.1, 0.1), 0.6, 0.9, fill=None, edgecolor='purple'))
axes[1, 1].set_title('Rectangle')

plt.tight_layout()

plt.show()
