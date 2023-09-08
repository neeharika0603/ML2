import pandas as pd
import numpy as np

file_name = r"19CSE305_LabData_Set3.1.xlsx"
worksheet_name = 'thyroid0387_UCI'
data = pd.read_excel(file_name, sheet_name=worksheet_name)

data.replace(' ', np.nan, inplace=True)

for col in data.columns:
    if data[col].dtype == 'float64' or data[col].dtype == 'int64':
     
        if col in ['TSH', 'T3', 'TT4', 'T4U', 'FTI']:
            data[col].fillna(data[col].median(), inplace=True)
        else:
            data[col].fillna(data[col].mean(), inplace=True)
    elif data[col].dtype == 'object':
        data[col].fillna(data[col].mode()[0], inplace=True)

missing_values_after_imputation = data.isnull().sum()

print("Missing Values After Imputation:")
print(missing_values_after_imputation)
