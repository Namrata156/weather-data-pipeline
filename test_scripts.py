from scripts.extract import get_multiple_cities_weather
from scripts.transform import transform_weather_data
from scripts.load import save_to_postgres

cities = ["Los Angeles", "San Francisco", "Bangalore", "New York", "Tokyo", "London","Abu Dhabi"]
raw_data = get_multiple_cities_weather(cities)
df = transform_weather_data(raw_data)
save_to_postgres(df)