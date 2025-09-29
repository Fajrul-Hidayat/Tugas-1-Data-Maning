import pandas as pd

# 1. COLLECTING DATA
df_raw = pd.read_csv("diet_recommendations_dataset.csv", delimiter=";")

# Simpan salinan mentah
df_raw.to_csv("data_collecting.csv", index=False)

print("Tahap 1 selesai → data_collecting.csv disimpan")
print(df_raw.head())
