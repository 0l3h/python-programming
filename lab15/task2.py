import pandas as pd
import matplotlib.pyplot as plt

try:
    data = open("comptagevelo2013.csv", "r", newline="")

    df = pd.read_csv(data, parse_dates=['Date'])
    df['YearMonth'] = df['Date'].dt.to_period('M')

    monthly_sum = df.drop(columns=['Date']).groupby('YearMonth').sum().sum(axis=1)

    print(monthly_sum)

    plt.figure(figsize=(10, 6))
    monthly_sum.plot(kind='bar', color='skyblue')
    plt.title('Відвідування за кожен місяць')
    plt.xlabel('Місяць')
    plt.ylabel('Кількість відвідувань')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()
except:
    print("Виникла помилка")
