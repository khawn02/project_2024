#!/usr/bin/env python3
import pandas as pd

def add_headers_to_excel(input_file, output_file, headers):
    try:
        excel_data = pd.read_excel(input_file, sheet_name=None, header=None)  # Load all sheets
    except FileNotFoundError:
        print(f"File not found: {input_file}. Please check the file path.")
        return

    updated_sheets = {}

    # Iterate through each sheet and add headers
    for sheet_name, data in excel_data.items():
        data.columns = headers[:len(data.columns)]  # Limit headers to match the number of columns in the sheet
        updated_sheets[sheet_name] = data

    # Save the updated data back to a new Excel file
    with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
        for sheet_name, data in updated_sheets.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Headers added to all sheets and saved to {output_file}")
headers = [
    "ID", "Status", "Zonal_Office", "Company", "Incident_Num", "Incident_Date",
    "Report_Date", "Containment", "Estimated_Quantity", "Quantity_Recovered",
    "Spill_Stop", "Facility", "Cause", "Initial_containment", "Site_Location",
    "Latitude", "Longitude", "LGA", "Estimated_Spill_Area", "Habitat", "Note", "State", "NA", "Form_A", "B", "C", "JIV_Date", "Present_JIV", "CleanUp_Date", "CleanUp_Completed", "Methods", "Inspection", "Assessment", "Remediation_Start", "Remediation_End", "type", "FinalSampling", "Final_Lab", "Certificate", "Cert.Num", "Update"
]

input_file = "OIL_Spill_2019_2022.xlsx"  #your input file
output_file = "NOSDRA_headers.xlsx"  # Update with the desired output path

# Call the function to add headers
add_headers_to_excel(input_file, output_file, headers)
