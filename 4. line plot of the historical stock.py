import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
start_date = '2024-01-01'
end_date = '2024-02-21'
num_dates = 21
date_range = pd.date_range(start=start_date, end=end_date, periods=num_dates)
prices = [100, 110, 105, 115, 120, 118, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195]
stock_data = pd.DataFrame({'Date': date_range, 'Price': prices})
stock_data.plot(kind='line', x='Date', y='Price', figsize=(10, 6), color='blue')
plt.title('Historical Stock Prices of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Price')

plt.grid(True)
plt.tight_layout()
plt.show()
