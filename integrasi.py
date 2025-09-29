import pandas as pd
import numpy as np

# Load data hasil collecting
df = pd.read_csv("data_collecting.csv")

# Fungsi membersihkan format angka salah (misal 58.04.00 → 58.04)
def clean_numeric(val):
    try:
        if isinstance(val, str):
            parts = val.split(".")
            if len(parts) > 2:
                val = ".".join(parts[:2])
        return float(val)
    except:
        return np.nan

# Kolom numerik yang perlu dibersihkan
numeric_columns = [
    "Weight_kg", "BMI", "Cholesterol_mg/dL",
    "Glucose_mg/dL", "Adherence_to_Diet_Plan",
    "Weekly_Exercise_Hours", "Dietary_Nutrient_Imbalance_Score"
]

for col in numeric_columns:
    df[col] = df[col].apply(clean_numeric)

# Pastikan tipe data numerik
df["Daily_Caloric_Intake"] = pd.to_numeric(df["Daily_Caloric_Intake"], errors="coerce")
df["Height_cm"] = pd.to_numeric(df["Height_cm"], errors="coerce")
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Blood_Pressure_mmHg"] = pd.to_numeric(df["Blood_Pressure_mmHg"], errors="coerce")

# Simpan hasil integrasi
df.to_csv("data_integration.csv", index=False)

print("Tahap 2 selesai → data_integration.csv disimpan")
print(df.head())
