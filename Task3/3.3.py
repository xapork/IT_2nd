import pandas as pd


def min_value_csv_file(filename: str, column_name: str):
    data = pd.read_csv(filename)

    if column_name in data.columns:
        return data[column_name].min()
    else:
        print(f"Столбец '{column_name}' в файле '{filename}' не существует")



filename = 'https://gist.githubusercontent.com/sathwika456/485dbd3fa8a1abc348694ae692695fdb/raw/f5202f67da57b3e3875e04682db73e15ac1992ad/weather.csv'
column_name = 'Temperature'

print(min_value_csv_file(filename, column_name))
