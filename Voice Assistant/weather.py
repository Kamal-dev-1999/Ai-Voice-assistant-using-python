import requests

def get_weather(location):
    api_key = "638f681e69244ae48a1194043242106"
    base_url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no"
    response = requests.get(base_url)
    data = response.json()

    if "error" not in data:
        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        description = data["current"]["condition"]["text"]
        return f"The temperature in {location} is {temp}°C with {description} and humidity of {humidity}%."
    else:
        return "Sorry, I couldn't find the weather for that location."
