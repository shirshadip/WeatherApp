import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="AI Weather App",
    page_icon="🌦️",
    layout="centered"
)

API_KEY = st.secrets["api_key"]

tab1, tab2 = st.tabs([
    "🌤 Current Weather",
    "📄 JSON Data"
])

with tab1:

    city = st.text_input("Enter City")

    if city:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            col1, col2, col3 = st.columns(3)

            col1.metric(
                "🌡 Temperature",
                f"{data['main']['temp']} °C"
            )

            col2.metric(
                "💧 Humidity",
                f"{data['main']['humidity']} %"
            )

            col3.metric(
                "🥵 Feels Like",
                f"{data['main']['feels_like']} °C"
            )

            st.write("Latitude:", data["coord"]["lat"])
            st.write("Longitude:", data["coord"]["lon"])

            df = pd.read_csv("weather_last_30_days.csv")

            st.subheader("Historical Weather Data")

            st.dataframe(df, use_container_width=True)

        else:
            st.error("City not found.")

with tab2:

    city = st.text_input("Enter City", key="json_city")

    if city:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:
            st.json(response.json())
        else:
            st.error("City not found.")