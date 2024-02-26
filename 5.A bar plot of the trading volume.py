#Parthibhan R
#192224275

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
start_date = '2024-01-01'
end_date = '2024-02-21'
num_dates = 21
date_range = pd.date_range(start=start_date, end=end_date, periods=num_dates)
volumes = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]
volume_data = pd.DataFrame({'Date': date_range, 'Volume': volumes})
plt.figure(figsize=(10, 6))
plt.bar(volume_data['Date'], volume_data['Volume'], color='green')
plt.title('Trading Volume of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()
