import streamlit as st
import folium
from streamlit_folium import folium_static

#########################################
# LOGO VE SLOGAN:
#########################################

col1, col2, col3 = st.columns(3)
col2.image("LOGO.png", width=550, use_container_width=False) #tüm ekran için true yap
col2.markdown("<h4 style='text-align: center;'>Kahve İçmenin En Akıllı Hali...</h4>", unsafe_allow_html=True)
col2.markdown("<h3 style='text-align: center;'> </h3>", unsafe_allow_html=True)
col2.markdown("<h1 style='text-align: center;'> </h1>", unsafe_allow_html=True)
#########################################
#########################################
# AÇIKLAMA ÖNCESİ GÖRSEL:
#########################################

col1, col2 = st.columns([16, 22])
col2.image("KAHVE KALP.png", width=180, use_container_width=False) #tüm ekran için true yap

#########################################
# AÇIKLAMANIN BAŞLIĞI:
#########################################

col1, col2, col3 = st.columns([8, 8, 7])

col2.title(":green[ Karşı]:red[yaka] 'nın Kalbi !")

#########################################
# AÇIKLAMA KISMI:
#########################################
col1, col2, col3 = st.columns([1, 8, 1])

col2.markdown("<h4 style='text-align: center;'>İzmir Karşıyaka’da açmayı planladığımız Miuul Coffee Shop için "
              "en uygun lokasyonu belirlemek amacıyla 60’tan fazla yoğun noktayı analiz ettik. "
              "Okullar, hastaneler, AVM’ler, pazar yerleri ve spor alanları gibi"
              " yaya trafiğinin yoğun olduğu bölgeleri işaretledik.</h4>", unsafe_allow_html=True)

col2.markdown("<h3 style='text-align: center;'>K-Means modeli ile müşteri potansiyeli en yüksek"
              " 3 ideal konumu belirledik. Aşağıdaki haritada, bu noktalarla birlikte"
              " analiz ettiğimiz tüm bölgeleri inceleyebilirsiniz.</h3>", unsafe_allow_html=True)

col2.markdown("<h1 style='text-align: center;'> </h1>", unsafe_allow_html=True)
col2.markdown("<h1 style='text-align: center;'> </h1>", unsafe_allow_html=True)


#########################################
# HARİTA BAŞLIĞI;
#########################################

st.title("Optimal Lokasyon Seçenekleri:")

#########################################
# HARİTANIN EKLENMESİ;
#########################################

col1, col2 = st.columns([8, 2])

# HTML dosyasını iframe olarak yükle
html_file = "miuul coffee lokasyon.html"  # Daha önce kaydettiğin dosyanın adı

with col1:
    st.components.v1.html(open(html_file, "r", encoding="utf-8").read(), height=700, width=1200)

#########################################
# HARİTANIN YANINDAKİ YAZILAR;
#########################################

with col2:
    st.markdown("<h4 style='text-align: center; color: red;'>Yaklaşan Etkinlikler</h4>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>Rezervuar Kanişleri</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: green;'>24 Nisan / 20:00 - Aylak Sahne</h6>", unsafe_allow_html=True)
    st.markdown("<h9 style='text-align: center;'></h9>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>İlker Gümüşoluk</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: green;'>24 Nisan / 20:00 - Hikmet Şimşek Sanat Merkezi</h6>", unsafe_allow_html=True)
    st.markdown("<h9 style='text-align: center;'></h9>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>Aşk Listesi - Tiyatro</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: green;'>24 Nisan / 20:00 - Sahne Tozu</h6>", unsafe_allow_html=True)
    st.markdown("<h9 style='text-align: center;'></h9>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>Sabahat Akkiraz</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: green;'>24 Nisan / 20:30 - Suat Taşer</h6>", unsafe_allow_html=True)
    st.markdown("<h9 style='text-align: center;'></h9>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>Bir Tutam Çehov</h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: green;'>24 Nisan / 20:30 - Han Tiyatrosu</h6>", unsafe_allow_html=True)
    st.markdown("<h9 style='text-align: center;'></h9>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>Salih Tıraş </h4>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center; color: green;'>24 Nisan / 21:00 - Rene Lokal</h6>", unsafe_allow_html=True)
    st.markdown("<h9 style='text-align: center;'></h9>", unsafe_allow_html=True)

#########################################
