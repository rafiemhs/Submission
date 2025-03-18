import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Fungsi untuk membaca data utama dari Google Drive
@st.cache_data
def load_main_data():
    file_id = "1LE6uieh7S06vbGqYTkwIADlqCkWRRdJa"  # Ganti dengan ID file utama
    url = f"https://drive.google.com/uc?id={file_id}"
    return pd.read_csv(url)

# Fungsi untuk membaca data RFM dari Google Drive
@st.cache_data
def load_rfm_data():
    file_id = "1JYkSiIcoVdxKEk73uhGXsua4e-mX1aRC"  # Ganti dengan ID file RFM
    url = f"https://drive.google.com/uc?id={file_id}"
    return pd.read_csv(url)

# Load Data
data = load_main_data()
rfm = load_rfm_data()

# Sidebar Menu
st.sidebar.title("📊 Dashboard Analisis Data")
menu = st.sidebar.radio("Pilih Analisis:", ["Overview", "Pola Pembelian", "Distribusi Geografis", "RFM Analysis"])

# Overview
if menu == "Overview":
    st.title("📊 Overview Data")
    st.write("### 🔍 Ringkasan Data")
    st.write("Bagian ini menyajikan ringkasan statistik dari dataset, seperti nilai rata-rata, nilai minimum, dan maksimum untuk setiap variabel numerik.")
    st.write(data.describe())

    st.write("### 🏷️ Sampel Data")
    st.write("Berikut adalah contoh beberapa baris data dari dataset yang digunakan dalam analisis ini:")
    st.write(data.head())

# Pola Pembelian
elif menu == "Pola Pembelian":
    st.title("🛒 Pola Pembelian Berdasarkan Kategori Produk")
    st.write("Analisis ini bertujuan untuk memahami kategori produk mana yang memberikan kontribusi pendapatan terbesar.")
    
    # Filter tahun (opsional, kalau ada kolom tanggal)
    if "order_purchase_timestamp" in data.columns:
        data["order_purchase_timestamp"] = pd.to_datetime(data["order_purchase_timestamp"])
        tahun_list = sorted(data["order_purchase_timestamp"].dt.year.unique(), reverse=True)
        tahun = st.sidebar.selectbox("Pilih Tahun:", tahun_list, index=0)
        data = data[data["order_purchase_timestamp"].dt.year == tahun]
    
    category_revenue = data.groupby("product_category_name")["price"].sum().sort_values(ascending=False).head(10)

    st.write("### 🔝 10 Kategori Produk Paling Menguntungkan")
    st.write("Grafik berikut menunjukkan 10 kategori produk dengan total pendapatan tertinggi. Hal ini membantu memahami preferensi pelanggan dan kategori produk yang paling menguntungkan bagi bisnis.")

    fig = px.bar(category_revenue, x=category_revenue.index, y=category_revenue.values, color=category_revenue.values,
                 color_continuous_scale="Blues", labels={"x": "Kategori Produk", "y": "Total Pendapatan"})
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)


# Distribusi Geografis
elif menu == "Distribusi Geografis":
    st.title("🌍 Distribusi Geografis Pelanggan")
    
    city_orders = data["customer_city"].value_counts().head(10)
    st.write("### 10 Kota dengan Pelanggan Terbanyak")
    fig = px.bar(city_orders, x=city_orders.index, y=city_orders.values, color=city_orders.values,
                 color_continuous_scale="Oranges", labels={"x": "Kota", "y": "Jumlah Pelanggan"})
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)

# RFM Analysis
elif menu == "RFM Analysis":
    st.title("📊 RFM Analysis")
    
    st.write("## 📌 Data RFM")
    st.write(rfm.head())
    
    # Distribusi Recency
    st.write("### 📌 Distribusi Recency")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(rfm["Recency"], bins=20, kde=True, ax=ax, color='green')
    st.pyplot(fig)

    # Distribusi Frequency
    st.write("### 📌 Distribusi Frequency")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(rfm["Frequency"], bins=20, kde=True, ax=ax, color='blue')
    st.pyplot(fig)

    # Distribusi Monetary
    st.write("### 📌 Distribusi Monetary")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(rfm["Monetary"], bins=20, kde=True, ax=ax, color='red')
    st.pyplot(fig)

st.sidebar.markdown("---")
st.sidebar.write("📌 **Dashboard interaktif ini dibuat menggunakan Streamlit**")
