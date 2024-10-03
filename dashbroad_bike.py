import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# Load dataset
sepeda_day = pd.read_csv("https://github.com/AdamNoorF/streamlit-bike/blob/main/day_sepeda_harian.csv")

st.title('Bike Sharing Analysis Data-EDA')

st.write('### Data Penyewaan Sepeda per hari dari tahun 2011 - 2012')
st.dataframe(sepeda_day.head())

#==================================================================================================>
st.title('Perbandingan Total Penyewaan Sepeda Berdasarkan Musim dan Kondisi Cuaca')

#Membuat catplot
def create_catplot(sepeda_day):
    # Menggunakan catplot dengan seaborn
    catplot_fig = sns.catplot(x="season", y="cnt", hue="weathersit", kind="bar", data=sepeda_day,  height=6, aspect=1.5)
    plt.title("Perbandingan Total Penyewaan Sepeda Berdasarkan Musim dan Kondisi Cuaca")
    plt.xlabel("Musim", fontsize=14)
    plt.ylabel("Total Penyewaan Sepeda", fontsize=14)
    return catplot_fig

# Layout dua kolom: bar plot di kolom kiri, kesimpulan di kolom kanan
col1, col2 = st.columns(2)

# Kolom untuk Catplot
with col1:
    catplot_fig = create_catplot(sepeda_day)
    st.pyplot(catplot_fig)

# Kolom untuk Kesimpulan
with col2:
    st.write("""
    Plot diperoleh kesimpulan bahwa: 
             
        - Musim panas dan cuaca sedikit berawan adalah kondisi terbaik dengan mencapai lebih dari 5000 penyewa sepeda
        - Musim dingin dan cuaca badai hujan/salju adalah kondisi terburuk dengan hanya mencapai tidak lebih dari 1000 penyewa sepeda
    """)


#=================================================================================>

# Menampilkan judul
st.title('Hubungan antar Variabel Kontinu dengan Total Penyewaan Sepeda')

# Membuat tabs
tab1, tab2, tab3, tab4 = st.tabs(["cnt vs temp", "cnt vs atemp", "cnt vs humadity", "cnt vs windspeed"])

# Fungsi untuk membuat scatter plot
def create_scatter(x, y, xlabel, title):
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel) 
    ax.set_ylabel('cnt')
    return fig

# Scatter plot pada Tab 1: cnt vs temp
with tab1:
    st.header("cnt vs temp")
    fig1 = create_scatter(sepeda_day['temp'], sepeda_day['cnt'],"temp", "cnt vs temp")
    st.pyplot(fig1)
    st.write(
        """Pola penyebaran dari *temp* pada *cnt* menaik ke arah positif hal ini dapat berkontribusi dengan banyaknya penyewaan sepeda. Jadi besarnya variabel temp dapat menaikkan angka penyewaan sepeda
        """
    )
# Scatter plot pada Tab 2: cnt vs atemp
with tab2:
    st.header("cnt vs atemp")
    fig2 = create_scatter(sepeda_day['atemp'], sepeda_day['cnt'],"atemp", "cnt vs atemp")
    st.pyplot(fig2)
    st.write(
        """Pola penyebaran dari *atemp* pada *cnt* menaik ke arah positif hal ini dapat berkontribusi dengan banyaknya penyewaan sepeda. Jadi besarnya variabel atemp dapat menaikkan angka penyewaan sepeda
        """
    )
# Scatter plot pada Tab 3: cnt vs hum
with tab3:
    st.header("cnt vs hum")
    fig3 = create_scatter(sepeda_day['hum'], sepeda_day['cnt'],"hum", "cnt vs hum")
    st.pyplot(fig3)
    st.write(
        """Pola penyebaran dari variabel *hum* pada *cnt* menaik ke arah negatif hal ini tidak dapat berkontribusi dengan banyaknya penyewaan sepeda. Akan tetapi bertolak belakang dari banyaknya penyewaan sepeda.
        Jadi besarnya variabel kelembapan akan mempekecil dari penyewaan sepeda
        """
    )

# Scatter plot pada Tab 4: cnt vs windspeed
with tab4:
    st.header("cnt vs windspeed")
    fig4 = create_scatter(sepeda_day['windspeed'], sepeda_day['cnt'], "windspeed", "cnt vs windspeed")
    st.pyplot(fig4)
    st.write(
        """Pola penyebaran dari *hum* pada *windspeed* menaik ke arah negatif hal ini tidak dapat berkontribusi dengan banyaknya penyewaan sepeda. Akan tetapi bertolak belakang dari banyaknya penyewaan sepeda.
        Jadi besarnya variabel windspeed akan mempekecil dari penyewaan sepeda
        """
    )


#=================================================================================>

# Menampilkan judul
st.title('Hubungan antar Variabel Kontinu')

