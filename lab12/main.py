import json
import pprint
import os

try:
    read_file = open("data.json", "r", encoding='utf-8')
    input_data = json.load(read_file)
    result = {k: input_data[k] for k in input_data}

    def add_record():
        print("Введіть нові дані")
        day = input("День (число): ")
        
        if day not in result:
            result[day] = {
                "Температура": int(input("Введіть температуру: ")),
                "Назва дня": input("Введіть назву дня: "),
                "К-ть опадів": float(input("Введіть к-ть опадів: "))
            }
            result[day]["Вид опадів"] = "Дощ" if input_data[key]['Температура'] > 0 else "Сніг"

        with open('result.json', 'w', encoding='utf-8') as result_file:
                json.dump(result, result_file, indent=4, ensure_ascii=False)
        print("Нові дані додано")

    def delete_record():
        day = input("Введіть день (число) для якого видалити дані: ")

        if day in result:
            del result[day]
            print("Дані для вказаного дня видалені")
            
            with open('result.json', 'w', encoding='utf-8') as result_file:
                json.dump(result, result_file, indent=4, ensure_ascii=False)
        else:
            print("Немає даних для вказаного дня")

    def find_record():
        day = input("Введіть день (число) який шукаєте: ")
        
        if day in input_data:
            print(input_data[day])
        else:
            print("Не знайдено даних для вказаного дня")
    
    for i in range(len(input_data)):
        key = str(i + 1)
        result[key]['Вид опадів'] = "Дощ" if input_data[key]['Температура'] > 0 else "Сніг"
    
    with open('result.json', 'w', encoding='utf-8') as result_file:
        json.dump(result, result_file, indent=4, ensure_ascii=False)   

    pprint.pprint(result)
    find_record()
    delete_record()
    pprint.pprint(result)
    add_record()
    pprint.pprint(result)

    read_file.close()
    result_file.close()
except:
    print('Помилка при роботі з файлами')
