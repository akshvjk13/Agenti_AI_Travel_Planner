CITY_COORDINATES = {

    "goa": {
        "latitude": 15.2993,
        "longitude": 74.1240
    },

    "delhi": {
        "latitude": 28.6139,
        "longitude": 77.2090
    },

    "mumbai": {
        "latitude": 19.0760,
        "longitude": 72.8777
    },

    "hyderabad": {
        "latitude": 17.3850,
        "longitude": 78.4867
    },

    "bangalore": {
        "latitude": 12.9716,
        "longitude": 77.5946
    },

    "chennai": {
        "latitude": 13.0827,
        "longitude": 80.2707
    },

    "kolkata": {
        "latitude": 22.5726,
        "longitude": 88.3639
    },

    "jaipur": {
        "latitude": 26.9124,
        "longitude": 75.7873
    },

    "agra": {
        "latitude": 27.1767,
        "longitude": 78.0081
    },

    "kochi": {
        "latitude": 9.9312,
        "longitude": 76.2673
    },

    "manali": {
        "latitude": 32.2396,
        "longitude": 77.1887
    },

    "shimla": {
        "latitude": 31.1048,
        "longitude": 77.1734
    },

    "udaipur": {
        "latitude": 24.5854,
        "longitude": 73.7125
    },

    "varanasi": {
        "latitude": 25.3176,
        "longitude": 82.9739
    }
}

import requests

def get_weather_forecast(city):
    """
    Fetch weather forecast
    using Open-Meteo API.
    """

    city = city.strip().lower()

    if city not in CITY_COORDINATES:

        return {
            "error": "City not found."
        }

    latitude = (
        CITY_COORDINATES[city]["latitude"]
    )

    longitude = (
        CITY_COORDINATES[city]["longitude"]
    )

    url = (
        "https://api.open-meteo.com/v1/forecast"
    )

    params = {

        "latitude": latitude,

        "longitude": longitude,

        "daily":
        "temperature_2m_max,"
        "temperature_2m_min",

        "timezone": "auto"
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        weather_data = response.json()

        return weather_data

    except requests.exceptions.RequestException as error:

        return {
            "error": str(error)
        }