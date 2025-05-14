import streamlit as st
import pydeck as pdk
import pandas as pd
from urllib.parse import quote

st.set_page_config(layout="wide")

hospitals = [
    {
        "name": "Гомельская областная клиническая больница",
        "lat": 52.441174, "lon": 30.987666,
        "rkt": "Aquilion LB, 16 срезов", "mrt": "Ingenia Philips",
        "address": "ул. Барыкина, 161", "phone": "+375 232 60-66-00",
        "access": "По направлению и платно", "photo": "https://medgomel.by/images/banners/main.jpg"
    },
    {
        "name": "Гомельский онкодиспансер",
        "lat": 52.449230, "lon": 30.997379,
        "rkt": "Aquilion Lightning, 80 срезов", "mrt": "—",
        "address": "ул. Ирининская, 16", "phone": "+375 232 60-66-90",
        "access": "По направлению", "photo": "https://oncogomel.by/wp-content/uploads/2023/02/IMG_1443-scaled.jpg"
    },
    {
        "name": "Гомельская городская клиническая больница №1",
        "lat": 52.429838, "lon": 30.993835,
        "rkt": "Revolution Evo, 28 срезов", "mrt": "Ingenia Philips",
        "address": "ул. Бородина, 2", "phone": "+375 232 50-62-00",
        "access": "По направлению", "photo": "https://1gkb.by/upload/iblock/64b/64b07aeb9c38e27a2b64570fa0115b18.jpg"
    },
    {
        "name": "Мозырская городская больница",
        "lat": 52.045620, "lon": 29.272020,
        "rkt": "Bright Speed Elite, 16 срезов", "mrt": "ANKE SuperMarie",
        "address": "ул. Притыцкого, 3", "phone": "+375 236 33-38-80",
        "access": "По направлению", "photo": "https://www.mozyrcrb.by/files/2021/07/gorb.jpg"
    },
    {
        "name": "Мозырская ЦРБ",
        "lat": 52.040900, "lon": 29.270000,
        "rkt": "Somatom go.Up", "mrt": "MagFinder WA 13200",
        "address": "ул. Ленинская, 52", "phone": "+375 236 32-29-00",
        "access": "По направлению", "photo": "https://www.mozyrcrb.by/files/2021/07/crb.jpg"
    },
    {
        "name": "Жлобинская ЦРБ",
        "lat": 52.892234, "lon": 30.024417,
        "rkt": "Somatom Emotion / go.Up", "mrt": "—",
        "address": "ул. Первомайская, 62", "phone": "+375 2334 3-11-44",
        "access": "По направлению", "photo": "https://zhlobincrb.by/upload/images/img_1.jpg"
    },
    {
        "name": "Светлогорская ЦРБ",
        "lat": 52.629496, "lon": 29.746804,
        "rkt": "Toshiba Aquilion", "mrt": "—",
        "address": "ул. Калинина, 12", "phone": "+375 2342 5-00-60",
        "access": "По направлению", "photo": "https://svetcrb.by/images/crb.jpg"
    },
    {
        "name": "Речицкая ЦРБ",
        "lat": 52.369254, "lon": 30.385557,
        "rkt": "Ventum, 64 среза", "mrt": "—",
        "address": "ул. Советская, 31", "phone": "+375 2340 5-55-55",
        "access": "По направлению", "photo": "https://rechcrb.by/images/crb.jpg"
    },
    {
        "name": "Петриковская ЦРБ",
        "lat": 52.132224, "lon": 28.495021,
        "rkt": "Ventum", "mrt": "—",
        "address": "ул. Коммунистическая, 99", "phone": "+375 2350 5-11-60",
        "access": "По направлению", "photo": "https://petrikovcrb.by/images/crb.jpg"
    },
    {
        "name": "Хойникская ЦРБ",
        "lat": 51.901414, "lon": 30.250221,
        "rkt": "Ventum", "mrt": "—",
        "address": "ул. 50 лет Октября, 2", "phone": "+375 2336 4-12-25",
        "access": "По направлению", "photo": "https://hoiniki.by/uploads/images/2022/10/30/pol-3.jpg"
    },
    {
        "name": "Чечерская ЦРБ",
        "lat": 52.883016, "lon": 30.915114,
        "rkt": "Ventum", "mrt": "—",
        "address": "ул. Советская, 78", "phone": "+375 2332 2-12-35",
        "access": "По направлению", "photo": "https://crbchechersk.by/images/galereya/1.jpg"
    }
]

st.title("Больницы Гомельской области")

search_query = st.text_input("Поиск по названию больницы")
selected_hospital = st.selectbox("Или выберите учреждение", [h["name"] for h in hospitals])

filtered_data = pd.DataFrame([h for h in hospitals if search_query.lower() in h["name"].lower()] if search_query else hospitals)

view = next((h for h in hospitals if h["name"] == selected_hospital), hospitals[0])

view_state = pdk.ViewState(latitude=view["lat"], longitude=view["lon"], zoom=13, pitch=0)

st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/dark-v10",
    initial_view_state=view_state,
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=filtered_data,
            get_position='[lon, lat]',
            get_radius=200,
            get_fill_color=[255, 0, 0, 160],
            pickable=True
        ),
        pdk.Layer(
            "TextLayer",
            data=filtered_data,
            get_position='[lon, lat]',
            get_text='name',
            get_size=16,
            get_color=[255, 255, 255],
            get_alignment_baseline="bottom"
        )
    ],
    tooltip={
        "html": "<b>{name}</b><br/>РКТ: {rkt}<br/>МРТ: {mrt}<br/>Тел: {phone}<br/>Адрес: {address}<br/><a href='https://yandex.by/maps/?ll={lon}%2C{lat}&z=16' target='_blank'>Открыть в Яндекс.Картах</a>",
        "style": {"backgroundColor": "white", "color": "black", "fontSize": "12px"}
    }
))

hospital_details = next((h for h in hospitals if h["name"] == selected_hospital), hospitals[0])

st.subheader(f"Информация об учреждении: {hospital_details['name']}")
st.image(hospital_details['photo'], use_column_width=True)
st.markdown(f"**Адрес:** {hospital_details['address']}")
st.markdown(f"**Телефон:** {hospital_details['phone']}")
st.markdown(f"**РКТ:** {hospital_details['rkt']}")
st.markdown(f"**МРТ:** {hospital_details['mrt']}")
st.markdown(f"**Доступность:** {hospital_details['access']}")

yandex_url = f"https://yandex.by/maps/?ll={hospital_details['lon']}%2C{hospital_details['lat']}&z=16"
st.markdown(f"[Открыть в Яндекс.Картах]({yandex_url})")