# Membuat tabs
tab1, tab2 = st.tabs(["cnt vs temp", "cnt vs atemp"])

# Fungsi untuk membuat scatter plot
def create_scatter(x, y, xlabel, ylabel, title):
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_title(title)
    ax.set_xlabel(xlabel) 
    ax.set_ylabel(ylabel)
    return fig

# Scatter plot pada Tab 1: cnt vs temp
with tab1:
    st.header("temp vs atemp")
    fig1 = create_scatter(sepeda_day['temp'], sepeda_day['atemp'],"temp", "atemp", "temp vs atemp")
    st.pyplot(fig1)
    st.write(
        """Pola penyebaran dari *temp* dengan *atemp* membuat sebuah garis positif, hubungan mereka sangat kuat
        """
    )
# Scatter plot pada Tab 2: cnt vs atemp
with tab2:
    st.header("hum vs windspeed")
    fig2 = create_scatter(sepeda_day['hum'], sepeda_day['windspeed'],"hum", "windspeed" ,"hum vs windspeed")
    st.pyplot(fig2)
    st.write(
        """Pola penyebaran dari *hum* dengan *windspeed* tidak terlalu baik, dapat dilihat dari pola penyebaran data hanya berkumpul di satu tempat. 
        """
    )


#=================================================================================>


# Menampilkan judul
st.title('Visualisasi Heatmap Korelasi Antar Variabel Sepeda Harian')

# Pilih subset kolom yang diinginkan
indatas = ["temp", "atemp", "hum", "windspeed", "cnt"]

# Menghitung matriks korelasi
korelasi = sepeda_day[indatas].corr()

# Membuat heatmap
st.write("Berikut ini adalah heatmap yang menunjukkan korelasi antara berbagai variabel terkait penyewaan sepeda:")

# Cek apakah korelasi berhasil dihitung
if korelasi.empty:
    st.write("Data korelasi tidak tersedia. Periksa input data Anda.")
else:
    # Membuat heatmap
    fig, ax = plt.subplots(figsize=(8, 6))  # Mengatur ukuran figure
    sns.heatmap(korelasi, annot=True, cmap='coolwarm', vmin=0, vmax=1, linewidths=0.5, ax=ax)
    ax.set_title("Heatmap Korelasi Antar Variabel Sepeda Harian", fontsize=16)
    ax.set_xlabel("Variabel", fontsize=14)
    ax.set_ylabel("Variabel", fontsize=14)

    # Menampilkan heatmap di Streamlit
    st.pyplot(fig)

    # Menambahkan expander di bawah heatmap dengan kesimpulan
    with st.expander("Kesimpulan"):
        st.write("""
        Dari heatmap di atas, dapat diambil beberapa kesimpulan:

        - Variabel *temp* dan *atemp* memiliki korelasi yang sangat kuat, mendekati nilai 1, menunjukkan bahwa keduanya hampir identik dalam konteks data ini.
        - Korelasi antara *cnt* (jumlah penyewaan) dan *temp* cukup kuat, menunjukkan bahwa peningkatan suhu cenderung dikaitkan dengan lebih banyak penyewaan sepeda.
        - Variabel *windspeed* menunjukkan korelasi yang rendah dengan variabel lain, terutama *cnt*, yang mengindikasikan bahwa kecepatan angin mungkin tidak terlalu mempengaruhi jumlah penyewaan sepeda.
        - Variabel *hum* (kelembaban) memiliki korelasi sedang terhadap jumlah penyewaan sepeda, menunjukkan bahwa kondisi kelembaban bisa sedikit mempengaruhi keputusan pengguna untuk menyewa sepeda.

        Secara keseluruhan, suhu (*temp* dan *atemp*) merupakan indikator yang berkontribusi baik terhadap jumlah penyewaan sepeda dalam dataset ini.
        """)

#=================================================================================>


# Menampilkan judul
st.title('Conclusion')
st.write("""
        Dari visualisasi data tersebut dipeoleh beberapa kesimpulan:
         
        - Musim panas merupakan musim panas merupakan musim terbaik untuk penyewaan sepeda dikarenakan cuaca pada musim panas tidak berawan sehingga dapat menikmat sepeda dengan minimnya gangguan eksternal cuaca. Akan tetapi, pada musim dingin merupakan musim yang buruk baik penyewaan sepeda dikarenakan cuaca yang kurang baik maupun cuaca tersebut meliputi tidak berawan, berkabut, dan badai salju/hujan.
        - Variabel yang berkontribusi berdampak pada banyaknya penyewaan sepeda adalah *atemp*. Jadi faktor ekstrnal dari musim, cuaca, dan suhu sangat berpengaruh pada banyaknya jumlah penyewa sepeda pada tahun 2011-2012
        """)
st.caption('created by : Adam Noor Falah')



