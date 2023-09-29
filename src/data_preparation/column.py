import pandas as pd

# Replace 'your_file.csv' with the actual path of your CSV file
file_path = "/home/soham/Project/NeuraPhrase/data/raw/temp2.csv"

# Read CSV file into a DataFrame
df = pd.read_csv(file_path)

# Get the column names
column_names = df.columns.tolist()

# Print the column names
print("Column Names:")
print(column_names)
