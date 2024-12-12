#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

def oilspills(input_file, output_file):
    excel_file = pd.ExcelFile(input_file)
    print("Sheet names:", excel_file.sheet_names)
    NOSDRA = pd.read_excel(input_file, sheet_name='2019-2020')
    print(NOSDRA)

    NOSDRA['Estimated_Spill_Area'] = NOSDRA['Estimated_Spill_Area'].replace('', 0).astype(float)

    # Filter out extreme outliers for better scaling
    max_value = NOSDRA['Estimated_Spill_Area'].quantile(0.95)  # 95th percentile
    NOSDRA_filtered = NOSDRA[NOSDRA['Estimated_Spill_Area'] <= max_value]

    # Plot the filtered data
    x = pd.to_datetime(NOSDRA_filtered['Incident_Date'])
    y = NOSDRA_filtered['Estimated_Spill_Area']

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='Spill Area')
    plt.title('2019 Oil Spills')
    plt.xlabel('Incident Date')
    plt.ylabel('Estimated Spill Area (m²)')
    plt.xticks(rotation=45)
    plt.yscale('linear')  # Or use 'log' for a logarithmic scale
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()

    # Annotate outliers (if needed)
    outliers = NOSDRA[NOSDRA['Estimated_Spill_Area'] > max_value]
    for _, row in outliers.iterrows():
        plt.scatter(pd.to_datetime(row['Incident_Date']), row['Estimated_Spill_Area'], color='red')
        plt.text(pd.to_datetime(row['Incident_Date']), row['Estimated_Spill_Area'], f"{row['Estimated_Spill_Area']:.0f}", color='red')

    plt.savefig(output_file)

# Example Usage
input_file = 'final_NOSDRA.xlsx'
output_file = '2019_plot.png'
oilspills(input_file, output_file)
