file_path = "/Users/v.winston.feng/Downloads/recap_inventory_20221208.csv"

def read_csv_to_pd(file_path):
    ## require csv file with both 'user_id' and 'drop_id' columns
    import pandas as pd
    df = pd.read_csv(file_path)
    return df[['user_id', 'drop_ids']]

def generate_output_file(size):
    upload_df = read_csv_to_pd(file_path)
    import numpy as np
    for k,g in upload_df.groupby(np.arange(len(upload_df))//size):
        g.to_csv('20221208_Export_{}.csv'.format(k+1), index=False)

size = 100000
generate_output_file(size)
