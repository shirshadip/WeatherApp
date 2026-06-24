import streamlit as st
import requests
import pandas as pd
import weatherreport
import matplotlib.pyplot as plt 
from datetime import datetime, timedelta , timezone


st.set_page_config(
    page_title="AI Weather App",
    page_icon="🌦️",
    layout="centered"
)

# API Key
API_KEY = st.secrets["api_key"]

# User Input
city = st.text_input(
    "Enter location",
    placeholder="e.g. Kolkata",
    key="city_input"
    
).strip()

# Tabs
tab1, tab2, tab3 = st.tabs([
    "🌤 Current Weather",
    "📈 Weather Data visualization",
    "📄 JSON Data"
    
])

# Variables
data = None
response = None

# Fetch weather only if a city is entered
if city:
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    try:
        with st.spinner("Fetching weather data..."):
            response = requests.get(url, timeout=10)

        if response.status_code == 200:
            data = response.json()
        else:
            st.error("❌ City not found.")

    except requests.exceptions.RequestException:
        st.error("⚠️ Unable to connect to the weather server.")

# -----------------------------
# TAB 1
# -----------------------------
with tab1:

    if data:

        col1, col2, col3 , col4 , col5  = st.columns(5)

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
            "💨 wind speed",
            f"{data['wind']['speed']} m/s"
        )
        col5.metric(
            "Weather condition",
            f"{data['weather'][0]['description']}"
        )
        
        timezone_offset = data["timezone"]

        @st.fragment(run_every="1s")
        def live_clock():
            utc_now = datetime.now(timezone.utc)
            local_time = utc_now + timedelta(seconds=timezone_offset)

            st.metric(
                f"🕒 Current Time of {city}",
                local_time.strftime("%H:%M:%S")
            )

        live_clock()
        latitude = data["coord"]["lat"]
        longitude = data["coord"]["lon"]
        
        st.write("📍 Latitude:", latitude)
        st.write("📍 Longitude:", longitude)

        with st.spinner("Generating 30-day weather report..."):
            weatherreport.generate_30_day_report(latitude, longitude)

        try:
            df = pd.read_csv("weather_last_30_days.csv")

            st.subheader(f"📊 Historical Weather Data of {city}")
            st.dataframe(df, use_container_width=True)

        except FileNotFoundError:
            st.warning(f"Historical weather report of {city} could not be found.")


# -----------------------------
# TAB 2
# -----------------------------
with tab2:
    if data:
        # st.write("OK")
        def plot_weather_graph(csv_file, column , title , ylabel):
            df = pd.read_csv(csv_file)
            df["date"]=pd.to_datetime(df["date"])
            
            fig , ax = plt.subplots(figsize=(12 , 5))
            ax.plot(df["date"],df[column],marker="o")
            
            ax.set_title(title)
            ax.set_ylabel(ylabel)
            ax.grid(True)

            plt.xticks(rotation=45)
            plt.tight_layout()

            st.pyplot(fig)
        st.header(f"Maximum temparature in {city} , last 30 days")
        plot_weather_graph(
    "weather_last_30_days.csv",
    "temp_max",
    "Maximum Temperature (30 Days)",
    "Temperature (°C)"
)
        st.markdown("""----""")
        st.header(f"Minimum temparature in {city} , last 30 days")
        plot_weather_graph(
    "weather_last_30_days.csv",
    "temp_min",
    "Minimum Temperature (30 Days)",
    "Temperature (°C)"
)
        st.markdown("""----""")
        st.header(f"Rain Fallen in {city} , last 30 days")
        plot_weather_graph(
    "weather_last_30_days.csv",
    "rain_mm",
    "Rainfall (30 Days)",
    "Rain (mm)"
)
        
        st.markdown("""----""")
# -----------------------------
# TAB 3
# -----------------------------
with tab3:

    if data:
        st.json(data)