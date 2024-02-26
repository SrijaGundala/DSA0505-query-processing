#Parthibhan R
#192224275
import pandas as pd
import matplotlib.pyplot as plt

start_date = '2024-01-01'
end_date = '2024-02-21'
num_dates = 21
date_range = pd.date_range(start=start_date, end=end_date, periods=num_dates)
prices = [100, 110, 105, 115, 120, 118, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195]
volumes = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]

stock_data = pd.DataFrame({'Date': date_range, 'Price': prices, 'Volume': volumes})

start_date = '2024-01-10'
end_date = '2024-02-10'
filtered_data = stock_data[(stock_data['Date'] >= start_date) & (stock_data['Date'] <= end_date)]

plt.figure(figsize=(10, 6))
plt.scatter(filtered_data['Price'], filtered_data['Volume'], color='blue')
plt.title('Trading Volume/Stock Prices of Alphabet Inc.')
plt.xlabel('Stock Price')
plt.ylabel('Volume')
plt.tight_layout()
plt.show()
