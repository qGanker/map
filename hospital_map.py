import streamlit as st
import pydeck as pdk
import pandas as pd

# Данные о больницах
data = pd.DataFrame([
    {
        "name": "Гомельская областная клиническая больница",
        "lat": 52.4228,
        "lon": 30.9784,
        "rkt": "Aquilion LB (16 срезов)",
        "mrt": "Ingenia Philips 1.5T"
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
        "mrt": "Ingenia Philips 1.5T"
    },
    {
        "name": "Мозырская городская больница",
        "lat": 52.0424,
        "lon": 29.2725,
        "rkt": "BrightSpeed Elite (16 срезов)",
        "mrt": "ANKE SuperMarie 1.5T"
    },
    {
        "name": "Мозырская ЦРБ",
        "lat": 52.0506,
        "lon": 29.2596,
        "rkt": "Somatom go.Up (32 среза)",
        "mrt": "MagFinder WA 13200 (1.5T)"
    },
    {
        "name": "Жлобинская ЦРБ",
        "lat": 52.8923,
        "lon": 30.0262,
        "rkt": "Somatom go.Up (32 среза)",
        "mrt": "—"
    },
    {
        "name": "Светлогорская ЦРБ",
        "lat": 52.6281,
        "lon": 29.7396,
        "rkt": "Toshiba Aquilion (16 срезов)",
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
        "rkt": "Ventum (64 среза)",
        "mrt": "—"
    },
    {
        "name": "Хойникская ЦРБ",
        "lat": 51.8802,
        "lon": 29.6257,
        "rkt": "Ventum (64 среза)",
        "mrt": "—"
    },
    {
        "name": "Чечерская ЦРБ",
        "lat": 52.9145,
        "lon": 30.9040,
        "rkt": "Ventum (64 среза)",
        "mrt": "—"
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

# Выбор учреждения
if not filtered.empty:
    selected_name = st.selectbox("📋 Выберите учреждение", filtered["name"])
    selected_row = filtered[filtered["name"] == selected_name].iloc[0]
    lat_center = selected_row["lat"]
    lon_center = selected_row["lon"]
    zoom_level = 40  # Увеличенный зум
else:
    st.warning("Нет учреждений, удовлетворяющих фильтрам.")
    st.stop()

# Карта с приближением к выбранной больнице
st.pydeck_chart(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state=pdk.ViewState(
        latitude=lat_center,
        longitude=lon_center,
        zoom=zoom_level,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=filtered,
            get_position='[lon, lat]',
            get_radius=200,
            get_fill_color=[255, 0, 0, 160],
            pickable=True,
        ),
        pdk.Layer(
            "TextLayer",
            data=filtered,
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

# Информация о выбранной больнице
st.markdown(f"""
### ℹ️ Информация о выбранной больнице:
- **Название:** {selected_row['name']}
- **🖥 РКТ:** {selected_row['rkt']}
- **🧲 МРТ:** {selected_row['mrt']}
""")
