import streamlit as st
import pydeck as pdk
import pandas as pd
import os

# Загружаем данные
data = pd.DataFrame([
    {
        "name": "Гомельский областной клинический онкологический диспансер",
        "lat": 52.4204,
        "lon": 31.0072,
        "rkt": "Aquilion LB (16 срезов), AQUILION Lightning (80 срезов)",
        "mrt": "SIEMENS Magneton Avanto-i 1,5 (1.5T)",
        "contacts": "📍 ул. Головацкого, 123, Гомель\n📞 +375 232 41-04-60\n🌐 https://gomelonk.by/",
        "image": "images/gomel_onko.jpg"
    },
    {
        "name": "Гомельская областная клиническая больница",
        "lat": 52.4228,
        "lon": 30.9784,
        "rkt": "Light Speed Pro16 (19 срезов), Revolution Evo (128 срезов)",
        "mrt": "iField (1.5T)",
        "contacts": "📍 ул. Ильича, 152, Гомель\n📞 +375 232 75-41-00\n🌐 https://gokb.by/",
        "image": "images/gomel_obl.jpg"
    },
    {
        "name": "Гомельский областной клинический госпиталь ИВОВ",
        "lat": 52.4300,
        "lon": 31.0000,
        "rkt": "GE Bright Speed Elite 16 (16 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. [адрес не указан], Гомель\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Гомельская областная клиническая детская больница",
        "lat": 52.4100,
        "lon": 30.9900,
        "rkt": "Toshiba Aquilion lightning (80 срезов)",
        "mrt": "PHILIPS Ingenia 1,5T (1.5T)",
        "contacts": "📍 [адрес не указан], Гомель\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Гомельский областной клинический кардиологический центр",
        "lat": 52.4150,
        "lon": 31.0050,
        "rkt": "Light Speed Pro32 (32 срезов)",
        "mrt": "MPT UIH uMR680 (1.5T)",
        "contacts": "📍 [адрес не указан], Гомель\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Гомельская областная клиническая туберкулезная больница",
        "lat": 52.4000,
        "lon": 30.9800,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "contacts": "📍 [адрес не указан], Гомель\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Гомельская центральная городская клиническая поликлиника",
        "lat": 52.4250,
        "lon": 30.9950,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "contacts": "📍 [адрес не указан], Гомель\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Гомельская городская клиническая больница скорой медицинской помощи",
        "lat": 52.4350,
        "lon": 30.9850,
        "rkt": "Ventum (64 срезов)",
        "mrt": "ANKE SuperMark (1.5T)",
        "contacts": "📍 [адрес не указан], Гомель\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Гомельская городская больница №1",
        "lat": 52.4416,
        "lon": 30.9942,
        "rkt": "Revolution Evo (128 срезов)",
        "mrt": "—",
        "contacts": "📍 пр-т Октября, 96, Гомель\n📞 +375 232 95-70-01\n🌐 http://gkb1.by/",
        "image": "images/gkb1.jpg"
    },
    {
        "name": "Гомельская городская больница №2",
        "lat": 52.4380,
        "lon": 31.0000,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "contacts": "📍 [адрес не указан], Гомель\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Гомельская городская клиническая больница №3",
        "lat": 52.4400,
        "lon": 30.9800,
        "rkt": "SOMATOM EMOTION MSOMATOM EMOTION (6 срезов), Somatom go.Up (64 срезов)",
        "mrt": "—",
        "contacts": "📍 [адрес не указан], Гомель\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Брагинская ЦРБ",
        "lat": 51.7900,
        "lon": 30.2700,
        "rkt": "Somatom go.Up (64 срезов)",
        "mrt": "—",
        "contacts": "📍 [адрес не указан], Брагин\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Житковичская ЦРБ",
        "lat": 52.2200,
        "lon": 27.8600,
        "rkt": "Somatom go.Up (64 срезов)",
        "mrt": "—",
        "contacts": "📍 [адрес не указан], Житковичи\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Жлобинская ЦРБ",
        "lat": 52.8923,
        "lon": 30.0262,
        "rkt": "GE Bright Speed Elite 16 (16 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Первомайская, 40, Жлобин\n📞 +375 2334 79-316\n🌐 https://zhlcrb.by/",
        "image": "images/zhlobin.jpg"
    },
    {
        "name": "Калинковичская ЦРБ",
        "lat": 52.1300,
        "lon": 29.3300,
        "rkt": "Somatom go.Up (64 срезов)",
        "mrt": "—",
        "contacts": "📍 [адрес не указан], Калинковичи\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Лельчицкая ЦРБ",
        "lat": 51.7800,
        "lon": 28.3300,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "contacts": "📍 [адрес не указан], Лельчицы\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Мозырская городская больница",
        "lat": 52.0424,
        "lon": 29.2725,
        "rkt": "Somatom go.Up (64 срезов)",
        "mrt": "MagFinder II/A 13200 (0.32T)",
        "contacts": "📍 ул. Притыцкого, 47, Мозырь\n📞 +375 236 39-57-35\n🌐 http://mozyrcrb.by/",
        "image": "images/mozyr_gor.jpg"
    },
    {
        "name": "Мозырский городской онкологический диспансер",
        "lat": 52.0450,
        "lon": 29.2750,
        "rkt": "Aquilion (80 срезов)",
        "mrt": "—",
        "contacts": "📍 [адрес не указан], Мозырь\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Петриковская ЦРБ",
        "lat": 52.1282,
        "lon": 28.4868,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Кирова, 43, Петриков\n📞 +375 2350 5-13-60",
        "image": "images/petrikov.jpg"
    },
    {
        "name": "Речицкая ЦРБ",
        "lat": 52.3690,
        "lon": 30.3896,
        "rkt": "Ventum (32 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Советская, 144, Речица\n📞 +375 2340 3-60-85\n🌐 http://rechcrb.by/",
        "image": "images/rechitsa.jpg"
    },
    {
        "name": "Рогачевская ЦРБ",
        "lat": 53.0800,
        "lon": 30.0500,
        "rkt": "ANATOM PRECISION (128 срезов)",
        "mrt": "—",
        "contacts": "📍 [адрес не указан], Рогачев\n📞 [телефон не указан]",
        "image": "images/default.jpg"
    },
    {
        "name": "Светлогорская ЦРБ",
        "lat": 52.6281,
        "lon": 29.7396,
        "rkt": "Toshiba Aquilion (32 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Интернациональная, 14, Светлогорск\n📞 +375 2342 3-19-94\n🌐 http://svcrb.by/",
        "image": "images/svetlogorsk.jpg"
    },
    {
        "name": "Чечерская ЦРБ",
        "lat": 52.9145,
        "lon": 30.9040,
        "rkt": "Ventum (128 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Ленина, 15, Чечерск\n📞 +375 2332 2-12-65",
        "image": "images/chechersk.jpg"
    }
])

