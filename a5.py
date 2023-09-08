import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

file_name = r"19CSE305_LabData_Set3.1.xlsx"
worksheet_name = 'thyroid0387_UCI'
data = pd.read_excel(file_name, sheet_name=worksheet_name)

vector1 = data.iloc[0, 1:].apply(lambda x: float(x) if str(x).replace('.', '', 1).isdigit() else np.nan)
vector2 = data.iloc[1, 1:].apply(lambda x: float(x) if str(x).replace('.', '', 1).isdigit() else np.nan)

dot_product = np.dot(vector1, vector2)

magnitude_vector1 = np.linalg.norm(vector1)
magnitude_vector2 = np.linalg.norm(vector2)

cosine_similarity = dot_product / (magnitude_vector1 * magnitude_vector2)

print("Cosine Similarity:", cosine_similarity)
