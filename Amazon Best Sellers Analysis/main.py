import pandas as pd

df = pd.read_csv('bestsellers.csv')

# Get the first 5 rows of the spreadsheet
print(df.head())

# Get the shape of the spreadsheet
print(df.shape)

# Get the column names of the spreadsheet
print(df.columns)

# Get summary statistics for each column
print(df.describe())

# Remove all duplicate rows
df.drop_duplicates(inplace=True)

# Rename column names to "Title", "Publication Year", and "Rating"
df.rename(columns={"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

# Convert "Price" column to use the float data type
df["Price"] = df["Price"].astype(float)