import pandas as pd
import glob
import os

# Define the source path for the original Excel files
path = r'C:/Your/Path/Excel_Files' 
all_files = glob.glob(os.path.join(path, "*.xlsx"))

# Use a list to store DataFrames for efficient concatenation (memory optimization)
df_list = []

for filename in all_files:
    print(f"Processing: {os.path.basename(filename)}")
    
    # Load data using 'openpyxl' engine to handle modern Excel formats
    # Note: Loading only required columns can further reduce RAM usage
    df = pd.read_excel(filename, engine='openpyxl')
    df_list.append(df)

# Consolidate all individual DataFrames into a single massive dataset
full_df = pd.concat(df_list, ignore_index=True)

# Export to Apache Parquet format (This is where the compression magic happens)
# We convert Gigabytes of raw data into Megabytes without any data loss
# Using 'pyarrow' engine and 'snappy' compression for high-performance I/O
full_df.to_parquet('pronostico_bi.parquet', engine='pyarrow', compression='snappy')

print(f"Finished! Total rows processed: {len(full_df)}")
