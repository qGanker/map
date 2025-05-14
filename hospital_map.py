import streamlit as st
import pydeck as pdk
import pandas as pd
from PIL import Image
import base64
import time

st.set_page_config(layout="wide")

# Загрузка данных о больницах
data = pd.DataFrame([
    {
        "name": "Гомельская областная клиническая больница",
        "lat": 52.4412,
        "lon": 30.9870,
        "rkt": "Aquilion LB (16 срезов)",
        "mrt": "Ingenia Philips",
        "address": "ул. Мазурова, 1, Гомель",
        "phone": "+375 232 34-12-00",
        "available": "По направлению и платно",
        "image": "images/gomel_obl.png"
    },
    {
        "name": "Гомельский онкодиспансер",
        "lat": 52.4290,
        "lon": 30.9995,
        "rkt": "Aquilion Lightning (80 срезов)",
        "mrt": "—",
        "address": "ул. Головацкого, 128, Гомель",
        "phone": "+375 232 75-91-00",
        "available": "По направлению",
        "image": "images/gomel_onco.png"
    },
    {
        "name": "Гомельская городская клиническая больница №1",
        "lat": 52.4263,
        "lon": 30.9807,
        "rkt": "Revolution Evo (28 срезов)",
        "mrt": "Ingenia Philips",
        "address": "ул. Лазурная, 20, Гомель",
        "phone": "+375 232 33-65-00",
        "available": "По направлению и платно",
        "image": "images/gomel_gkb1.png"
    },
    {
        "name": "Мозырская городская больница",
        "lat": 52.0456,
        "lon": 29.2450,
        "rkt": "Bright Speed Elite (16 срезов)",
        "mrt": "ANKE SuperMarie",
        "address": "ул. Рыжкова, 78, Мозырь",
        "phone": "+375 236 32-31-00",
        "available": "По направлению",
        "image": "images/mozyr_gkb.png"
    }
])

st.title("🏥 Больницы Гомельской области")
st.markdown("Выберите учреждение на карте или из списка ниже")

search_query = st.text_input("🔎 Поиск по названию учреждения")

# Фильтрация данных
filtered_data = data[data["name"].str.contains(search_query, case=False)] if search_query else data

selected_hospital = st.selectbox("📋 Список учреждений:", filtered_data["name"].tolist())
hospital_info = filtered_data[filtered_data["name"] == selected_hospital].iloc[0]

# Центрировать карту при выборе учреждения
view_state = pdk.ViewState(
    latitude=hospital_info["lat"],
    longitude=hospital_info["lon"],
    zoom=12,
    pitch=0,
)

# Слои карты
layer_scatter = pdk.Layer(
    "ScatterplotLayer",
    data=filtered_data,
    get_position='[lon, lat]',
    get_radius=200,
    get_fill_color='[255, 0, 0, 160]',
    pickable=True
)
layer_text = pdk.Layer(
    "TextLayer",
    data=filtered_data,
    get_position='[lon, lat]',
    get_text='name',
    get_size=14,
    get_color='[0, 0, 0]',
    get_alignment_baseline="'bottom'"
)

with st.spinner("🔄 Загрузка карты..."):
    time.sleep(0.5)
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/dark-v10',
        initial_view_state=view_state,
        layers=[layer_scatter, layer_text],
        tooltip={
            "html": "<b>{name}</b><br/>РКТ: {rkt}<br/>МРТ: {mrt}",
            "style": {"backgroundColor": "white", "color": "black", "fontSize": "12px"}
        }
    ))

# Информация об учреждении
st.subheader(f"🏥 {hospital_info['name']}")
st.write(f"**📍 Адрес:** {hospital_info['address']}")
st.write(f"**📞 Телефон:** {hospital_info['phone']}")
st.write(f"**🧠 РКТ:** {hospital_info['rkt']}")
st.write(f"**🧲 МРТ:** {hospital_info['mrt']}")
st.write(f"**📌 Доступность:** {hospital_info['available']}")

# Фото учреждения
try:
    image = Image.open(hospital_info["image"])
    st.image(image, use_column_width=True)
except:
    st.warning("Фото учреждения не найдено")

# Кнопка открыть в Яндекс.Картах
yandex_url = f"https://yandex.by/maps/?ll={hospital_info['lon']}%2C{hospital_info['lat']}&z=16"
st.markdown(f"[📍 Открыть в Яндекс.Картах]({yandex_url})", unsafe_allow_html=True)
