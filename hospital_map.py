import streamlit as st
import folium
from streamlit_folium import st_folium

# Создаём карту с другим tile-провайдером, например от CartoDB (чистый и без политики)
m = folium.Map(
    location=[52.441176, 30.993005], 
    zoom_start=8,
    tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
    attr='&copy; <a href="https://carto.com/">CARTO</a>'
)

# Пример точки
folium.Marker(
    location=[52.426739, 31.01412],
    popup="Гомельская областная больница<br>МРТ: Siemens Aera (48 срезов)",
    tooltip="Гомельская обл. больница"
).add_to(m)

# Показываем карту
st_data = st_folium(m, width=800, height=600)
