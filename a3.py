import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

file_name = r"19CSE305_LabData_Set3.1.xlsx"
worksheet_name = 'thyroid0387_UCI'
data = pd.read_excel(file_name, sheet_name=worksheet_name)

data.replace(' ', pd.NA, inplace=True)

numeric_attributes = ['age', 'TSH', 'T3', 'TT4', 'T4U', 'FTI']

minmax_scaler = MinMaxScaler()
data[numeric_attributes] = minmax_scaler.fit_transform(data[numeric_attributes])

print("Normalized Data:")
print(data.head())
