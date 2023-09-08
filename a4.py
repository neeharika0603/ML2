import pandas as pd

file_name = r"19CSE305_LabData_Set3.1.xlsx"
worksheet_name = 'thyroid0387_UCI'
data = pd.read_excel(file_name, sheet_name=worksheet_name)

binary_attributes = ['on thyroxine', 'query on thyroxine', 'on antithyroid medication',
                     'sick', 'pregnant', 'thyroid surgery', 'I131 treatment', 'query hypothyroid',
                     'query hyperthyroid', 'lithium', 'goitre', 'tumor', 'hypopituitary']

vector1 = data.loc[0, binary_attributes].astype(str)
vector2 = data.loc[1, binary_attributes].astype(str)

f11 = sum((vector1 == '1') & (vector2 == '1'))
f01 = sum((vector1 == '0') & (vector2 == '1'))
f10 = sum((vector1 == '1') & (vector2 == '0'))
f00 = sum((vector1 == '0') & (vector2 == '0'))

if f01 + f10 + f11 != 0:
    jc = f11 / (f01 + f10 + f11)
else:
    jc = 0.0

if f00 + f01 + f10 + f11 != 0:
    smc = (f11 + f00) / (f00 + f01 + f10 + f11)
else:
    smc = 0.0 
    
print("Jaccard Coefficient (JC):", jc)
print("Simple Matching Coefficient (SMC):", smc)
