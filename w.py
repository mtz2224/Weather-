import requests

main = input("Enter your country or city: ")

geo_url = f"https://geocoding-api.open-meteo.com/v1/sea>
geo_res = requests.get(geo_url).json()

if "results" not in geo_res:
    print("City or country not found.")
    exit()

lat = geo_res["results"][0]["latitude"]
lon = geo_res["results"][0]["longitude"]

weather_url = f"https://api.open-meteo.com/v1/forecast?>
weather_res = requests.get(weather_url).json()

temp = weather_res["current_weather"]["temperature"]
ws = weather_res["current_weather"]["windspeed"]

print(f"Temperature in {main}: {temp}°C")
print(f"Wind speed: {ws} km/h")
