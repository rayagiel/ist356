import requests
import streamlit as st

st.title("Weather App")

def geocode(place:str) -> (float, float):
    url = "https://portal.app.cent-su.org/api/weather/geocode"
    params = {
    "language": "en",
    "count": 1,
    "place": place,
    }
    headers = {
    "accept": "application/json",
    "X-API-KEY": 'd404ab024a625b70d37134e1'
    } 

    response = requests.get(url, params=params, headers=headers, timeout=30) # this is just a string
    response.raise_for_status()
    data = response.json()
    if len(data["results"]) == 0:
        raise ValueError(f"No results found for {place}")
    lat = data['results'][0]['latitude']
    lon = data['results'][0]['longitude']
    return lat, lon

location = st.text_input("Enter a location (city, state):", "Syracuse, New York")
if location:
    try:
        lat, lon = geocode(location)
        st.write(f"Coordinates for {location}: Latitude: {lat} Longitude: {lon}")
    except 

        
def current_weather(lat: float, lon: float) -> float:
    """Return the current temperature in Fahrenheit."""
    url = "https://portal.app.cent-su.org/api/weather/current"
    params = {
        "units": "imperial",
        "lon": lon,
        "lat": lat,
    }
    headers = {
        "accept": "application/json",
        "X-API-KEY": st.secrets["WEATHER_API_KEY"],
    }

    response = requests.get(url, params=params, headers=headers, timeout=30)
    response.raise_for_status()
    data = response.json()