import streamlit as st

col1, col2, col3 = st.columns([1,3,1])
col2.markdown("<h6 style='text-align: center;'> </h6>", unsafe_allow_html=True)
col2.image("img.png", width=400, use_container_width=True) #tüm ekran için true yap


col1, col2, col3,col4, col5 = st.columns([3,1,3,1,3])
col2.markdown("<h6 style='text-align: center;'> </h6>", unsafe_allow_html=True)
col1.image("Vahit Keskin ve Nan Stop.jpg", width=400, use_container_width=True) #tüm ekran için true yap

video_file = open('Vahit el sallıyor.mp4', 'rb')
video_bytes = video_file.read()

col3.video(video_bytes)

col5.image("Vahit NanStop.jpg", width=400, use_container_width=True) #tüm ekran için true yap


