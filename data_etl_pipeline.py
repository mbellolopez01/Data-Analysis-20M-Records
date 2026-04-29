import pandas as pd
import glob

# Consolidating 20M+ records from multiple Excel sources
path = './raw_data/' 
all_files = glob.glob(path + "*.xlsx")

li = []
for filename in all_files:
    # Efficiently reading large files
    df = pd.read_excel(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

# Exporting to Parquet for high-performance Power BI integration
frame.to_parquet('optimized_dataset.parquet', engine='pyarrow', compression='snappy')
