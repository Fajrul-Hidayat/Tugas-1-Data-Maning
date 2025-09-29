import pandas as pd

# Load data hasil integrasi
df = pd.read_csv("data_integration.csv")

# Statistik deskriptif
stats = df.describe()

# Distribusi penyakit
disease_counts = df["Disease_Type"].value_counts()

# Rata-rata BMI, Kalori, Tekanan Darah per penyakit
grouped_means = df.groupby("Disease_Type")[["BMI", "Daily_Caloric_Intake", "Blood_Pressure_mmHg"]].mean()

# Gabungkan semua hasil ke dalam 1 file CSV
with open("data_analysis.csv", "w") as f:
    f.write("=== Statistik Deskriptif ===\n")
    stats.to_csv(f)
    
    f.write("\n\n=== Distribusi Penyakit ===\n")
    disease_counts.to_csv(f, header=["Count"])
    
    f.write("\n\n=== Rata-rata BMI, Kalori, Tekanan Darah per Penyakit ===\n")
    grouped_means.to_csv(f)

print("Hasil analisis sudah tersimpan di data_analysis.csv")
