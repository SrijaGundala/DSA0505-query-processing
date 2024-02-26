#Parthibhan R
#192224275
import pandas as pd
from tabulate import tabulate

data = {
    'Student_ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'School_Code': ['S001', 'S002', 'S001', 'S002', 'S003'],
    'Grade': ['A', 'B', 'A', 'C', 'B']
}

df = pd.DataFrame(data)

grouped = df.groupby('School_Code')

all_groups = pd.concat([group for _, group in grouped])

print(tabulate(all_groups, headers='keys', tablefmt='pretty'))
