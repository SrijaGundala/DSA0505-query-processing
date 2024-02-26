#Parthibhan R
#192224275
import pandas as pd

data = {
    'Student_ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
    'School_Code': ['S001', 'S002', 'S001', 'S002', 'S003'],
    'Age': [25, 30, 27, 28, 26]
}

df = pd.DataFrame(data)
school_stats = df.groupby('School_Code')['Age'].agg(['mean', 'min', 'max'])

print("Statistics for each school:")
print(school_stats)
