import pandas as pd


def union(file_names: list[str], output_file: str):
    df_list = []
    for file_name in file_names:
        df = pd.read_csv(file_name)
        df_list.append(df)

    combined_df = pd.concat(df_list, ignore_index=True)

    combined_df.to_csv(output_file, index=False)


csv_one = "./one.csv"
csv_two = "./two.csv"

union(file_names=[csv_one, csv_two], output_file="./result.csv")