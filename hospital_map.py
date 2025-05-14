import streamlit as st
import folium
from folium.plugins import Search
from streamlit_folium import st_folium

st.set_page_config(page_title="Больницы Гомельской области", layout="wide")

# Данные по больницам
hospitals = [
    {
        "name": "Гомельская областная клиническая больница",
        "lat": 52.4285, "lon": 30.9939,
        "ct_model": "Aquilion LB", "slices": "16",
        "mri_model": "Ingenia Philips"
    },
    {
        "name": "Гомельский онкодиспансер",
        "lat": 52.4206, "lon": 30.9990,
        "ct_model": "Aquilion Lightning", "slices": "80",
        "mri_model": "—"
    },
    {
        "name": "Гомельская городская клиническая больница №1",
        "lat": 52.4397, "lon": 30.9870,
        "ct_model": "Revolution Evo", "slices": "28",
        "mri_model": "Ingenia Philips"
    },
    {
        "name": "Мозырская городская больница",
        "lat": 52.0493, "lon": 29.2667,
        "ct_model": "Bright Speed Elite", "slices": "16",
        "mri_model": "ANKE SuperMarie"
    },
    {
        "name": "Мозырская ЦРБ",
        "lat": 52.0386, "lon": 29.3091,
        "ct_model": "Somatom go.Up", "slices": "—",
        "mri_model": "MagFinder WA 13200"
    },
    {
        "name": "Жлобинская ЦРБ",
        "lat": 52.8912, "lon": 30.0333,
        "ct_model": "Somatom Emotion / go.Up", "slices": "—",
        "mri_model": "—"
    },
    {
        "name": "Светлогорская ЦРБ",
        "lat": 52.6326, "lon": 29.7400,
        "ct_model": "Toshiba Aquilion", "slices": "—",
        "mri_model": "—"
    },
    {
        "name": "Речицкая ЦРБ",
        "lat": 52.3632, "lon": 30.3921,
        "ct_model": "Ventum", "slices": "64",
        "mri_model": "—"
    },
    {
        "name": "Петриковская ЦРБ",
        "lat": 52.1305, "lon": 28.4930,
        "ct_model": "Ventum", "slices": "—",
        "mri_model": "—"
    },
    {
        "name": "Хойникская ЦРБ",
        "lat": 51.8872, "lon": 30.2581,
        "ct_model": "Ventum", "slices": "—",
        "mri_model": "—"
    },
    {
        "name": "Чечерская ЦРБ",
        "lat": 52.8916, "lon": 30.9151,
        "ct_model": "Ventum", "slices": "—",
        "mri_model": "—"
    },
]

# Поиск
query = st.text_input("🔍 Поиск по учреждению", "")

# Инициализация карты
m = folium.Map(location=[52.4, 30.9], zoom_start=8, tiles="CartoDB positron")

# Добавление маркеров
for hospital in hospitals:
    if query.lower() in hospital["name"].lower():
        folium.Marker(
            location=[hospital["lat"], hospital["lon"]],
            tooltip=hospital["name"],
            popup=folium.Popup(
                f"<b>{hospital['name']}</b><br>"
                f"📌 <b>РКТ:</b> {hospital['ct_model']}<br>"
                f"🧩 <b>Срезов:</b> {hospital['slices']}<br>"
                f"🧲 <b>МРТ:</b> {hospital['mri_model']}",
                max_width=300
            ),
            icon=folium.Icon(color="blue", icon="plus-sign", prefix='fa')
        ).add_to(m)

# Отображение карты
st_folium(m, width=1000, height=700)
