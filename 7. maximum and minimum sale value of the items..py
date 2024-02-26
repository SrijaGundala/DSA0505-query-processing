#Parthibhan R
#192224275

import pandas as pd

data = {
    'Item': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03'],
    'Sale': [100, 150, 120, 130, 110, 160]
}

sales_data = pd.DataFrame(data)

sales_data['Date'] = pd.to_datetime(sales_data['Date'])

pivot_table = pd.pivot_table(sales_data, values='Sale', index='Item', aggfunc=['max', 'min'])

pivot_table.columns = ['Max Sale', 'Min Sale']

print("Pivot Table:")
print(pivot_table)
overall_max_sale = sales_data['Sale'].max()
overall_min_sale = sales_data['Sale'].min()

print("\nOverall Maximum Sale Value:", overall_max_sale)
print("Overall Minimum Sale Value:", overall_min_sale)
