import requests
import pandas as pd
from datetime import datetime, timedelta
import argparse
import app


def generate_30_day_report(lat,long):
    """Download last 30 days of daily weather for given coords and save CSV."""

    # Last 30 days
    end_date = datetime.today().date()
    start_date = end_date - timedelta(days=30)

    url = (
        f"https://archive-api.open-meteo.com/v1/archive?"
        f"latitude={lat}"
        f"&longitude={long}"
        f"&start_date={start_date}"
        f"&end_date={end_date}"
        f"&daily=temperature_2m_max,temperature_2m_min,"
        f"precipitation_sum"
        f"&timezone=auto"
    )

    response = requests.get(url)
    try:
        response.raise_for_status()
    except requests.HTTPError:
        print("Status Code:", response.status_code)
        print("Response:")
        print(response.text)
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate 30-day weather report CSV for coords")
    parser.add_argument("--lat", type=float, default=22.5726, help="Latitude (default: Kolkata)")
    parser.add_argument("--lon", type=float, default=88.3639, help="Longitude (default: Kolkata)")
    args = parser.parse_args()
    generate_30_day_report(args.lat, args.lon)