import streamlit as st
import pydeck as pdk
import pandas as pd

# Актуальные данные по учреждениям
data = pd.DataFrame([
    {
        "name": "Гомельская областная клиническая больница",
        "lat": 52.4228,
        "lon": 30.9784,
        "rkt": "Aquilion LB (16 срезов)",
        "mrt": "Ingenia Philips"
    },
    {
        "name": "Гомельский онкодиспансер",
        "lat": 52.4204,
        "lon": 31.0072,
        "rkt": "Aquilion Lightning (80 срезов)",
        "mrt": "—"
    },
    {
        "name": "Гомельская городская клиническая больница №1",
        "lat": 52.4416,
        "lon": 30.9942,
        "rkt": "Revolution Evo (28 срезов)",
        "mrt": "Ingenia Philips"
    },
    {
        "name": "Мозырская городская больница",
        "lat": 52.0424,
        "lon": 29.2725,
        "rkt": "Bright Speed Elite (16 срезов)",
        "mrt": "ANKE SuperMarie"
    },
    {
        "name": "Мозырская ЦРБ",
        "lat": 52.0506,
        "lon": 29.2596,
        "rkt": "Somatom go.Up",
        "mrt": "MagFinder WA 13200"
    },
    {
        "name": "Жлобинская ЦРБ",
        "lat": 52.8923,
        "lon": 30.0262,
        "rkt": "Somatom Emotion / go.Up",
        "mrt": "—"
    },
    {
        "name": "Светлогорская ЦРБ",
        "lat": 52.6281,
        "lon": 29.7396,
        "rkt": "Toshiba Aquilion",
        "mrt": "—"
    },
    {
        "name": "Речицкая ЦРБ",
        "lat": 52.3690,
        "lon": 30.3896,
        "rkt": "Ventum (64 среза)",
        "mrt": "—"
    },
    {
        "name": "Петриковская ЦРБ",
        "lat": 52.1282,
        "lon": 28.4868,
        "rkt": "Ventum",
        "mrt": "—"
    },
    {
        "name": "Хойникская ЦРБ",
        "lat": 51.8802,
        "lon": 29.6257,
        "rkt": "Ventum",
        "mrt": "—"
    },
    {
        "name": "Чечерская ЦРБ",
        "lat": 52.9145,
        "lon": 30.9040,
        "rkt": "Ventum",
        "mrt": "—"
    },
])

# Заголовок
st.title("🏥 Больницы Гомельской области")
search_query = st.text_input("🔎 Поиск по названию больницы")

# Фильтрация
if search_query:
    filtered_data = data[data["name"].str.contains(search_query, case=False)]
else:
    filtered_data = data

# Карта с маркерами
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=52.4,
        longitude=30.9,
        zoom=7,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=filtered_data,
            get_position='[lon, lat]',
            get_radius=4000,
            get_fill_color=[255, 0, 0, 160],
            pickable=True
        ),
        pdk.Layer(
            "TextLayer",
            data=filtered_data,
            get_position='[lon, lat]',
            get_text='name',
            get_size=14,
            get_color=[0, 0, 0],
            get_alignment_baseline="'bottom'"
        )
    ],
    tooltip={
        "html": "<b>{name}</b><br/>🖥 РКТ: {rkt}<br/>🧲 МРТ: {mrt}",
        "style": {
            "backgroundColor": "white",
            "color": "black",
            "fontSize": "12px"
        }
    }
))

# Список больниц снизу
st.subheader("📋 Список учреждений")
st.dataframe(data[["name", "rkt", "mrt"]].rename(columns={
    "name": "Учреждение",
    "rkt": "РКТ",
    "mrt": "МРТ"
}), use_container_width=True)
