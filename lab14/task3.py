import json
import numpy as np
import matplotlib.pyplot as plt  

try:
    with open("data.json", "r", encoding='utf-8') as read_file:
        input_data = json.load(read_file)
    
    total_precipitation = sum(input_data[k]["К-ть опадів"] for k in input_data)
    percentages = [(input_data[k]["К-ть опадів"] / total_precipitation) * 100 for k in input_data]
    days = [int(k) for k in input_data]

    fig, ax = plt.subplots()
    ax.pie(percentages, labels=days, autopct='%1.1f%%')
    ax.axis("equal")
    plt.title("Відсоток опадів за кожен день")
    plt.legend() 
    plt.show()
except Exception as e:
    print(f"Помилка при зчитуванні з json-файлу: {e}")
