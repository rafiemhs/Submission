import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("main_data.csv")

data = load_data()

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
elif menu == "RFM Analysis":
    st.title("📈 RFM Analysis")
    
    rfm = pd.read_csv("rfm_analysis.csv")
    st.write("### Data RFM")
    st.write(rfm.head())
    
    st.write("### Distribusi Recency")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(rfm["Recency"], bins=20, kde=True, ax=ax, color='green')
    st.pyplot(fig)
    
    st.write("### Distribusi Frequency")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(rfm["Frequency"], bins=20, kde=True, ax=ax, color='blue')
    st.pyplot(fig)
    
    st.write("### Distribusi Monetary")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.histplot(rfm["Monetary"], bins=20, kde=True, ax=ax, color='red')
    st.pyplot(fig)
