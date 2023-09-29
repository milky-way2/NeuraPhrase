import pandas as pd

# Replace 'file1.csv' and 'file2.csv' with your actual file paths
file_path = "/home/soham/Project/NeuraPhrase/data/raw"
file1_path = f"{file_path}/merged_dataset.csv"
file2_path = f"{file_path}/temp.csv"

# Read CSV files into DataFrames
df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)

# Get the number of rows in each DataFrame
num_rows_file1 = df1.shape[0]
num_rows_file2 = df2.shape[0]

# Print the results
print(f"Number of rows in {file1_path}: {num_rows_file1}")
print(f"Number of rows in {file2_path}: {num_rows_file2}")
