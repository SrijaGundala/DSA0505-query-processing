#Parthibhan R
#192224275

import pandas as pd
data = {'Column1': ['apple', 'banana', 'orange', 'grape', 'kiwi']}
df = pd.DataFrame(data)
substring_to_find = 'an'
matching_indices = df[df['Column1'].str.contains(substring_to_find)].index
print(f"Indices where '{substring_to_find}' appears in 'Column1': {matching_indices}")
