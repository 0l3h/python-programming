import numpy as np
import pandas as pd
import random

weeks = ['Понеділок', "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]*4
weather = dict()

for i in range(len(weeks)):
    weather[i+1] = { 
        'День': weeks[i],
        'Температура': round(random.uniform(-5, 20), 2),
        'К-ть опадів': round(random.random() * 5, 2)
    }
    weather[i+1]['Вид опадів'] = "Дощ" if weather[i+1]['Температура'] > 0 else "Сніг"

weather_df = pd.DataFrame.from_dict(weather, orient='index')
average_temp_by_day = weather_df.groupby('День')['Температура'].mean().reset_index()
average_temp_by_day.columns = ['День', 'Середня температура']

print(average_temp_by_day)
