# 📊 Dashboard Analisis Data

Dashboard ini dibuat menggunakan **Streamlit** untuk menyajikan hasil analisis data secara interaktif.

## 📌 Fitur Dashboard
- **Overview**: Menampilkan ringkasan statistik data.
- **Pola Pembelian**: Menganalisis kategori produk berdasarkan total pendapatan.
- **Distribusi Geografis**: Melihat sebaran pelanggan berdasarkan kota.
- **RFM Analysis**: Menganalisis pelanggan menggunakan model **Recency, Frequency, Monetary (RFM)**.

---
## 🚀 Cara Menjalankan Dashboard

### 1️⃣ **Persyaratan**
Pastikan Anda telah menginstal **Python 3.8+** dan pustaka berikut:
```bash
pip install streamlit pandas plotly seaborn matplotlib
```

### 2️⃣ **Clone Repository** (Opsional)
Jika menggunakan Git:
```bash
git clone https://github.com/user/repository-name.git
cd repository-name
```

### 3️⃣ **Menjalankan Dashboard**
Gunakan perintah berikut di terminal atau command prompt:
```bash
streamlit run dashboard.py
```

---
## 📦 Struktur Proyek
```
📂 project-directory
├── 📄 dashboard.py  # Script utama Streamlit
├── 📄 requirements.txt  # dependencies atau pustaka (libraries) yang dibutuhkan
├── 📄 README.md     # Dokumentasi proyek
├── 📄 rfm_analysis.csv # dataset rfm
└── (untuk main data dan rfm analysis dipanggil melalui drive, karena file terlalu besar)
```

---
## 🎯 Catatan
- **Pastikan koneksi internet stabil** karena data diambil dari Google Drive.
- Jika ingin menggunakan dataset lokal, ubah bagian pemuatan data dalam `dashboard.py`.

Selamat mencoba! 🚀

