import streamlit as st
import pydeck as pdk
import pandas as pd

# Все больницы Гомельской области
data = pd.DataFrame([
    {
        "name": "Гомельская областная клиническая больница",
        "lat": 52.4345,
        "lon": 30.9754,
        "rkt": "Aquilion LB (16 срезов)",
        "mrt": "Ingenia Philips"
    },
    {
        "name": "Гомельский онкодиспансер",
        "lat": 52.4219,
        "lon": 31.0086,
        "rkt": "Aquilion Lightning (80 срезов)",
        "mrt": "—"
    },
    {
        "name": "Гомельская городская клиническая больница №1",
        "lat": 52.4417,
        "lon": 30.9878,
        "rkt": "Revolution Evo (28 срезов)",
        "mrt": "Ingenia Philips"
    },
    {
        "name": "Мозырская городская больница",
        "lat": 52.0494,
        "lon": 29.2637,
        "rkt": "Bright Speed Elite (16 срезов)",
        "mrt": "ANKE SuperMarie"
    },
    {
        "name": "Мозырская ЦРБ",
        "lat": 52.0467,
        "lon": 29.2572,
        "rkt": "Somatom go.Up",
        "mrt": "MagFinder WA 13200"
    },
    {
        "name": "Жлобинская ЦРБ",
        "lat": 52.8925,
        "lon": 30.0244,
        "rkt": "Somatom Emotion / go.Up",
        "mrt": "—"
    },
    {
        "name": "Светлогорская ЦРБ",
        "lat": 52.6333,
        "lon": 29.7333,
        "rkt": "Toshiba Aquilion",
        "mrt": "—"
    },
    {
        "name": "Речицкая ЦРБ",
        "lat": 52.3617,
        "lon": 30.3853,
        "rkt": "Ventum (64 среза)",
        "mrt": "—"
    },
    {
        "name": "Петриковская ЦРБ",
        "lat": 52.1281,
        "lon": 28.4917,
        "rkt": "Ventum",
        "mrt": "—"
    },
    {
        "name": "Хойникская ЦРБ",
        "lat": 51.8861,
        "lon": 29.6272,
        "rkt": "Ventum",
        "mrt": "—"
    },
    {
        "name": "Чечерская ЦРБ",
        "lat": 52.9167,
        "lon": 30.9000,
        "rkt": "Ventum",
        "mrt": "—"
    },
])

# Заголовок
st.title("🏥 Больницы Гомельской области")
search_query = st.text_input("🔎 Поиск по названию больницы")

# Фильтрация по запросу
if search_query:
    filtered_data = data[data["name"].str.contains(search_query, case=False)]
else:
    filtered_data = data

# Карта с маркерами и названиями
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
            get_radius=8000,
            get_fill_color=[0, 128, 255, 160],
            pickable=True
        ),
        pdk.Layer(
            "TextLayer",
            data=filtered_data,
            get_position='[lon, lat]',
            get_text='name',
            get_size=16,
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
