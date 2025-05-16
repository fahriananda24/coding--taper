import pandas as pd

# Data dasar untuk absensi
data = {
    "Nama": [],  # Kosong dulu, bisa diisi manual nanti
    "Hadir": [],
    "Izin": [],
    "Sakit": [],
    "Alpha": []
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Menyimpan ke file Excel
filename = "Absensi_X_Teknik_Informatika_2025_2026.xlsx"
df.to_excel(filename, index=False)
