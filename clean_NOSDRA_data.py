#!/usr/bin/env python3

import pandas as pd

def clean_oil_data_excel(input_file_path, output_file_path):
    """
    Cleans the 'Estimated_Spill_Area' column in all sheets of an Excel file.
    
    Parameters:
    - input_file_path: str, path to the input Excel file.
    - output_file_path: str, path to save the cleaned Excel file.
    
    Returns:
    - None, but saves the cleaned data to the specified output path.
    """
    # Load the entire Excel file with multiple sheets
    excel_data = pd.read_excel(input_file_path, sheet_name=None)
    
    cleaned_sheets = {}
    
    for sheet_name, df in excel_data.items():
        if "Estimated_Spill_Area" in df.columns:
            # Remove non-numeric values and handle missing data
            df["Estimated_Spill_Area"] = df["Estimated_Spill_Area"].replace(['n/a', 'N/A', 'nill'], None)
            df["Estimated_Spill_Area"] = pd.to_numeric(df["Estimated_Spill_Area"], errors='coerce')
            
            # Convert km² to m² (if needed)
            df["Estimated_Spill_Area"] = df["Estimated_Spill_Area"].apply(lambda x: x * 1e6 if pd.notnull(x) else x)
        
        # Store the cleaned sheet
        cleaned_sheets[sheet_name] = df

    # Save the cleaned sheets to a new Excel file
    with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
        for sheet_name, df in cleaned_sheets.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    print(f"Cleaned data saved to {output_file_path}")

# Check if the script is run directly
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: ./clean_oil_data.py <input_file_path> <output_file_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    clean_oil_data_excel(input_file, output_file)
