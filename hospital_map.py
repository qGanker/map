import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# --- Данные по больницам ---
data = [
    {"name": "Гомельская областная клиническая больница", "ct_model": "Aquilion LB", "ct_slices": 16, "mri_model": "Ingenia Philips", "lat": 52.43, "lon": 30.99},
    {"name": "Гомельский онкодиспансер", "ct_model": "Aquilion Lightning", "ct_slices": 80, "mri_model": "—", "lat": 52.43, "lon": 30.98},
    {"name": "Гомельская городская клиническая больница №1", "ct_model": "Revolution Evo", "ct_slices": 28, "mri_model": "Ingenia Philips", "lat": 52.44, "lon": 30.97},
    {"name": "Мозырская городская больница", "ct_model": "Bright Speed Elite", "ct_slices": 16, "mri_model": "ANKE SuperMarie", "lat": 52.05, "lon": 29.26},
    {"name": "Мозырская ЦРБ", "ct_model": "Somatom go.Up", "ct_slices": "—", "mri_model": "MagFinder WA 13200", "lat": 52.03, "lon": 29.27},
    {"name": "Жлобинская ЦРБ", "ct_model": "Somatom Emotion / go.Up", "ct_slices": "—", "mri_model": "—", "lat": 52.89, "lon": 30.02},
    {"name": "Светлогорская ЦРБ", "ct_model": "Toshiba Aquilion", "ct_slices": "—", "mri_model": "—", "lat": 52.63, "lon": 29.73},
    {"name": "Речицкая ЦРБ", "ct_model": "Ventum", "ct_slices": 64, "mri_model": "—", "lat": 52.36, "lon": 30.39},
    {"name": "Петриковская ЦРБ", "ct_model": "Ventum", "ct_slices": "—", "mri_model": "—", "lat": 52.13, "lon": 28.49},
    {"name": "Хойникская ЦРБ", "ct_model": "Ventum", "ct_slices": "—", "mri_model": "—", "lat": 51.88, "lon": 30.26},
    {"name": "Чечерская ЦРБ", "ct_model": "Ventum", "ct_slices": "—", "mri_model": "—", "lat": 52.92, "lon": 30.91},
]
df = pd.DataFrame(data)

# --- Интерфейс ---
st.set_page_config(layout="wide")
st.title("Карта больниц Гомельской области")

search = st.text_input("🔍 Поиск по названию больницы:")

filtered_df = df[df["name"].str.contains(search, case=False)] if search else df

# --- Карта ---
map_center = [52.43, 30.99]
m = folium.Map(location=map_center, zoom_start=8)

for _, row in filtered_df.iterrows():
    popup_text = f"""
    <b>{row['name']}</b><br>
    <b>РКТ:</b> {row['ct_model']} ({row['ct_slices']} срезов)<br>
    <b>МРТ:</b> {row['mri_model']}
    """
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=popup_text,
        icon=folium.Icon(color="blue", icon="plus-sign")
    ).add_to(m)

st_data = st_folium(m, width=1200, height=600)

st.markdown("""
<small>❗ Все координаты условные. Информация собрана с предоставленных изображений.</small>
""", unsafe_allow_html=True)
