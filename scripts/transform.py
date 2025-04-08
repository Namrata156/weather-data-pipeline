import pandas as pd  
from datetime import datetime


def transform_weather_data(raw_data):
    print(raw_data[0])
    transformed = []

    for entry in raw_data:
        transformed.append({
            "city": entry["name"],
            "country": entry["sys"]["country"],
            "temperature_C": entry["main"]['temp'],
            "humidity_percent": entry["main"]["humidity"],
            "wind_speed_mps": entry["wind"]["speed"],
            "weather": entry["weather"][0]["description"],
            "datetime": datetime.utcfromtimestamp(entry["dt"]).strftime('%Y-%m-%d %H:%M:%S')
        })

    return pd.DataFrame(transformed)