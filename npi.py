import polars as pl
import pandas as pd
import time

npi = pd.read_csv ('./Module1_MedicalCodexes/npi/npi_25.csv')

## just load the first 1000 rows
start_time_polars = time.time()
df_polars = pl.read_csv(npi_file_path) #, n_rows=1_000_000)
end_time_polars = time.time()
elapsed_time_polars = end_time_polars - start_time_polars
print(elapsed_time_polars)


start_time_pandas = time.time()
df_pandas = pd.read_csv(npi_file_path, nrows=1000000, low_memory=False)
end_time_pandas = time.time()
elapsed_time_pandas = end_time_pandas - start_time_pandas
print(elapsed_time_pandas)



print(f"Successfully loaded {len(df_polars)} records from NPI data")
print(f"Columns: {df_polars.columns}")
print(f"\nDataset shape: {df_polars.shape}")
print(f"\nFirst 5 rows:")
print(df_polars.head())

print(f"\nMemory usage (MB): {df.estimated_size() / 100**2:.2f}")


df_polars_small = df_polars.select([
    'NPI', 
    'Provider Last Name (Legal Name)'
])


df_polars_small = df_polars_small.rename({
    'NPI': 'code',
    'Provider Last Name (Legal Name)': 'description',
    'last_updated': 'last_updated'
})


output_path = 'Module1_MedicalCodexes/npi/output/npi_25.csv'
df_polars_small.write_csv(output_path)
df_polars_small.write_parquet('Module1_MedicalCodexes/npi/output/npi_small.parquet')

