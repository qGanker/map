import streamlit as st
import pydeck as pdk
import pandas as pd

# Пример данных: замените или расширьте
data = pd.DataFrame([
    {
        "name": "Гомельская областная больница",
        "lat": 52.4412,
        "lon": 30.9870,
        "rkt": "Siemens Somatom, 64 среза",
        "mrt": "Philips Achieva 1.5T"
    },
    {
        "name": "Мозырская городская больница",
        "lat": 52.0500,
        "lon": 29.2700,
        "rkt": "GE BrightSpeed, 16 срезов",
        "mrt": "Нет"
    },
    {
        "name": "Речицкая ЦРБ",
        "lat": 52.3693,
        "lon": 30.3945,
        "rkt": "Toshiba Aquilion, 32 среза",
        "mrt": "Siemens Avanto 1.5T"
    }
])

# Заголовок
st.title("Больницы Гомельской области")
search_query = st.text_input("Поиск по названию больницы")

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
            get_radius=8000,
            get_fill_color=[255, 0, 0, 160],
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
        "html": "<b>{name}</b><br/>РКТ: {rkt}<br/>МРТ: {mrt}",
        "style": {
            "backgroundColor": "white",
            "color": "black",
            "fontSize": "12px"
        }
    }
))
