import streamlit as st
import pandas as pd
import pydeck as pdk

# === Заголовок ===
st.set_page_config(page_title="Карта больниц Гомельской области", layout="wide")
st.title("\U0001F3E5 Больницы Гомельской области")

# === Данные (примерные координаты и информация) ===
data = [
    {"name": "Гомельская областная клиническая больница", "lat": 52.4412, "lon": 30.9878,
     "rct": "Siemens SOMATOM, 64 среза", "mrt": "Philips Ingenia, 1.5 Тл"},
    {"name": "Мозырская городская больница", "lat": 52.0436, "lon": 29.2722,
     "rct": "GE Optima CT, 16 срезов", "mrt": "Hitachi Aperto, 0.4 Тл"},
    {"name": "Речицкая ЦРБ", "lat": 52.3626, "lon": 30.3935,
     "rct": "Toshiba Aquilion, 32 среза", "mrt": "нет"},
    {"name": "Светлогорская ЦРБ", "lat": 52.6335, "lon": 29.7333,
     "rct": "Siemens Emotion, 16 срезов", "mrt": "нет"},
    {"name": "Жлобинская ЦРБ", "lat": 52.8924, "lon": 30.0184,
     "rct": "Philips Brilliance, 64 среза", "mrt": "нет"},
    {"name": "Новобелицкая больница (Гомель)", "lat": 52.4002, "lon": 30.9031,
     "rct": "Canon CT, 128 срезов", "mrt": "Siemens Avanto, 1.5 Тл"}
]

df = pd.DataFrame(data)

# === Поиск по названию ===
search = st.text_input("Поиск больницы по названию:").lower()
if search:
    df = df[df['name'].str.lower().str.contains(search)]

# === Карта ===
st.map(df[['lat', 'lon']])

# === Отображение информации по больницам ===
for index, row in df.iterrows():
    with st.expander(row['name']):
        st.markdown(f"**РКТ:** {row['rct']}")
        st.markdown(f"**МРТ:** {row['mrt']}")
