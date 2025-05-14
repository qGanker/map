import streamlit as st
import pydeck as pdk
import pandas as pd

# Основные данные о больницах
data = pd.DataFrame([
    {
        "name": "Гомельская областная клиническая больница",
        "lat": 52.4228,
        "lon": 30.9784,
        "rkt": "Aquilion LB (16 срезов)",
        "mrt": "Ingenia Philips 1.5T",
        "contacts": "📍 ул. Ильича, 152, Гомель\n📞 +375 232 75-41-00\n🌐 https://gokb.by/"
    },
    {
        "name": "Гомельский онкодиспансер",
        "lat": 52.4204,
        "lon": 31.0072,
        "rkt": "Aquilion Lightning (80 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Головацкого, 123, Гомель\n📞 +375 232 41-04-60\n🌐 https://gomelonk.by/"
    },
    {
        "name": "Гомельская городская клиническая больница №1",
        "lat": 52.4416,
        "lon": 30.9942,
        "rkt": "Revolution Evo (28 срезов)",
        "mrt": "Ingenia Philips 1.5T",
        "contacts": "📍 пр-т Октября, 96, Гомель\n📞 +375 232 95-70-01\n🌐 http://gkb1.by/"
    },
    {
        "name": "Мозырская городская больница",
        "lat": 52.0424,
        "lon": 29.2725,
        "rkt": "BrightSpeed Elite (16 срезов)",
        "mrt": "ANKE SuperMarie 1.5T",
        "contacts": "📍 ул. Притыцкого, 47, Мозырь\n📞 +375 236 39-57-35\n🌐 http://mozyrcrb.by/"
    },
    {
        "name": "Мозырская ЦРБ",
        "lat": 52.0506,
        "lon": 29.2596,
        "rkt": "Somatom go.Up (32 среза)",
        "mrt": "MagFinder WA 13200 (1.5T)",
        "contacts": "📍 ул. Советская, 176, Мозырь\n📞 +375 236 39-57-35\n🌐 http://mozyrcrb.by/"
    },
    {
        "name": "Жлобинская ЦРБ",
        "lat": 52.8923,
        "lon": 30.0262,
        "rkt": "Somatom go.Up (32 среза)",
        "mrt": "—",
        "contacts": "📍 ул. Первомайская, 40, Жлобин\n📞 +375 2334 79-316\n🌐 https://zhlcrb.by/"
    },
    {
        "name": "Светлогорская ЦРБ",
        "lat": 52.6281,
        "lon": 29.7396,
        "rkt": "Toshiba Aquilion (16 срезов)",
        "mrt": "—",
        "contacts": "📍 ул. Интернациональная, 14, Светлогорск\n📞 +375 2342 3-19-94\n🌐 http://svcrb.by/"
    },
    {
        "name": "Речицкая ЦРБ",
        "lat": 52.3690,
        "lon": 30.3896,
        "rkt": "Ventum (64 среза)",
        "mrt": "—",
        "contacts": "📍 ул. Советская, 144, Речица\n📞 +375 2340 3-60-85\n🌐 http://rechcrb.by/"
    },
    {
        "name": "Петриковская ЦРБ",
        "lat": 52.1282,
        "lon": 28.4868,
        "rkt": "Ventum (64 среза)",
        "mrt": "—",
        "contacts": "📍 ул. Кирова, 43, Петриков\n📞 +375 2350 5-13-60"
    },
    {
        "name": "Хойникская ЦРБ",
        "lat": 51.8802,
        "lon": 29.6257,
        "rkt": "Ventum (64 среза)",
        "mrt": "—",
        "contacts": "📍 ул. Советская, 58, Хойники\n📞 +375 2336 5-13-81"
    },
    {
        "name": "Чечерская ЦРБ",
        "lat": 52.9145,
        "lon": 30.9040,
        "rkt": "Ventum (64 среза)",
        "mrt": "—",
        "contacts": "📍 ул. Ленина, 15, Чечерск\n📞 +375 2332 2-12-65"
    },
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
