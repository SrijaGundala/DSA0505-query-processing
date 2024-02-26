#Parthibhan R
#192224275

import pandas as pd
from io import StringIO

csv_data = """
Year,WHO Region,Country,Type,Display Value
2015,Americas,United States,Beer,200
2015,Europe,France,Wine,300
2016,Africa,Nigeria,Spirits,150
2016,Americas,Canada,Beer,180
2017,Western Pacific,Japan,Spirits,250
"""
df = pd.read_csv(StringIO(csv_data))

print(df)
