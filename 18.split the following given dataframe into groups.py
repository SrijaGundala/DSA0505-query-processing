#Parthibhan R
#192224275

import pandas as pd
data = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Henry'],
    'School_Code': ['S001', 'S002', 'S001', 'S002', 'S003', 'S001', 'S002', 'S003'],
    'Class': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B']
}

df = pd.DataFrame(data)

grouped = df.groupby(['School_Code', 'Class'])

for (school, class_), group in grouped:
    print(f"\nSchool: {school}, Class: {class_}")
    print(group)
