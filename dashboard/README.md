# 📊 Dashboard Interaktif dengan Streamlit

Dashboard ini dibuat menggunakan **Streamlit** untuk menganalisis data e-commerce, termasuk pola pembelian pelanggan, distribusi geografis, dan analisis RFM.

## 📌 Fitur Utama
- **Overview Data**: Menampilkan informasi dasar dan ringkasan statistik.
- **Analisis Pola Pembelian**: Visualisasi kategori produk dengan pendapatan tertinggi.
- **Analisis Geografis**: Distribusi pelanggan berdasarkan kota.
- **Analisis RFM**: Klasifikasi pelanggan berdasarkan Recency, Frequency, dan Monetary.

## 📂 Struktur Direktori
```
📁 project-directory
│── dashboard.py                # Script utama untuk menjalankan dashboard
│── main_data.csv            # Data utama yang digunakan untuk analisis
│── rfm_analysis.csv         # Hasil analisis RFM
```

## 🚀 Cara Menjalankan Dashboard
### 1️⃣ Instalasi Dependensi
Pastikan Python telah terinstal, lalu jalankan perintah berikut:
```sh
pip install -r requirements.txt
```

### 2️⃣ Menjalankan Streamlit
Gunakan perintah berikut untuk menjalankan dashboard:
```sh
streamlit run dashboard.py
```

### 3️⃣ Mengakses Dashboard
Setelah dijalankan, Streamlit akan memberikan URL lokal seperti:
```
http://localhost:8501
```
Buka URL tersebut di browser untuk melihat tampilan dashboard.

## 🛠️ Requirements
Dependensi proyek ini terdapat dalam **requirements.txt**, yang mencakup:
```
pandas
streamlit
matplotlib
seaborn
```
Untuk menginstalnya secara manual, jalankan:
```sh
pip install pandas streamlit matplotlib seaborn
```
