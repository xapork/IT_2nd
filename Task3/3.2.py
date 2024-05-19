import csv

with open('../data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Имя", "Фамилия", "Возраст"])
    writer.writerow(["Идиот", "Романенко", 100])
    writer.writerow(["Ольга", "Степанова", 18])
    writer.writerow(["Юстина", "Романенко", 17])


def print_csv(filename: str):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))


print_csv('../data.csv')