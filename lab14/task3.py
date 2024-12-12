import json
import numpy as np
import matplotlib.pyplot as plt  

try:
    read_file = open("data.json", "r", encoding='utf-8')
    input_data = json.load(read_file)
    y = [input_data[k]["К-ть опадів"] for k in input_data]
    x = [*range(1,29)]

    np.array(x)
    np.array(y)

    fig, ax = plt.subplots()
    ax.pie(y, labels = x)
    ax.axis("equal")
    plt.legend() 
    plt.show()
except:
    print("Помилка при зчитуванні з json-файлу")
