import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# Данные по учреждениям
data = [
    {
        "Учреждение": "Гомельская областная клиническая больница",
        "lat": 52.4345, "lon": 30.9754,
        "РКТ": "Aquilion LB", "Срезов": "16", "МРТ": "Ingenia Philips"
    },
    {
        "Учреждение": "Гомельский онкодиспансер",
        "lat": 52.4219, "lon": 31.0086,
        "РКТ": "Aquilion Lightning", "Срезов": "80", "МРТ": "—"
    },
    {
        "Учреждение": "Гомельская городская клиническая больница №1",
        "lat": 52.4417, "lon": 30.9878,
        "РКТ": "Revolution Evo", "Срезов": "28", "МРТ": "Ingenia Philips"
    },
    {
        "Учреждение": "Мозырская городская больница",
        "lat": 52.0494, "lon": 29.2637,
        "РКТ": "Bright Speed Elite", "Срезов": "16", "МРТ": "ANKE SuperMarie"
    },
    {
        "Учреждение": "Мозырская ЦРБ",
        "lat": 52.0467, "lon": 29.2572,
        "РКТ": "Somatom go.Up", "Срезов": "—", "МРТ": "MagFinder WA 13200"
    },
    {
        "Учреждение": "Жлобинская ЦРБ",
        "lat": 52.8925, "lon": 30.0244,
        "РКТ": "Somatom Emotion / go.Up", "Срезов": "—", "МРТ": "—"
    },
    {
        "Учреждение": "Светлогорская ЦРБ",
        "lat": 52.6333, "lon": 29.7333,
        "РКТ": "Toshiba Aquilion", "Срезов": "—", "МРТ": "—"
    },
    {
        "Учреждение": "Речицкая ЦРБ",
        "lat": 52.3617, "lon": 30.3853,
        "РКТ": "Ventum", "Срезов": "64", "МРТ": "—"
    },
    {
        "Учреждение": "Петриковская ЦРБ",
        "lat": 52.1281, "lon": 28.4917,
        "РКТ": "Ventum", "Срезов": "—", "МРТ": "—"
    },
    {
        "Учреждение": "Хойникская ЦРБ",
        "lat": 51.8861, "lon": 29.6272,
        "РКТ": "Ventum", "Срезов": "—", "МРТ": "—"
    },
    {
        "Учреждение": "Чечерская ЦРБ",
        "lat": 52.9167, "lon": 30.9,
        "РКТ": "Ventum", "Срезов": "—", "МРТ": "—"
    },
]

# Интерфейс
st.set_page_config(page_title="Учреждения здравоохранения Гомельской области", layout="wide")
st.title("🩺 Учреждения здравоохранения Гомельской области")
search = st.text_input("🔎 Поиск по названию учреждения")

# Карта
m = folium.Map(location=[52.4, 30.9], zoom_start=8, tiles="Stamen Terrain")

for entry in data:
    if search.lower() in entry["Учреждение"].lower():
        folium.Marker(
            location=[entry["lat"], entry["lon"]],
            popup=f"""
                <b>{entry["Учреждение"]}</b><br>
                <b>РКТ:</b> {entry["РКТ"]}<br>
                <b>Срезов:</b> {entry["Срезов"]}<br>
                <b>МРТ:</b> {entry["МРТ"]}
            """,
            icon=folium.Icon(color="blue", icon="plus-sign"),
        ).add_to(m)

# Отображение карты
st_data = st_folium(m, width=1300, height=700)
