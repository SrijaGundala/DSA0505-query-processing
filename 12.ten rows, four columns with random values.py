import pandas as pd
import numpy as np

# Create a DataFrame with ten rows and four columns with random values
data = np.random.rand(10, 4)
columns = ['Column1', 'Column2', 'Column3', 'Column4']
df = pd.DataFrame(data, columns=columns)

# Convert the DataFrame to strings with HTML-style formatting
formatted_df = df.applymap(lambda x: f'<span style="background-color:black; color:yellow;">{x:.4f}</span>')

# Display the HTML-formatted DataFrame using print
print(formatted_df.to_string(escape=False))
