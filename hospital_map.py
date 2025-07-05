import streamlit as st
import pandas as pd
import os
import folium
from streamlit_folium import st_folium

# Загружаем данные
data = pd.DataFrame([
    {
        "name": "Гомельский областной клинический онкологический диспансер",
        "lat": 52.4204,
        "lon": 31.0072,
        "rkt": "Aquilion LB (16 срезов), AQUILION Lightning (80 срезов)",
        "mrt": "SIEMENS Magneton Avanto-i 1,5 (1.5T)",
        "uzi": "—",
        "contacts": "📍 ул. Медицинская, 2, Гомель\n📞 +375 232 33-56-70\n🌐 https://gomelod.by/",
        "image": "images/gomel_onko.jpg"
    },
    {
        "name": "Гомельская областная клиническая больница",
        "lat": 52.4170,
        "lon": 31.0150,
        "rkt": "Light Speed Pro16 (16 срезов), Revolution Evo (128 срезов)",
        "mrt": "iField (1.5T)",
        "uzi": "—",
        "contacts": "📍 ул. Братьев Лизюковых, 5, Гомель\n📞 +375 232 34-72-92\n🌐 https://gokb.by/",
        "image": "images/gomel_okb.jpg"
    },
    {
        "name": "Гомельский областной клинический госпиталь ИВОВ",
        "lat": 52.4280,
        "lon": 31.0180,
        "rkt": "GE Bright Speed Elite 16 (16 срезов)",
        "mrt": "—",
        "uzi": "—",
        "contacts": "📍 ул. Ильича, 284, Гомель\n📞 +375 232 37-80-55\n🌐 http://ivov-gomel.by/",
        "image": "images/gomel_ivov.jpg"
    },
    {
        "name": "Гомельская областная детская клиническая больница",
        "lat": 52.4100,
        "lon": 30.9900,
        "rkt": "Toshiba Aquilion lightning (80 срезов)",
        "mrt": "PHILIPS Ingenia 1,5T (1.5T)",
        "uzi": "—",
        "contacts": "📍 ул. Жарковского, 7, Гомель\n📞 +375 232 34-79-92\n🌐 http://gocdb.by/",
        "image": "images/gomel_child.jpg"
    },
    {
        "name": "Гомельский областной клинический кардиологический центр",
        "lat": 52.4150,
        "lon": 31.0050,
        "rkt": "Light Speed Pro32 (32 срезов)",
        "mrt": "MPT UIH uMR680 (1.5T)",
        "uzi": "—",
        "contacts": "📍 ул. Медицинская, 4, Гомель\n📞 +375 232 34-71-33\n🌐 http://cardio.gomel.by/",
        "image": "images/gomel_cardio.jpg"
    },
    {
        "name": "Гомельская областная туберкулезная клиническая больница",
        "lat": 52.4000,
        "lon": 30.9800,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "uzi": "—",
        "contacts": "📍 ул. Богданова, 1, Гомель\n📞 +375 232 33-52-04",
        "image": "images/gomel_tub.jpg"
    },
    {
        "name": "Гомельская центральная городская клиническая поликлиника",
        "lat": 52.4250,
        "lon": 30.9950,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "uzi": "SONOLINE (G60S, G50, G20S, Adara, PRIMA), GE (LOGIQ S7, LOGIQ C5), Sonoscape (вкл. S20exp), Medison SonoACE R7, CHISON Qbit10, SA 8000EX, SIUI Apogee 3800, ACUSON (X 500, NX 3), Aloca prosound SSD-3500SV, WEР-9618",
        "contacts": "📍 ул. Ильича, 286, Гомель\n📞 +375 232 75-71-41\n🌐 http://ggkp.by/",
        "image": "images/gomel_polyclinic.jpg"
    },
    {
        "name": "Гомельская городская клиническая больница скорой медицинской помощи",
        "lat": 52.4350,
        "lon": 30.9850,
        "rkt": "Ventum (64 срезов)",
        "mrt": "ANKE SuperMark (1.5T)",
        "uzi": "TOSHIBA APLIO XG, SONOLINE G60 S, MINDRAY DC7",
        "contacts": "📍 ул. Комиссарова, 12, Гомель\n📞 +375 232 75-31-41\n🌐 http://gkb-smp.by/",
        "image": "images/gomel_emergency.jpg"
    },
    {
        "name": "Гомельская городская больница №1",
        "lat": 52.4416,
        "lon": 30.9942,
        "rkt": "Revolution Evo (128 срезов)",
        "mrt": "—",
        "uzi": "SONO ACE-X6, SONO ACE R7",
        "contacts": "📍 пр-т Октября, 96, Гомель\n📞 +375 232 95-70-01\n🌐 http://gkb1.by/",
        "image": "images/gomel_gkb1.jpg"
    },
    {
        "name": "Гомельская городская поликлиника №1",
        "lat": 52.4045,
        "lon": 31.0203,
        "rkt": "—",
        "mrt": "—",
        "uzi": "SONOLINE G50S, Sonoscape S20exp, Megas FD-570A, SIEMENS Sonoline G-50",
        "contacts": "📍 ул. Косарева, 19, Гомель\n📞 +375 232 31-99-60",
        "image": "images/placeholder.jpg"
    },
    {
        "name": "Гомельская городская больница №2",
        "lat": 52.4380,
        "lon": 31.0000,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "uzi": "SA 8000, ALOKA SSD 1700, Aloca 3500, Logiq P5",
        "contacts": "📍 ул. Медицинская, 1, Гомель\n📞 +375 232 56-91-03",
        "image": "images/gomel_gkb2.jpg"
    },
    {
        "name": "Гомельская городская клиническая больница №3",
        "lat": 52.4400,
        "lon": 30.9800,
        "rkt": "SOMATOM EMOTION MSOMATOM EMOTION (6 срезов), Somatom go.Up (64 срезов)",
        "mrt": "—",
        "uzi": "SonoScape S40 Pro, Logiq P5, SA 8000, Siemens Acuson Х 500, MINDRAY М7, ASTRUM X 7",
        "contacts": "📍 ул. Мазурова, 10В, Гомель\n📞 +375 232 40-52-03\n🌐 http://gkb3.by/",
        "image": "images/gomel_gkb3.jpg"
    },
    {
        "name": "Гомельская городская больница №4",
        "lat": 52.4093,
        "lon": 30.9634,
        "rkt": "—",
        "mrt": "—",
        "uzi": "SONOACE R7, Aloka SSD-630",
        "contacts": "📍 ул. Богдана Хмельницкого, 79, Гомель\n📞 +375 232 53-35-64",
        "image": "images/placeholder.jpg"
    },
    {
        "name": "Гомельская центральная городская детская клиническая поликлиника",
        "lat": 52.4495,
        "lon": 30.9680,
        "rkt": "—",
        "mrt": "—",
        "uzi": "LOGIQ (P9, P5), MINDRAY (МХ ДС7, DC7), SIEMENS (Sonoline G60S, Acusion NX3, Prima SLC), В-К Меdikal PRO FOKUS 2202, Chison Qbit10, WED-9618",
        "contacts": "📍 ул. Мазурова, 28, Гомель\n📞 +375 232 20-75-75\n🌐 http://gscdp.by/",
        "image": "images/placeholder.jpg"
    },
    {
        "name": "Брагинская ЦРБ",
        "lat": 51.7900,
        "lon": 30.2700,
        "rkt": "Somatom go.Up (64 срезов)",
        "mrt": "—",
        "uzi": "—",
        "contacts": "📍 ул. Советская, 74, Брагин\n📞 +375 2344 2-15-41",
        "image": "images/bragin_crb.jpg"
    },
    {
        "name": "Житковичская ЦРБ",
        "lat": 52.2200,
        "lon": 27.8600,
        "rkt": "Somatom go.Up (64 срезов)",
        "mrt": "—",
        "uzi": "—",
        "contacts": "📍 ул. Советская, 123, Житковичи\n📞 +375 2353 2-25-41\n🌐 http://zhitkov-crb.by/",
        "image": "images/zhitkovichi_crb.jpg"
    },
    {
        "name": "Жлобинская ЦРБ",
        "lat": 52.8923,
        "lon": 30.0262,
        "rkt": "GE Bright Speed Elite 16 (16 срезов)",
        "mrt": "—",
        "uzi": "—",
        "contacts": "📍 ул. Первомайская, 40, Жлобин\n📞 +375 2334 2-34-56\n🌐 https://zhlcrb.by/",
        "image": "images/zhlobin_crb.jpg"
    },
    {
        "name": "Калинковичская ЦРБ",
        "lat": 52.1300,
        "lon": 29.3300,
        "rkt": "Somatom go.Up (64 срезов)",
        "mrt": "—",
        "uzi": "—",
        "contacts": "📍 ул. Куйбышева, 1, Калинковичи\n📞 +375 2345 2-56-78\n🌐 http://kalinkovichi-crb.by/",
        "image": "images/kalinkovichi_crb.jpg"
    },
    {
        "name": "Лельчицкая ЦРБ",
        "lat": 51.7800,
        "lon": 28.3300,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "uzi": "—",
        "contacts": "📍 ул. Советская, 45, Лельчицы\n📞 +375 2356 2-12-34",
        "image": "images/lelchitsy_crb.jpg"
    },
    {
        "name": "Мозырская городская больница",
        "lat": 52.0424,
        "lon": 29.2725,
        "rkt": "Somatom go.Up (64 срезов)",
        "mrt": "MagFinder II/A 13200 (0.32T)",
        "uzi": "—",
        "contacts": "📍 ул. Притыцкого, 47, Мозырь\n📞 +375 236 32-45-67\n🌐 http://mozyr-crb.by/",
        "image": "images/mozyr_gor.jpg"
    },
    {
        "name": "Мозырский городской онкологический диспансер",
        "lat": 52.0450,
        "lon": 29.2750,
        "rkt": "Aquilion (80 срезов)",
        "mrt": "—",
        "uzi": "—",
        "contacts": "📍 ул. Медицинская, 5, Мозырь\n📞 +375 236 32-56-78",
        "image": "images/mozyr_onko.jpg"
    },
    {
        "name": "Петриковская ЦРБ",
        "lat": 52.1282,
        "lon": 28.4868,
        "rkt": "Ventum (64 срезов)",
        "mrt": "—",
        "uzi": "—",
        "contacts": "📍 ул. Кирова, 43, Петриков\n📞 +375 2350 2-34-56\n🌐 http://petrikov-crb.by/",
        "image": "images/petrikov_crb.jpg"
    },
    {
        "name": "Речицкая ЦРБ",
        "lat": 52.3690,
        "lon": 30.3896,
        "rkt": "Ventum (32 срезов)",
        "mrt": "—",
        "uzi": "—",
        "contacts": "📍 ул. Советская, 144, Речица\n📞 +375 2340 2-45-67\n🌐 http://rechcrb.by/",
        "image": "images/rechitsa_crb.jpg"
    },
    {
        "name": "Рогачевская ЦРБ",
        "lat": 53.0800,
        "lon": 30.0500,
        "rkt": "ANATOM PRECISION (128 срезов)",
        "mrt": "—",
        "uzi": "—",
        "contacts": "📍 ул. Ленина, 12, Рогачев\n📞 +375 2339 2-34-56\n🌐 http://rogachev-crb.by/",
        "image": "images/rogachev_crb.jpg"
    },
    {
        "name": "Светлогорская ЦРБ",
        "lat": 52.6281,
        "lon": 29.7396,
        "rkt": "Toshiba Aquilion (32 срезов)",
        "mrt": "—",
        "uzi": "—",
        "contacts": "📍 ул. Интернациональная, 14, Светлогорск\n📞 +375 2342 2-34-56\n🌐 http://svetlogorsk-crb.by/",
        "image": "images/svetlogorsk_crb.jpg"
    },
    {
        "name": "Чечерская ЦРБ",
        "lat": 52.9145,
        "lon": 30.9040,
        "rkt": "Ventum (128 срезов)",
        "mrt": "—",
        "uzi": "—",
        "contacts": "📍 ул. Ленина, 15, Чечерск\n📞 +375 2332 2-12-34\n🌐 http://chechersk-crb.by/",
        "image": "images/chechersk_crb.jpg"
    }
])
# Заголовок
st.title("🏥 Учреждения здравоохранения Гомельской области")

