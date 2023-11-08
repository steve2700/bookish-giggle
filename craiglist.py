import pandas as pd

# Get the data
data = pd.read_csv('craigslist_vehicles.csv')

# Count the occurrences of each brand, model, and trim
brand_counts = data['brand'].value_counts()
model_counts = data['model'].value_counts()
trim_counts = data['trim'].value_counts()

# Print the top 10 most popular brands, models, and trims
print('Top 10 most popular brands:')
print(brand_counts.head(10))

print('Top 10 most popular models:')
print(model_counts.head(10))

print('Top 10 most popular trims:')
print(trim_counts.head(10))
import matplotlib.pyplot as plt

# Get the data
data = pd.read_csv('craigslist_vehicles.csv')

# Plot the price vs mileage
plt.scatter(data['mileage'], data['price'])
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.title('Relationship between price and mileage')
plt.show()

