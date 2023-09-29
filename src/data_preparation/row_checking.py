import pandas as pd

# Replace 'your_file.csv' with the actual path of your CSV file
tempcsv = input("Enter Temporary csv file name: ")
file_path = f"/home/soham/Project/NeuraPhrase/data/raw/{tempcsv}"

# Read CSV file into a DataFrame
df = pd.read_csv(file_path)

# Print the first row
print("First Row:")
print(df.head(1))

# Print the last row
print("\nLast Row:")
print(df.tail(1))
