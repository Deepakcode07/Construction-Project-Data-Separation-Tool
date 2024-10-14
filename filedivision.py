import pandas as pd

# Path to the original CSV file
input_csv_file = r'D:\fabricspark_transformation\data_gen\construction_project_data_final.csv'

# Read the entire CSV file into a DataFrame
df = pd.read_csv(input_csv_file)

# Print available columns to check
print("Available columns in the CSV:", df.columns)

# Define the columns for each file with corrected names
project_columns = [
    "projectCode", "projectName", "BuilderCode", "rateSqMeter", "year", 
    "location", "stage", "dimension", "Flat_available", "totalOccupied_flat", 
    "totalBooked", "onTime", "expectedDeliveryDate", "actualDeliveryDate", 
    "interiorQualityRating", "exteriorQualityRating", "societyRating", 
    "securityRating", "amenities", "date", "customerCode"
]

customer_columns = [
    "customerCode", "projectCode", "propertyType", "customerName", 
    "customerEmail", "customerPhone", "possessionDate"
]

builder_columns = [
    "BuilderCode", "builder_name", "BuilderRating"
]

material_columns = [
    "materialCode", "materialName", "materialDescription", 
    "materialPrice", "projectCode", "date", "materialQty", "unit"
]

property_columns = [
    "propertyCode", "projectCode", "propertyType", "propertyAddress", 
    "propertyArea", "propertyPrice"
]

# Output file paths
project_file = r'D:\fabricspark_transformation\Seperated_file\project_data.csv'
customer_file = r'D:\fabricspark_transformation\Seperated_file\customer_data.csv'
builder_file = r'D:\fabricspark_transformation\Seperated_file\builder_data.csv'
material_file = r'D:\fabricspark_transformation\Seperated_file\material_data.csv'
property_file = r'D:\fabricspark_transformation\Seperated_file\property_data.csv'

# Check if columns exist in the DataFrame before saving
for col_set, file_name in zip([project_columns, customer_columns, builder_columns, material_columns, property_columns],
                              [project_file, customer_file, builder_file, material_file, property_file]):
    missing_cols = [col for col in col_set if col not in df.columns]
    if missing_cols:
        print(f"Missing columns for {file_name}: {missing_cols}")
    else:
        df[col_set].to_csv(file_name, index=False)

print("CSV files successfully created where applicable!")
