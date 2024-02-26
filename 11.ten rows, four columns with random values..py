#Parthibhan R
#192224275
import pandas as pd
import numpy as np
data = {
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [1.32921, np.nan, -1.07082, 0.564417, -1.6264, 0.961538, np.nan, 1.68658, -0.12982, -0.586538],
    'C': [np.nan, -0.31628, -1.43871, 0.295722, 0.219565, np.nan, 0.104011, -1.32596, 0.631523, np.nan],
    'D': [-0.99081, 1.88927, np.nan, np.nan, 1.05774, 0.562861, 1.2076, -2.08935, 1.39285, 0.519818],
    'E': [0.678805, 1.03753, 1.6278, -0.385684, 0.850229, 0.165562, -0.00204021, np.nan, -0.063328, np.nan]
}

df = pd.DataFrame(data)

formatted_df = df.applymap(lambda x: f'{x:.5f}' if not pd.isna(x) else 'nan')
print(formatted_df)
