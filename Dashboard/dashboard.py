import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data dengan optimasi
@st.cache_data
def load_data(nrows=None):
    df = pd.read_csv("main_data.csv", nrows=nrows, low_memory=True)
    
    # Konversi kolom numerik yang terbaca sebagai object
    for col in df.select_dtypes(include=['object']).columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except ValueError:
            pass
    
    # Konversi kolom tanggal jika ada
    date_cols = ["order_purchase_timestamp", "order_approved_at", "order_delivered_carrier_date", "order_delivered_customer_date", "order_estimated_delivery_date"]
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    
    # Mengisi nilai NaN dengan rata-rata untuk kolom numerik
    df.fillna(df.select_dtypes(include=['number']).mean(), inplace=True)
    
    return df

df = load_data()

# Sidebar untuk filter dan pilihan kolom
st.sidebar.header("Filter Data")
columns = df.select_dtypes(include=['number']).columns.tolist()
selected_col = st.sidebar.selectbox("Pilih Kolom untuk Visualisasi", columns if columns else [None])
nrows = st.sidebar.slider("Jumlah Data yang Ditampilkan", min_value=1000, max_value=len(df), value=5000, step=1000)

df = load_data(nrows)

# Main Dashboard
st.title("📊 Dashboard Analisis Data Interaktif")
st.markdown("### Selamat datang di dashboard interaktif untuk eksplorasi data!")

# Show DataFrame dengan opsi untuk menampilkan semua kolom atau beberapa saja
st.subheader("📋 Data Tabel")
if st.checkbox("Tampilkan Semua Kolom"):
    st.dataframe(df)
else:
    st.dataframe(df.head())

# Statistik Data
st.subheader("📈 Statistik Data")
st.write(df.describe())

# Visualisasi Data dengan berbagai opsi
st.subheader("📊 Visualisasi Data")
chart_type = st.selectbox("Pilih Jenis Grafik", ["Histogram", "Boxplot", "Scatter Plot"])

if selected_col:
    fig, ax = plt.subplots()
    if chart_type == "Histogram":
        sns.histplot(df[selected_col], bins=20, kde=True, ax=ax)
    elif chart_type == "Boxplot":
        sns.boxplot(x=df[selected_col], ax=ax)
    elif chart_type == "Scatter Plot":
        x_col = st.sidebar.selectbox("Pilih Kolom X", columns)
        y_col = st.sidebar.selectbox("Pilih Kolom Y", columns)
        sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
    st.pyplot(fig)
else:
    st.warning("Pilih kolom numerik untuk visualisasi!")

# Analisis tambahan
st.subheader("📌 Insight Data")
st.write("Berikut beberapa wawasan yang dapat diperoleh dari data:")
st.markdown("- **Distribusi Data:** Histogram membantu memahami sebaran data.")
st.markdown("- **Outlier Detection:** Boxplot dapat menunjukkan outlier dalam data.")
st.markdown("- **Hubungan Antar Variabel:** Scatter plot membantu menemukan pola antara dua variabel.")

st.success("Gunakan dashboard ini untuk mengeksplorasi data lebih lanjut dan menemukan pola yang menarik! 🚀")

# Menjalankan dengan `streamlit run dashboard.py`
