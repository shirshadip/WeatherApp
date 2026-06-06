import streamlit as st
import requests
import tomllib

with open("KEYS.toml", "rb") as file:
    weather_data = tomllib.load(file)

API_KEY = weather_data["api_key"]

city = st.text_input("Enter a city name")

if city:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    st.json(data)

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    feels_like = data["main"]["feels_like"]

    st.write("Temperature:", temp, "°C")
    st.write("Humidity:", humidity, "%")
    st.write("Feels Like:", feels_like, "°C")