import pandas as pd

# Load data hasil integrasi
df = pd.read_csv("data_integration.csv")

validation_results = {}

# Validasi rentang logis
validation_results["Age_out_of_range"] = df[(df["Age"] < 0) | (df["Age"] > 120)]
validation_results["BMI_out_of_range"] = df[(df["BMI"] < 10) | (df["BMI"] > 60)]
validation_results["Blood_Pressure_out_of_range"] = df[(df["Blood_Pressure_mmHg"] < 60) | (df["Blood_Pressure_mmHg"] > 250)]

# Outlier dengan IQR
outlier_info = {}
for col in ["BMI", "Daily_Caloric_Intake", "Blood_Pressure_mmHg"]:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
    outlier_info[col] = outliers.shape[0]

# Simpan hasil validasi ke file
df.to_csv("data_validation.csv", index=False)

print("Tahap 4 selesai → data_validation.csv disimpan")
print("\nRingkasan Validasi:")
print("Outlier BMI:", outlier_info["BMI"])
print("Outlier Kalori:", outlier_info["Daily_Caloric_Intake"])
print("Outlier Tekanan Darah:", outlier_info["Blood_Pressure_mmHg"])
