# Dashboard Panduan Penggunaan

## 📌 Persyaratan

Sebelum menjalankan dashboard, pastikan Anda memiliki:

- Python (>=3.7)
- Pip (terinstal dengan Python)
- Virtual environment (opsional, tapi disarankan)
- Streamlit (untuk menjalankan dashboard)

## 🛠 Instalasi

1. **Clone repository ini** atau pindahkan file ke direktori kerja Anda:

   ```sh
   git clone <repo-url>
   cd <nama-folder>
   ```

2. **Buat virtual environment (opsional, tetapi disarankan):**

   ```sh
   python -m venv venv
   source venv/bin/activate  # Untuk macOS/Linux
   venv\Scripts\activate     # Untuk Windows
   ```

3. **Instal dependensi yang dibutuhkan:**

   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Menjalankan Dashboard

Dashboard ini dibuat menggunakan **Streamlit**. Untuk menjalankannya, gunakan perintah berikut:

```sh
streamlit run dashboard.py
```

Setelah perintah dijalankan, Streamlit akan otomatis membuka dashboard di browser.

## 🏗 Struktur Proyek

```
📂 project-folder
├── 📜 dashboard.py    # File utama dashboard
├── 📜 main_data.csv   # Dataset yang digunakan
├── 📜 requirements.txt # Daftar pustaka yang dibutuhkan
└── 📜 README.md       # Panduan penggunaan ini
```

## ❓ Troubleshooting

Jika terjadi masalah saat menjalankan dashboard, coba langkah berikut:

- Pastikan semua pustaka telah diinstal dengan benar
- Periksa versi Python dan Streamlit yang digunakan
- Pastikan file **main_data.csv** ada di direktori yang sama dengan **dashboard.py**
- Jika ada error spesifik, coba cari solusinya di [dokumentasi Streamlit](https://docs.streamlit.io/)

Selamat mencoba! 🚀

