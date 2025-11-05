import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def prepare_smartphone_data(file_path):
    """
    To prepare the smartphone data for visualization, a number of transformations 
    will be applied after reading in the raw DataFrame to memory, including:
        - reducing the number of columns to only those needed for later analysis
        - removing records without a battery_capacity value
        - divide the price column by 100 to find the dollar amount
    
    :param file_path: the file path where the raw smartphone data is stored
    :return: a cleaned dataset having had the operations above applied to it
    """

    # Check first if the file exists
    if os.path.exists(file_path):
        raw_data = pd.read_csv(file_path)
        # Update 1: Variable name 'raw Data' changed to 'raw_data' for Python snake_case naming convention.
    else:
        raise Exception(f"File containing smartphone data not found at path {file_path}")

    # Keep only necessary columns for analysis
    features = [
        "brand_name",
        "os",
        "price",
        "avg_rating",
        "processor_speed",
        "battery_capacity",
        "screen_size"
    ]

    # Update 2: Renamed 'columns_to_keep_in_clean data' to 'feature_set' for clarity and succinctness.
    clean_data = raw_data.loc[:, features]
    
    # Remove entries without 'battery_capacity' or 'os'
    clean_data = clean_data.dropna(subset=["battery_capacity", "os"])
    # Update 3: Adjusted spacing in 'dropna' function call to improve readability.
    
    # Convert 'price' column to reflect dollar amounts
    clean_data["price"] = clean_data["price"] / 100
    # Update 4: Added spaces around '/' operator for better code readability.
    
    return clean_data


# Call the function to prepare data
cleaned_data = prepare_smartphone_data("./data/smartphones.csv")
