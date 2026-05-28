from tools.weather_tool import (
    get_weather_forecast
)


weather = get_weather_forecast(
    "manali"
)

print("\nWeather Forecast:\n")

print(weather)