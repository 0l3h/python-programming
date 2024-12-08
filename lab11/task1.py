import csv

try:
    with open('data.csv', newline='') as read_file: 
        reader = csv.reader(read_file)
        write_file = open('result.csv', 'w', newline='')
        writer = csv.writer(write_file)
        
        writer.writerow(["Lowest GDP", "Highest GDP"])

        next(reader)

        max_value = float('-inf')
        min_value = float('inf')

        max_row = None
        min_row = None
        
        for row in reader:
            if row[4] != '..':
                value = float(row[4])
                
                if value > max_value:
                    max_value = value
                    max_row = row
                
                if value < min_value:
                    min_value = value
                    min_row = row
        
        writer.writerow([min_row[2], max_row[2]])
        writer.writerow([min_value, max_value])
        
        print(max_row)
        print(min_row)
except:
    print("Помилка при роботі з CSV-файлами")
    pass
