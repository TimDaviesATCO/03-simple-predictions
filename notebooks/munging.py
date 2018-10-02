import pandas as pd

def load_data(data_file, sht_name, file_type):
    excel_filetypes = ['Excel', 'xls', 'XLS', 'xlsx']
    csv_filetypes = ['CSV' or 'csv']
    
    if file_type in excel_filetypes
        try:
            df = pd.read_excel(io=data_file, sheet_name = sht_name)
        except:
            print ("Error opening file.")
    
    if file_type in csv_filetypes:
        try:
            df = pd.read_csv(data_file)
        except:
            print ("Error opening file.")
    
    return df
