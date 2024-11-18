#!/usr/bin/env python3
import pandas as pd
import numpy as np

def clean_oil_data(input_file_path, output_file_path):
    """
    Cleans the 'Estimated_Spill_Area' column in the Oil_2022.csv file
    Parameters:
    - input_file_path: str, path to the input CSV file.
    - output_file_path: str, path to save the cleaned CSV file
    Returns:
    - None, but saves the cleaned data to the specified output path.
    """
    # Load the dataset
    df = pd.read_csv(input_file_path)
    # Define the column to clean
    column_name = "Estimated_Spill_Area"
    # Remove non-numeric values (e.g., n/a, N/A, nill, etc.)
    df[column_name] = df[column_name].replace(['n/a', 'N/A', 'nill', ''], np.nan)
    # Convert to numeric values (ignoring non-convertible strings like "2376.90m2")
    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    # Handle specific cases where units are included (e.g., "m2")
    df[column_name] = df[column_name].apply(lambda x: float(str(x).replace('m2', '')) if isinstance(x, str) and 'm2' in str(x) else x)
    # Convert km^2 to m^2 (assuming all valid numeric values are in km^2)
    df[column_name] = df[column_name] * 1e6  # Convert km² to m²
    # Save the cleaned dataset to the output file path
    df.to_csv(output_file_path, index=False)
    # Confirm that the cleaned data was saved
    print(f"Cleaned data saved to {output_file_path}")
    # Optionally return the cleaned dataframe if needed for further use
    return df

