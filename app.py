import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, timezone
from streamlit_geolocation import streamlit_geolocation
import weatherreport


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AI Weather App",
    page_icon="🌦️",
    layout="wide"
)


# ==========================================================
# API KEY
# ==========================================================

API_KEY = st.secrets["api_key"]


# ==========================================================
# LOCATION DETECTION
# ==========================================================
# Try to get the user's current location using browser GPS.
# If the user denies access, we will show a manual city input.
# ==========================================================

location = streamlit_geolocation()

url = None
city = None


# ==========================================================
# AUTOMATIC LOCATION
# ==========================================================

if (
    location
    and location.get("latitude") is not None
    and location.get("longitude") is not None
):

    lat = location["latitude"]
    lon = location["longitude"]

    st.success("📍 Location detected automatically")

    # Fetch weather using coordinates
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}"
        f"&lon={lon}"
        f"&appid={API_KEY}"
        f"&units=metric"
    )

# ==========================================================
# MANUAL LOCATION INPUT
# ==========================================================

else:

    st.warning(
        "Location permission denied or unavailable. "
        "Please enter a location manually."
    )

    city = st.text_input(
        "Enter Location",
        placeholder="e.g. Kolkata",
        key="city_search_input"
    ).strip()

    if city:

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}"
            f"&appid={API_KEY}"
            f"&units=metric"
        )

    else:
        st.stop()


# ==========================================================
# WEATHER DATA FETCHING
# ==========================================================

data = None

try:

    with st.spinner("Fetching weather data..."):

        response = requests.get(url, timeout=10)

    if response.status_code == 200:

        data = response.json()

        # Actual city name returned by API
        city = data["name"]

    else:

        st.error("❌ Unable to find this location.")
        st.stop()

except requests.exceptions.RequestException:

    st.error("⚠️ Unable to connect to OpenWeatherMap.")
    st.stop()


# ==========================================================
# TABS
# ==========================================================

tab1, tab2, tab3 = st.tabs(
    [
        "🌤 Current Weather",
        "📈 Weather Visualizations",
        "📄 JSON Data"
    ]
)


# ==========================================================
# CACHE WEATHER REPORT GENERATION
# ==========================================================
# Prevents generating the same CSV every time the app reruns.
# ==========================================================

@st.cache_data(ttl=3600)
def generate_historical_report(lat, lon):
    weatherreport.generate_30_day_report(lat, lon)


# ==========================================================
# GRAPH FUNCTION
# ==========================================================

def plot_weather_graph(csv_file, column, title, ylabel):

    df = pd.read_csv(csv_file)

    df["date"] = pd.to_datetime(df["date"])

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        df["date"],
        df[column],
        marker="o"
    )

    ax.set_title(title)
    ax.set_xlabel("Date")
    ax.set_ylabel(ylabel)

    ax.grid(True)

    plt.xticks(rotation=45)

    plt.tight_layout()

    st.pyplot(fig)


# ==========================================================
# TAB 1 : CURRENT WEATHER
# ==========================================================

with tab1:

    col1, col2, col3, col4, col5 = st.columns(5)

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

    col4.metric(
        "💨 Wind Speed",
        f"{data['wind']['speed']} m/s"
    )

    col5.metric(
        "🌤 Weather",
        data["weather"][0]["description"].title()
    )

    # ------------------------------------------------------
    # LIVE CLOCK
    # ------------------------------------------------------

    timezone_offset = data["timezone"]

    @st.fragment(run_every="1s")
    def live_clock():

        utc_now = datetime.now(timezone.utc)

        local_time = utc_now + timedelta(
            seconds=timezone_offset
        )

        st.metric(
            f"🕒 Current Time in {city}",
            local_time.strftime("%H:%M:%S")
        )

    live_clock()

    # ------------------------------------------------------
    # LOCATION INFORMATION
    # ------------------------------------------------------

    latitude = data["coord"]["lat"]
    longitude = data["coord"]["lon"]

    st.write(f"📍 Latitude: {latitude}")
    st.write(f"📍 Longitude: {longitude}")

    # ------------------------------------------------------
    # HISTORICAL WEATHER DATA
    # ------------------------------------------------------

    with st.spinner("Generating historical weather report..."):

        generate_historical_report(
            latitude,
            longitude
        )

    try:

        df = pd.read_csv(
            "weather_last_30_days.csv"
        )

        st.subheader(
            f"📊 Historical Weather Data of {city}"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    except FileNotFoundError:

        st.warning(
            "Historical weather data could not be generated."
        )


# ==========================================================
# TAB 2 : VISUALIZATIONS
# ==========================================================

with tab2:

    st.header(
        f"📈 Maximum Temperature in {city} (Last 30 Days)"
    )

    plot_weather_graph(
        "weather_last_30_days.csv",
        "temp_max",
        "Maximum Temperature (30 Days)",
        "Temperature (°C)"
    )

    st.divider()

    st.header(
        f"📉 Minimum Temperature in {city} (Last 30 Days)"
    )

    plot_weather_graph(
        "weather_last_30_days.csv",
        "temp_min",
        "Minimum Temperature (30 Days)",
        "Temperature (°C)"
    )

    st.divider()

    st.header(
        f"🌧 Rainfall in {city} (Last 30 Days)"
    )

    plot_weather_graph(
        "weather_last_30_days.csv",
        "rain_mm",
        "Rainfall (30 Days)",
        "Rainfall (mm)"
    )


# ==========================================================
# TAB 3 : RAW JSON
# ==========================================================

with tab3:

    st.json(data)