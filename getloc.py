import streamlit as st
import requests
from streamlit_geolocation import streamlit_geolocation

st.set_page_config(
    page_title="Auto Weather App",
    page_icon="🌦️"
)

st.title("🌦️ Automatic Weather App")

API_KEY = st.secrets["api_key"]

st.write("Click the button below and allow location access.")

location = streamlit_geolocation()

if location and location["latitude"] is not None:

    lat = location["latitude"]
    lon = location["longitude"]

    st.success("Location detected!")

    st.write(f"Latitude: {lat}")
    st.write(f"Longitude: {lon}")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        st.subheader(f"📍 {data['name']}")

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
            "💨 Wind",
            f"{data['wind']['speed']} m/s"
        )

        st.write(
            "Weather:",
            data["weather"][0]["description"].title()
        )

        st.json(data)

    else:
        st.error("Failed to fetch weather data.")

else:
    st.info("Waiting for location permission...")