#Parthibhan R
#192224275

import pandas as pd
data = {'ID': [1, 2, 3, 4],
        'Name': ['John', 'Alice', 'Bob', 'Eve']}
df = pd.DataFrame(data)

specified_column = 'Name'

df[specified_column] = df[specified_column].str.swapcase()

print("DataFrame after swapping cases:")
print(df)
