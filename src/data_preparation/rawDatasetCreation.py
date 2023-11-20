import os
from datasets import load_dataset
import pandas as pd
import sys

def process_first_code():
    # Load the datasets
    dataset1 = load_dataset("meta-math/MetaMathQA")
    dataset2 = load_dataset("vikp/textbook_quality_programming")

    # Define chunk size based on available memory
    chunk_size = 500  # You can adjust this based on your available memory

    # Initialize an empty DataFrame for merged data
    merged_df = pd.DataFrame(columns=["prompt", "response"])

    # Process each chunk of the first dataset
    for chunk_start in range(0, len(dataset1["train"]["query"]), chunk_size):
        chunk_end = chunk_start + chunk_size

        # Extract the desired columns from the current chunk of dataset1
        column1 = dataset1["train"]["query"][chunk_start:chunk_end]
        column2 = dataset1["train"]["response"][chunk_start:chunk_end]

        # Extract the desired columns from the corresponding chunk of dataset2
        column3 = dataset2["train"]["topic"][chunk_start:chunk_end]
        column4 = dataset2["train"]["markdown"][chunk_start:chunk_end]

        # Create DataFrames for the current chunk
        df1 = pd.DataFrame({"prompt": column1, "response": column2})
        df2 = pd.DataFrame({"prompt": column3, "response": column4})

        # Concatenate DataFrames vertically
        merged_df = pd.concat([merged_df, df1, df2], axis=0)

    # Take csv_file_name as input
    csvfile = input("Enter new_csv File Name: ")

    # Specify the full path for saving the CSV file
    output_path = f"/home/soham/NeuraPhrase/data/raw/{csvfile}"

    # Ensure the directory exists, create it if needed
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the merged DataFrame to a CSV file
    merged_df.to_csv(output_path, index=False, escapechar='\\')

def process_second_code():
    # Taking dataset name and column name
    tempcsv = input("Enter Temporary csv file name: ")
    existCsv = f"/home/soham/NeuraPhrase/data/raw/{tempcsv}"
    new_dataset = input("Enter New Dataset path: ")
    col1 = input("Enter prompt column name: ")
    col2 = input("Enter response column name: ")
    key = input("Enter key name: ")

    # Define chunk size based on available memory
    chunk_size = 500  # You can adjust this based on your available memory

    # Load the datasets in chunks
    chunks1 = pd.read_csv(existCsv, chunksize=chunk_size)
    dataset2 = load_dataset(new_dataset)

    # Initialize an empty DataFrame for merged data
    merged_df = pd.DataFrame(columns=["prompt", "response"])

    # Process each chunk of the first dataset
    for chunk1 in chunks1:
        # Extract the desired columns from the current chunk
        column1 = chunk1["prompt"]
        column2 = chunk1["response"]

        # Extract the desired columns from the second dataset
        column3 = dataset2[key][col1]
        column4 = dataset2[key][col2]

        # Create DataFrames for the current chunk
        df1 = pd.DataFrame({"prompt": column1, "response": column2})
        df2 = pd.DataFrame({"prompt": column3, "response": column4})

        # Concatenate DataFrames vertically
        merged_df = pd.concat([merged_df, df1, df2], axis=0)

    # Take csv_file_name as input
    csvfile = input("Enter new_csv File Name: ")

    # Specify the full path for saving the CSV file
    output_path = f"/home/soham/NeuraPhrase/data/raw/{csvfile}"

    # Ensure the directory exists, create it if needed
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save the merged DataFrame to a CSV file
    merged_df.to_csv(output_path, index=False, escapechar='\\')

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ['-f', '-s']:
        print("Usage: python script.py [-f | -s]")
        sys.exit(1)

    if sys.argv[1] == '-f':
        process_first_code()
    elif sys.argv[1] == '-s':
        process_second_code()
    else:
        print("Invalid argument")

if __name__ == "__main__":
    main()
