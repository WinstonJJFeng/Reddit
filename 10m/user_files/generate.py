file_path = "/Users/v.winston.feng/Downloads/batch_2.csv"

def read_csv_to_pd(file_path):
    ## require csv file with both 'user_id' and 'drop_id' columns
    import pandas as pd
    df = pd.read_csv(file_path)
    df = df[['user_id', 'drop_ids']]
#     df = df.sort_values(by='user_id').reset_index(drop=True)
    return df

def generate_output_file(size):
    upload_df = read_csv_to_pd(file_path)
    end = upload_df.shape[0]
    start = 0
    cut = 0
    import numpy as np
    for k,g in upload_df.groupby(np.arange(len(upload_df))//size):
        if start + size < end:
            cut += size
            g.to_csv('/Users/v.winston.feng/Downloads/output_files/20221214_batch_2/batch_2_from_{}_to_{}.csv'.format(start+1,cut), index=False)
            start += size            
        else:
            g.to_csv('/Users/v.winston.feng/Downloads/output_files/20221214_batch_2/batch_2_from_{}_to_{}.csv'.format(start+1,end), index=False)

size = 100000
generate_output_file(size)
