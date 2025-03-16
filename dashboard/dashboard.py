import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


@st.cache_data
def load_data():
    file_id = "1IvXYeUe3quFHBHlkd2PGy-bY_dQ3SkJp" 
    url = f"https://drive.google.com/uc?id={file_id}"
    return pd.read_csv(url)

data = load_data()
st.write(data.head())

# Sidebar Menu
st.sidebar.title("Dashboard Analisis Data")
menu = st.sidebar.radio("Pilih Analisis:", ["Overview", "Pola Pembelian", "Distribusi Geografis", "RFM Analysis"])

# Overview
if menu == "Overview":
    st.title("📊 Overview Data")
    st.write("### Ringkasan Data")
    st.write(data.describe())
    st.write("### Sampel Data")
    st.write(data.head())

# Pola Pembelian
elif menu == "Pola Pembelian":
    st.title("🛒 Pola Pembelian Berdasarkan Kategori Produk")
    
    category_revenue = data.groupby("product_category_name")["price"].sum().sort_values(ascending=False).head(10)
    st.write("### 10 Kategori Produk Paling Menguntungkan")
    fig, ax = plt.subplots(figsize=(10, 5))
    category_revenue.plot(kind='bar', ax=ax, color='skyblue')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Distribusi Geografis
elif menu == "Distribusi Geografis":
    st.title("🌍 Distribusi Geografis Pelanggan")
    
    city_orders = data["customer_city"].value_counts().head(10)
    st.write("### 10 Kota dengan Pelanggan Terbanyak")
    fig, ax = plt.subplots(figsize=(10, 5))
    city_orders.plot(kind='bar', ax=ax, color='orange')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# RFM Analysis
@st.cache_data
def load_data():
    file_id = "1EkrihfkYyqp6B6yPgvqPgZAb4qWdcIoN" 
    url = f"https://drive.google.com/uc?id={file_id}"
    return pd.read_csv(url)

# Simulasi menu di Streamlit
menu = st.sidebar.selectbox("Pilih Menu", ["Home", "RFM Analysis"])

# Home
if menu == "Home":
    st.title("📊 Dashboard Analisis")
    st.write("Selamat datang di dashboard analisis!")

# RFM Analysis Menu
elif menu == "RFM Analysis":
    st.title("📊 RFM Analysis")

    # Load Data
    rfm = load_data()
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
