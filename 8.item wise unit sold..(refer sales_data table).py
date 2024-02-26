#Parthibhan R
#192224275

import pandas as pd

data = {
    'Item': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03'],
    'Unit Sold': [10, 15, 12, 13, 11, 16]
}

sales_data = pd.DataFrame(data)
sales_data['Date'] = pd.to_datetime(sales_data['Date'])

pivot_table = pd.pivot_table(sales_data, values='Unit Sold', index='Item', aggfunc='sum')
print("Item-wise Unit Sold Pivot Table:")
print(pivot_table)
