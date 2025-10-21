import json
import csv

with open('Модуль 1\Заказчики.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(data)

headers = list(data[0].keys())

with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, fieldnames=headers, delimiter=";")

    for item in data:
        writer.writerow(item)