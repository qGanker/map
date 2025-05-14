import streamlit as st
import folium
from streamlit_folium import folium_static

# Настройки страницы
st.set_page_config(page_title="Карта учреждений Гомельской области", layout="wide")
st.title("Учреждения здравоохранения Гомельской области")

# Центр карты (Гомельская область)
center = [52.426, 30.993]
zoom = 8

# Создание карты с кастомным tiles (без флагов)
m = folium.Map(location=center, zoom_start=zoom,
               tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
               attr='&copy; <a href="https://carto.com/attributions">CARTO</a>')

# Данные по больницам (11 учреждений)
hospitals = [
    {
        "name": "Гомельская областная клиническая больница",
        "coords": [52.4453, 30.9878],
        "ct": "Aquilion LB (16 срезов)",
        "mri": "Ingenia Philips"
    },
    {
        "name": "Гомельский онкодиспансер",
        "coords": [52.4442, 30.9568],
        "ct": "Aquilion Lightning (80 срезов)",
        "mri": "—"
    },
    {
        "name": "Гомельская городская клиническая больница №1",
        "coords": [52.4306, 30.9822],
        "ct": "Revolution Evo (28 срезов)",
        "mri": "Ingenia Philips"
    },
    {
        "name": "Мозырская городская больница",
        "coords": [52.0459, 29.2766],
        "ct": "Bright Speed Elite (16 срезов)",
        "mri": "ANKE SuperMarie"
    },
    {
        "name": "Мозырская ЦРБ",
        "coords": [52.0335, 29.2807],
        "ct": "Somatom go.Up",
        "mri": "MagFinder WA 13200"
    },
    {
        "name": "Жлобинская ЦРБ",
        "coords": [52.8924, 30.0336],
        "ct": "Somatom Emotion / go.Up",
        "mri": "—"
    },
    {
        "name": "Светлогорская ЦРБ",
        "coords": [52.6328, 29.7384],
        "ct": "Toshiba Aquilion",
        "mri": "—"
    },
    {
        "name": "Речицкая ЦРБ",
        "coords": [52.3691, 30.3869],
        "ct": "Ventum (64 среза)",
        "mri": "—"
    },
    {
        "name": "Петриковская ЦРБ",
        "coords": [52.1286, 28.4941],
        "ct": "Ventum",
        "mri": "—"
    },
    {
        "name": "Хойникская ЦРБ",
        "coords": [51.8801, 30.2577],
        "ct": "Ventum",
        "mri": "—"
    },
    {
        "name": "Чечерская ЦРБ",
        "coords": [52.9136, 31.3841],
        "ct": "Ventum",
        "mri": "—"
    },
]

# Добавление маркеров на карту
for hospital in hospitals:
    popup_html = f"""
    <b>{hospital['name']}</b><br>
    <b>КТ:</b> {hospital['ct']}<br>
    <b>МРТ:</b> {hospital['mri']}
    """
    folium.Marker(
        location=hospital["coords"],
        popup=folium.Popup(popup_html, max_width=300),
        icon=folium.Icon(color="blue", icon="plus-sign", prefix="fa")
    ).add_to(m)

# Отображение карты
folium_static(m)

st.markdown("""
<style>
    .folium-map {
        height: 90vh;
    }
</style>
""", unsafe_allow_html=True)