# Заголовок
st.title("🏥 Учреждения здравоохранения Гомельской области")

# Фильтры
st.sidebar.header("🔎 Фильтры")
has_rkt = st.sidebar.checkbox("Показать только с РКТ", value=False)
has_mrt = st.sidebar.checkbox("Показать только с МРТ", value=False)

filtered = data.copy()
if has_rkt:
    filtered = filtered[~filtered["rkt"].str.strip().isin(["—", "Нет", ""])]
if has_mrt:
    filtered = filtered[~filtered["mrt"].str.strip().isin(["—", "Нет", ""])]

selected_name = st.selectbox("📋 Выберите учреждение", filtered["name"] if not filtered.empty else ["Нет учреждений"])

if not filtered.empty:
    selected_row = filtered[filtered["name"] == selected_name].iloc[0]
    zoom_level = 15
else:
    st.warning("Нет учреждений, удовлетворяющих выбранным фильтрам.")
    st.stop()

# Карта
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v10',
    initial_view_state=pdk.ViewState(
        latitude=selected_row["lat"],
        longitude=selected_row["lon"],
        zoom=zoom_level,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=filtered,
            get_position='[lon, lat]',
            get_radius=250,
            get_fill_color=[255, 0, 0, 160],
            pickable=True
        ),
        pdk.Layer(
            "TextLayer",
            data=filtered,
            get_position='[lon, lat]',
            get_text='name',
            get_size=14,
            get_color=[255, 255, 255],
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

# Информация
st.markdown(f"""
### ℹ️ Информация о выбранной больнице:
- **Название:** {selected_row['name']}
- **🖥 РКТ:** {selected_row['rkt']}
- **🧲 МРТ:** {selected_row['mrt']}
- **📞 Контакты:**  
{selected_row['contacts']}
""")

# Фотография
if os.path.exists(selected_row["image"]):
    st.image(selected_row["image"], caption=selected_row["name"], use_column_width=True)
else:
    st.info("Фото пока недоступно.")
