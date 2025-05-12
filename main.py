import streamlit as st



home_page = st.Page(page="pages/HomePage.py", title="Ana Sayfa")
lokasyon = st.Page(page="pages/Lokasyon.py", title="Lokasyon")
siparis = st.Page(page="pages/Siparis.py", title="Sipariş Ekranı")
kar_hesapla = st.Page(page="pages/Kar_Hesapla.py", title="Günlük Kâr Hesapla")
Model_degerlendirmesi = st.Page(page="pages/Model_degerlendirmesi.py", title="Teknik Bilgiler")
Nan_Stop = st.Page(page="pages/Nan_Stop.py", title="NaN Stop")

pg = st.navigation([home_page, lokasyon,  kar_hesapla, siparis, Model_degerlendirmesi, Nan_Stop])

pg.run()

