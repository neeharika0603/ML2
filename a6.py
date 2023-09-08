import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import jaccard_score
from sklearn.metrics.pairwise import cosine_similarity

file_name = "19CSE305_LabData_Set3.1.xlsx"
worksheet_name = "thyroid0387_UCI"
data = pd.read_excel(file_name, sheet_name=worksheet_name)

vectors = data.iloc[:20, 1:-1]

def jaccard_coefficient(vector1, vector2):
    intersection = np.logical_and(vector1, vector2)
    union = np.logical_or(vector1, vector2)
    return np.sum(intersection) / np.sum(union)

jc_matrix = np.zeros((20, 20))
smc_matrix = np.zeros((20, 20))
cosine_matrix = np.zeros((20, 20))

for i in range(20):
    for j in range(20):
        vector1 = vectors.iloc[i].astype(bool)
        vector2 = vectors.iloc[j].astype(bool)
        jc_matrix[i, j] = jaccard_coefficient(vector1, vector2)
        smc_matrix[i, j] = jaccard_score(vector1, vector2, average='binary')
        cosine_matrix[i, j] = cosine_similarity([vector1], [vector2])[0, 0]

plt.figure(figsize=(10, 8))
sns.heatmap(jc_matrix, annot=True, fmt=".2f", cmap="YlGnBu", xticklabels=False, yticklabels=False)
plt.title("Jaccard Coefficient Heatmap")
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(smc_matrix, annot=True, fmt=".2f", cmap="YlGnBu", xticklabels=False, yticklabels=False)
plt.title("Simple Matching Coefficient Heatmap")
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(cosine_matrix, annot=True, fmt=".2f", cmap="YlGnBu", xticklabels=False, yticklabels=False)
plt.title("Cosine Similarity Heatmap")
plt.show()
