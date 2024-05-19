import csv

def sum_column(filename, column_index):
    total_sum = 0
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                value = float(row[column_index])
                total_sum += value
            except ValueError:
                pass
    return total_sum


filename = './data.csv'
column_index = 2
total_sum = sum_column(filename, column_index)
print(f"Сумма столбца {column_index}: {total_sum}")
