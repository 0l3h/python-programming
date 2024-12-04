import random
import pprint

def print_all():
    print("Виведення даних про опади за один місяць")
    pprint.pprint(weather)

def print_sorted():
    print("Словник відсортований в оберненому порядку:")
    sorted_data = {k: weather[k] for k in sorted(weather.keys(), key=int, reverse=True)}
    pprint.pprint(sorted_data, sort_dicts=False)

def delete_record():
    day = int(input("Введіть день (число) для видалення: "))
    del weather[day]
    print("Дані про опади для вказаного дня видалено")

def add_record():
    print("Введіть дані для іншого дня")
    day = int(input("Введіть день (число): "))
    if day not in weather:
        weather[day] = {
            "День": "", 
            "К-ть опадів": 0.0, 
            "Температура": 0.0
        }
        weather[day]['Вид опадів'] = "Дощ" if weather[day]['Температура'] > 0 else "Сніг"

    if not weather[day]["День"]:
        weather[day]["День"] = input("Введіть назву дня: ")

    weather[day]["К-ть опадів"] = float(input("Кількість опадів (мм): "))
    weather[day]["Температура"] = float(input("Температура: "))

weeks = ['Понеділок', "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота", "Неділя"]*4
weather = dict()

for i in range(len(weeks)):
    weather[i+1] = { 
        'День': weeks[i],
        'Температура': round(random.uniform(-5, 20), 2), 
        'К-ть опадів': round(random.random() * 5, 2)
    }
    weather[i+1]['Вид опадів'] = "Дощ" if weather[i+1]['Температура'] > 0 else "Сніг"

print_all()
delete_record()
print_all()
add_record()
print_sorted()
