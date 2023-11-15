import os
from datasets import load_dataset
import pandas as pd
'''
# Taking dataset name and column name
tempcsv = input("Enter Temporary csv file name: ")
existCsv = f"/home/soham/Project/NeuraPhrase/data/raw/{tempcsv}"
new_dataset = input("Enter New Dataset path: ")
col1 = input("Enter prompt column name: ")
col2 = input("Enter response column name: ")
key = input("Enter key name: ")

# Load the datasets
dataset1 = pd.read_csv(existCsv)
dataset2 = load_dataset(new_dataset)

# Extract the desired columns from both datasets
column1 = dataset1["prompt"]
column2 = dataset1["response"]
column3 = dataset2[key][col1]
column4 = dataset2[key][col2]
'''

# Load the datasets
dataset1 = load_dataset("meta-math/MetaMathQA")
dataset2 = load_dataset("vikp/textbook_quality_programming")

# Extract the desired columns from both datasets
column1 = dataset1["train"]["query"]
column2 = dataset1["train"]["response"]
column3 = dataset2["train"]["topic"]
column4 = dataset2["train"]["markdown"]


# Create DataFrames for the desired columns
df1 = pd.DataFrame({"prompt": column1, "response": column2})
df2 = pd.DataFrame({"prompt": column3, "response": column4})

# Concatenate DataFrames vertically
merged_df = pd.concat([df1, df2], axis=0)

# Take csv_file_name as input
csvfile = input("Enter new_csv File Name: ")

# Specify the full path for saving the CSV file
output_path = f"/home/soham/Project/NeuraPhrase/data/raw/{csvfile}"

# Ensure the directory exists, create it if needed
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Save the merged DataFrame to a CSV file
merged_df.to_csv(output_path, index=False, escapechar='\\')
