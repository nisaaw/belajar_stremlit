import streamlit as st
import pandas as pd

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("kos_data.csv")

data = load_data()

# Sidebar filter
st.sidebar.header("Filter Pencarian")
lokasi = st.sidebar.multiselect("Pilih Lokasi", options=data['lokasi'].unique(), default=data['lokasi'].unique())
harga_max = st.sidebar.slider("Harga Maksimal (Rp)", min_value=500000, max_value=2000000, value=1500000, step=50000)

# Filter data
filtered_data = data[(data['lokasi'].isin(lokasi)) & (data['harga'] <= harga_max)]

# Tampilan utama
st.title("🏠 Info Kos-Kosan")
st.write("Temukan kos sesuai kebutuhanmu!")

st.dataframe(filtered_data)

# Tambah data baru
st.subheader("➕ Tambah Kos Baru")
with st.form("form_kos"):
    nama = st.text_input("Nama Kos")
    lokasi_baru = st.text_input("Lokasi")
    harga = st.number_input("Harga (Rp)", min_value=0)
    fasilitas = st.text_input("Fasilitas (pisahkan dengan ';')")
    submit = st.form_submit_button("Tambah Kos")

    if submit:
        new_data = pd.DataFrame({
            'nama': [nama],
            'lokasi': [lokasi_baru],
            'harga': [harga],
            'fasilitas': [fasilitas]
        })
        new_data.to_csv("kos_data.csv", mode='a', header=False, index=False)
        st.success("Data kos baru berhasil ditambahkan! Silakan refresh halaman.")

