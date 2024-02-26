#Parthibhan R
#192224275

import pandas as pd
import numpy as np

np.random.seed(42)  
data = np.random.randn(10, 4)

df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D'])

def format_numbers(val):
    return f'{val:.3f}' if val >= 0 else f'{val:.2f}'

formatted_df = df.applymap(format_numbers)

print(formatted_df)
