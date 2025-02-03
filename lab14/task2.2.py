import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('service-export.csv')

ukraine_row = df[df['Country Name'] == 'Ukraine']
ukraine_data = ukraine_row.iloc[0, 4:].values.astype(float)  

uk_row = df[df['Country Name'] == 'United Kingdom']
uk_data = uk_row.iloc[0, 4:].values.astype(float)

years = [year.split(' ')[0] for year in df.columns[4:]]

ax = plt.gca()

country = input("Введіть країну (1 - Україна, 2 - Велика Британія): ")

if country == "1":
    ax.bar(years, ukraine_data, align='edge')
elif country == "2":
    ax.bar(years, uk_data, align='edge')

ax.set_xticks(years)
ax.set_xticklabels(years)

plt.title('Service exports (USD)')
plt.show()
