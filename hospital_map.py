import streamlit as st
import folium
from streamlit_folium import st_folium

# Список больниц (пример)
hospitals = [
    {
        "name": "Гомельская областная больница",
        "lat": 52.426739,
        "lon": 31.014120,
        "info": "МРТ: Siemens Aera (48 срезов)<br>РКТ: Toshiba Aquilion (64 среза)"
    },
    {
        "name": "Мозырская центральная больница",
        "lat": 52.042365,
        "lon": 29.245457,
        "info": "МРТ: Philips Ingenia (32 среза)<br>РКТ: GE BrightSpeed (16 срезов)"
    }
]

st.set_page_config(layout="wide")
st.title("Карта больниц Гомельской области")

# Создаём карту с нейтральным источником tiles
m = folium.Map(
    location=[52.441176, 30.993005],
    zoom_start=8,
    tiles="https://{{s}}.basemaps.cartocdn.com/light_all/{{z}}/{{x}}/{{y}}{{r}}.png",
    attr='&copy; <a href="https://carto.com/">CARTO</a>'
)

# Фильтр по поиску
query = st.text_input("Поиск больницы по названию")
filtered = [h for h in hospitals if query.lower() in h["name"].lower()] if query else hospitals

# Добавляем маркеры
for h in filtered:
    folium.Marker(
        location=[h["lat"], h["lon"]],
        popup=f"<b>{h['name']}</b><br>{h['info']}",
        tooltip=h["name"]
    ).add_to(m)

st_data = st_folium(m, width=900, height=600)