# Фильтры
st.sidebar.header("🔎 Фильтры")
has_rkt = st.sidebar.checkbox("Показать только с РКТ", value=False)
has_mrt = st.sidebar.checkbox("Показать только с МРТ", value=False)
has_uzi = st.sidebar.checkbox("Показать только с УЗИ", value=False)

filtered = data.copy()
if has_rkt:
    filtered = filtered[~filtered["rkt"].str.strip().isin(["—", "Нет", ""])]
if has_mrt:
    filtered = filtered[~filtered["mrt"].str.strip().isin(["—", "Нет", ""])]
if has_uzi:
    filtered = filtered[~filtered["uzi"].str.strip().isin(["—", "Нет", ""])]

# Выбор учреждения
if not filtered.empty:
    sorted_names = sorted(filtered["name"].unique())
    selected_name = st.selectbox("📋 Выберите учреждение", sorted_names)
    selected_row = filtered[filtered["name"] == selected_name].iloc[0]
    zoom_level = 15
else:
    st.warning("Нет учреждений, удовлетворяющих выбранным фильтрам.")
    st.stop()

# --- БЛОК ДЛЯ СОЗДАНИЯ КАРТЫ ---
# Создаем карту с центром в выбранной больнице
m = folium.Map(location=[selected_row["lat"], selected_row["lon"]], zoom_start=zoom_level)

# Добавляем все отфильтрованные больницы на карту в виде кругов
for idx, row in filtered.iterrows():
    tooltip_text = f"""
    <b>{row['name']}</b><br>
    🖥 РКТ: {row['rkt']}<br>
    🧲 МРТ: {row['mrt']}<br>
    🩺 УЗИ: {row['uzi']}
    """
    folium.CircleMarker(
        location=[row["lat"], row["lon"]],
        radius=8,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.7,
        tooltip=tooltip_text
    ).add_to(m)


# Отображаем карту в Streamlit
st_folium(m, width=725, height=500, returned_objects=[])


# Информация под картой (остается без изменений)
st.markdown(f"""
### ℹ️ Информация о выбранной больнице:
- **Название:** {selected_row['name']}
- **🖥 РКТ:** {selected_row['rkt']}
- **🧲 МРТ:** {selected_row['mrt']}
- **🩺 УЗИ:** {selected_row['uzi']}
- **📞 Контакты:** {selected_row['contacts']}
""")

# Фотография
if "image" in selected_row and pd.notna(selected_row["image"]) and os.path.exists(selected_row["image"]):
    st.image(selected_row["image"], caption=selected_row["name"], use_container_width=True)
else:
    st.info("Фото пока недоступно.")
