import pandas as pd
import numpy as np

file_name = r"19CSE305_LabData_Set3.1.xlsx"
worksheet_name = 'thyroid0387_UCI'
data = pd.read_excel(file_name, sheet_name=worksheet_name)
data_types = data.dtypes

categorical_cols = data.select_dtypes(include=['object']).columns
nominal_cols = ['referral source'] + [col for col in data.columns if data[col].dtype == 'O' and data[col].str.contains(' ').any()]
ordinal_cols = list(set(categorical_cols) - set(nominal_cols))

numeric_variables = data.select_dtypes(include=['int64', 'float64'])
data_range = numeric_variables.max() - numeric_variables.min()

missing_values = data.isnull().sum()

outliers = {}
for col in numeric_cols.columns:
    mean = numeric_cols[col].mean()
    std = numeric_cols[col].std()
    lower_bound = mean - 3 * std
    upper_bound = mean + 3 * std
    outliers[col] = len(numeric_cols[(numeric_cols[col] < lower_bound) | (numeric_cols[col] > upper_bound)])

numeric_mean = numeric_cols.mean()
numeric_variance = numeric_cols.var()

print("Task 1: Data Types")
print(data_types)

print("\nTask 2: Encoding Schemes")
print("Nominal Columns:", nominal_cols)
print("Ordinal Columns:", ordinal_cols)

print("\nTask 3: Data Range")
print(data_range)

print("\nTask 4: Missing Values")
print(missing_values)

print("\nTask 5: Outliers")
print(outliers)

print("\nTask 6: Mean and Variance for Numeric Variables")
print("Mean:")
print(numeric_mean)
print("\nVariance:")
print(numeric_variance)
