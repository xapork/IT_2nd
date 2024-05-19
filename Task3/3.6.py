import pandas as pd
import glob
import os


def combine_csv_files_by_user_id(directory):
    file_pattern = os.path.join(directory, '*.csv')
    all_files = glob.glob(file_pattern)

    df_list = []

    for file in all_files:
        df = pd.read_csv(file)
        df_list.append(df)

    if not df_list:
        print("Нет файлов для обработки.")
        return pd.DataFrame()

    combined_df = df_list[0]
    for df in df_list[1:]:
        combined_df = pd.merge(combined_df, df, on='user_id', how='outer')

    return combined_df


directory = './data/'

combined_data = combine_csv_files_by_user_id(directory)

print(combined_data.to_string())
