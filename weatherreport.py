import requests
import pandas as pd
from datetime import datetime, timedelta
import app


def Generate_30_day_report():
# Kolkata coordinates
    latitude = app.latitude
    longitude = app.longitude

    # Last 30 days
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=30)

    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={latitude}"
        f"&longitude={longitude}"
        f"&start_date={start_date}"
        f"&end_date={end_date}"
        f"&daily=temperature_2m_max,temperature_2m_min,"
        f"precipitation_sum"
        f"&timezone=auto"
    )

    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f"Request failed: {e}")
        return
    data = response.json()
    if "daily" not in data:
        print("Unexpected API response: 'daily' key missing")
        return
    df = pd.DataFrame({
        "date": data["daily"]["time"],
        "temp_max": data["daily"]["temperature_2m_max"],
        "temp_min": data["daily"]["temperature_2m_min"],
        "rain_mm": data["daily"]["precipitation_sum"]
    })

    df.to_csv("weather_last_30_days.csv", index=False)

    print("CSV saved successfully!")
    print(df.head())

if __name__=="main":
    Generate_30_day_report()