import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

# Creating a horizontal bar chart
plt.barh(languages, popularity, color='skyblue')
plt.xlabel('Popularity (%)')
plt.title('Popularity of Programming Languages')
plt.grid(axis='x')

# Display the chart
plt.show()
