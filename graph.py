#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt

def oilspills(input_file, output_file_spills, output_file_tally):
    excel_file = pd.ExcelFile(input_file)
    print("Sheet names:", excel_file.sheet_names)
    NOSDRA = pd.read_excel(input_file, sheet_name='2019-2020')
    print(NOSDRA)

    # Clean up data
    NOSDRA['Estimated_Spill_Area'] = NOSDRA['Estimated_Spill_Area'].replace('', 0).astype(float)
    NOSDRA['Incident_Date'] = pd.to_datetime(NOSDRA['Incident_Date'], errors='coerce')

    # Tally spills over time (by month)
    NOSDRA['Month'] = NOSDRA['Incident_Date'].dt.to_period('M')
    tally = NOSDRA.groupby('Month').size()

    # Plot the tally of oil spills
    plt.figure(figsize=(10, 6))
    tally.plot(kind='bar', color='blue', alpha=0.7)
    plt.title('Number of Oil Spills Over Time (2019)')
    plt.xlabel('Month')
    plt.ylabel('Number of Spills')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_file_tally)

    # Plot estimated spill areas
    max_value = NOSDRA['Estimated_Spill_Area'].quantile(0.95)  # 95th percentile
    NOSDRA_filtered = NOSDRA[NOSDRA['Estimated_Spill_Area'] <= max_value]
    x = NOSDRA_filtered['Incident_Date']
    y = NOSDRA_filtered['Estimated_Spill_Area']

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='Spill Area')
    plt.title('2019 Oil Spills')
    plt.xlabel('Incident Date')
    plt.ylabel('Estimated Spill Area (m²)')
    plt.xticks(rotation=45)
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.tight_layout()
    plt.savefig(output_file_spills)

# Example Usage
input_file = 'final_NOSDRA.xlsx'
output_file_spills = '2019_plot_spills.png'
output_file_tally = '2019_tally.png'
oilspills(input_file, output_file_spills, output_file_tally)
