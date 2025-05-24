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
        "contacts": "📍 ул. Головацкого, 123, Гомель\n📞 +375 232 41-04-60 (регистратура)\n📞 +375 232 41-04-63 (справочная)\n🌐 https://gomelonk.by/",
        "image": "images/gomel_onko.jpg"
    },
    {
        "name": "Гомельская областная клиническая больница",
        "lat": 52.4228,
        "lon": 30.9784,
        "rkt": "Light Speed Pro16 (19 срезов), Revolution Evo (128 срезов)",
        "mrt": "iField (1.5T)",
        "contacts": "📍 ул. Ильича, 152, Гомель\n📞 +375 232 75-41-00 (справочная)\n📞 +375 232 75-41-01 (приемная)\n🌐 https://gokb.by/",
        "image": "images/gomel_okb.jpg"
    },
    {
        "name": "Гомельский областной клинический госпиталь ИВОВ",
        "lat": 52.4300,
        "lon": 31.0000,
        "rkt": "GE Bright Speed Elite 16 (16 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Богданова, 13, Гомель\n📞 +375 232 33-52-11 (регистратура)\n🌐 http://ivov-gomel.by/",
        "image": "images/gomel_ivov.jpg"
    },
    {
        "name": "Гомельская областная клиническая детская больница",
        "lat": 52.4100,
        "lon": 30.9900,
        "rkt": "Toshiba Aquilion lightning (80 срезов)",
        "mrt": "PHILIPS Ingenia 1,5T (1.5T)",
        "contacts": "📍 ул. Советская, 22, Гомель\n📞 +375 232 75-74-41 (справочная)\n📞 +375 232 75-74-42 (приемная)\n🌐 http://gocdb.by/",
        "image": "images/gomel_child.jpg"
    },
    {
        "name": "Гомельский областной клинический кардиологический центр",
        "lat": 52.4150,
        "lon": 31.0050,
        "rkt": "Light Speed Pro32 (32 срезов)",
        "mrt": "MPT UIH uMR680 (1.5T)",
        "contacts": "📍 ул. Рокоссовского, 49, Гомель\n📞 +375 232 49-17-49 (регистратура)\n🌐 http://cardio.gomel.by/",
        "image": "images/gomel_cardio.jpg"
    },
    {
        "name": "Гомельская областная клиническая туберкулезная больница",
        "lat": 52.4000,
        "lon": 30.9800,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Богданова, 1, Гомель\n📞 +375 232 33-52-04 (регистратура)\n📞 +375 232 33-52-05 (приемная)",
        "image": "images/gomel_tub.jpg"
    },
    {
        "name": "Гомельская центральная городская клиническая поликлиника",
        "lat": 52.4250,
        "lon": 30.9950,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Ильича, 286, Гомель\n📞 +375 232 75-71-41 (регистратура)\n🌐 http://ggkp.by/",
        "image": "images/gomel_polyclinic.jpg"
    },
    {
        "name": "Гомельская городская клиническая больница скорой медицинской помощи",
        "lat": 52.4350,
        "lon": 30.9850,
        "rkt": "Ventum (64 срезов)",
        "mrt": "ANKE SuperMark (1.5T)",
        "contacts": "📍 ул. Комиссарова, 12, Гомель\n📞 +375 232 75-31-41 (справочная)\n🌐 http://gkb-smp.by/",
        "image": "images/gomel_emergency.jpg"
    },
    {
        "name": "Гомельская городская больница №1",
        "lat": 52.4416,
        "lon": 30.9942,
        "rkt": "Revolution Evo (128 срезов)",
        "mrt": "—",
        "contacts": "📍 пр-т Октября, 96, Гомель\n📞 +375 232 95-70-01 (регистратура)\n🌐 http://gkb1.by/",
        "image": "images/gomel_gkb1.jpg"
    },
    {
        "name": "Гомельская городская больница №2",
        "lat": 52.4380,
        "lon": 31.0000,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Медицинская, 1, Гомель\n📞 +375 232 56-91-03 (регистратура)",
        "image": "images/gomel_gkb2.jpg"
    },
    {
        "name": "Гомельская городская клиническая больница №3",
        "lat": 52.4400,
        "lon": 30.9800,
        "rkt": "SOMATOM EMOTION MSOMATOM EMOTION (6 срезов), Somatom go.Up (64 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Мазурова, 10В, Гомель\n📞 +375 232 40-52-03 (регистратура)\n🌐 http://gkb3.by/",
        "image": "images/gomel_gkb3.jpg"
    },
    {
        "name": "Брагинская ЦРБ",
        "lat": 51.7900,
        "lon": 30.2700,
        "rkt": "Somatom go.Up (64 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Советская, 74, Брагин\n📞 +375 2344 2-15-41 (регистратура)",
        "image": "images/bragin_crb.jpg"
    },
    {
        "name": "Житковичская ЦРБ",
        "lat": 52.2200,
        "lon": 27.8600,
        "rkt": "Somatom go.Up (64 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Советская, 123, Житковичи\n📞 +375 2353 2-25-41 (регистратура)\n🌐 http://zhitkov-crb.by/",
        "image": "images/zhitkovichi_crb.jpg"
    },
    {
        "name": "Жлобинская ЦРБ",
        "lat": 52.8923,
        "lon": 30.0262,
        "rkt": "GE Bright Speed Elite 16 (16 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Первомайская, 40, Жлобин\n📞 +375 2334 2-34-56 (регистратура)\n🌐 https://zhlcrb.by/",
        "image": "images/zhlobin_crb.jpg"
    },
    {
        "name": "Калинковичская ЦРБ",
        "lat": 52.1300,
        "lon": 29.3300,
        "rkt": "Somatom go.Up (64 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Куйбышева, 1, Калинковичи\n📞 +375 2345 2-56-78 (регистратура)\n🌐 http://kalinkovichi-crb.by/",
        "image": "images/kalinkovichi_crb.jpg"
    },
    {
        "name": "Лельчицкая ЦРБ",
        "lat": 51.7800,
        "lon": 28.3300,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Советская, 45, Лельчицы\n📞 +375 2356 2-12-34 (регистратура)",
        "image": "images/lelchitsy_crb.jpg"
    },
    {
        "name": "Мозырская городская больница",
        "lat": 52.0424,
        "lon": 29.2725,
        "rkt": "Somatom go.Up (64 срезов)",
        "mrt": "MagFinder II/A 13200 (0.32T)",
        "contacts": "📍 ул. Притыцкого, 47, Мозырь\n📞 +375 236 32-45-67 (регистратура)\n🌐 http://mozyr-crb.by/",
        "image": "images/mozyr_gor.jpg"
    },
    {
        "name": "Мозырский городской онкологический диспансер",
        "lat": 52.0450,
        "lon": 29.2750,
        "rkt": "Aquilion (80 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Медицинская, 5, Мозырь\n📞 +375 236 32-56-78 (регистратура)",
        "image": "images/mozyr_onko.jpg"
    },
    {
        "name": "Петриковская ЦРБ",
        "lat": 52.1282,
        "lon": 28.4868,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Кирова, 43, Петриков\n📞 +375 2350 2-34-56 (регистратура)\n🌐 http://petrikov-crb.by/",
        "image": "images/petrikov_crb.jpg"
    },
    {
        "name": "Речицкая ЦРБ",
        "lat": 52.3690,
        "lon": 30.3896,
        "rkt": "Ventum (32 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Советская, 144, Речица\n📞 +375 2340 2-45-67 (регистратура)\n🌐 http://rechcrb.by/",
        "image": "images/rechitsa_crb.jpg"
    },
    {
        "name": "Рогачевская ЦРБ",
        "lat": 53.0800,
        "lon": 30.0500,
        "rkt": "ANATOM PRECISION (128 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Ленина, 12, Рогачев\n📞 +375 2339 2-34-56 (регистратура)\n🌐 http://rogachev-crb.by/",
        "image": "images/rogachev_crb.jpg"
    },
    {
        "name": "Светлогорская ЦРБ",
        "lat": 52.6281,
        "lon": 29.7396,
        "rkt": "Toshiba Aquilion (32 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Интернациональная, 14, Светлогорск\n📞 +375 2342 2-34-56 (регистратура)\n🌐 http://svetlogorsk-crb.by/",
        "image": "images/svetlogorsk_crb.jpg"
    },
    {
        "name": "Чечерская ЦРБ",
        "lat": 52.9145,
        "lon": 30.9040,
        "rkt": "Ventum (128 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Ленина, 15, Чечерск\n📞 +375 2332 2-12-34 (регистратура)\n🌐 http://chechersk-crb.by/",
        "image": "images/chechersk_crb.jpg"
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
    st.image(selected_row["image"], caption=selected_row["name"], use_container_width=True)
else:
    st.info("Фото пока недоступно.")
