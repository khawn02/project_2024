# project_2024
# INTRODUCTION
## From 1990 to present day Rivers State, Nigeria has been subjected to ongoing oil spills from refineries and underground oil and gas pipelines. Unfortunately, due to the vastness of land, limited accessability to pipelines and even lesser regulations on oil companies has led to much of the land becoming inaccessable. This lack in ground coverage by service teams and reconstruction units means there is not accurate data on the current state of the oil spills present. For this reason, the use of Geographic Interface Systems of GIS through the use of satellite imagery is a neew wave of interpreting ground levels of inaccessible regions.
Issue:
Data for oil spills is contained within the National Oil Spill Detection and Response Agency (NOSDRA) 
Data was obtained through https://oilspillmonitor.ng/ specifically for the Rivers State region between 2019- 2022. Unfortunately to obtain the data you have to copy and paste it into an excell file where headers are missing and data is non-normalized. Additionally, we wanted to use the estimated areas to map real time area of detected oil spills, a colun not recognized by excell as numerical.
Solution: 
The first function produced was add_headers_to_excel. This function has the ability to fill in the designated headers found in NOSDRAs data set for each sheet of the years we wanted and saves as a new file.  
The code starts out with a shebang line so bash can tell python3 to use the script.
The function is defined as add_headers_to_excel that takes three arguments input_file(path), output_file (path to excel file), headers (the list of columns).
The following command then uses panda to read the input excel file assuming it doesnt contain headers, load all the sheets, assigns the new headers limited to the number of columns and saves the excell file as a new file using openxl engine. To then use the function simply run add_headers_to_excel(input_file, output_file, headers) where input_file is the location of original NOSDRA data and the output is name and location of updated excell sheets. 

#2 Solution is the function was created using the script clean_NOSDRA_data.py
the function name in the dictionary was clean_oil_data_excel. This was used to clean up the column Estimated_Spill_Area and normalize the column so everything was in square meters. 
The function iterated accross the three sheets of oil spill data using the excell sheet created using the function above.It worked by reading the sheet for the desired column, changes orientation to numeric values, cleaned it of any missing data or charachters such as NA, NIL, etc. The data once cleaned assumed any rows not in square kilometers would remain and the rest would be converted to square meters before getting saved to a new excel file. 
