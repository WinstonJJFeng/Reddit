file_path = "/Users/v.winston.feng/Downloads/bquxjob_58a3eb3d_184eef0eaa9.csv"

def read_csv_to_pd(file_path):
    ## require csv file with both 'user_id' and 'drop_id' columns
    import pandas as pd
    pd.read_csv(file_path)
    return df[['user_id', 'drop_id']]

def generate_output_file(size):
    upload_df = read_csv_to_pd(file_path)
    import numpy as np
    for k,g in upload_df.groupby(np.arange(len(upload_df))//size):
        g.to_csv('Export_{}.csv'.format(k+1), index=False)

size = 30       
generate_output_file(size)
