import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('service-export.csv')

ukraine_row = df[df['Country Name'] == 'Ukraine']
ukraine_data = ukraine_row.iloc[0, 4:].values.astype(float)  

uk_row = df[df['Country Name'] == 'United Kingdom']
uk_data = uk_row.iloc[0, 4:].values.astype(float)

years = [year.split(' ')[0] for year in df.columns[4:]]

plt.plot(years, ukraine_data, 'k', label="Ukraine")
plt.plot(years, uk_data, 'b', label="United Kingdom")

plt.xlabel('Years')
plt.ylabel('Values')
plt.title('Service exports (USD)')
plt.legend()
plt.show()
