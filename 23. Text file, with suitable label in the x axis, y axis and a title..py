#Parthibhan R
#192224275

import pandas as pd
import matplotlib.pyplot as plt

data = {'X': [1, 2, 3],
        'Y': [2, 4, 1]}

df = pd.DataFrame(data)

x_values = df['X'].tolist()
y_values = df['Y'].tolist()

plt.plot(x_values, y_values)

plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Line Plot with Labels from DataFrame')

plt.show()
