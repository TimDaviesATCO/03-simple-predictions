import pandas as pd

def load_data(data_file, sht_name, file_type):
    if file_type == 'Excel':
        df = pd.read_excel(io=data_file, sheet_name = sht_name)
    if file_type == 'CSV' or 'csv':
        df = pd.read_csv(data_file)
    return df
