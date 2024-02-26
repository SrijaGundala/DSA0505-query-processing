#Parthibhan R
#192224275
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO


csv_data = """Date,Open,High,Low,Close
10-03-16,774.25,776.065002,769.5,772.559998
10-04-16,776.030029,778.710022,772.890015,776.429993
10-05-16,779.309998,782.070007,775.650024,776.469971
10-06-16,779,780.47998,775.539978,776.859985
10-07-16,779.659973,779.659973,770.75,775.080017"""


df = pd.read_csv(StringIO(csv_data), parse_dates=['Date'])

plt.plot(df['Date'], df['Open'], color='blue', label='Open', marker='o')
plt.plot(df['Date'], df['High'], color='green', label='High', marker='o')
plt.plot(df['Date'], df['Low'], color='red', label='Low', marker='o')
plt.plot(df['Date'], df['Close'], color='purple', label='Close', marker='o')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Alphabet Inc. Financial Data (Oct 3, 2016 - Oct 7, 2016)')
plt.legend()

plt.show()





'''

#This Is import the file 

import pandas as pd
import matplotlib.pyplot as plt

# Read financial data from the CSV file into a DataFrame
df = pd.read_csv('fdata.csv', parse_dates=['Date'])

# Plotting the line chart
plt.plot(df['Date'], df['Close'])

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Alphabet Inc. Financial Data (Oct 3, 2016 - Oct 7, 2016)')

# Display the plot
plt.show()'''





















