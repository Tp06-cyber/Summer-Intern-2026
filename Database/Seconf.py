import requests
def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9c4d75bcc7984428aa16f2eab08bc3e7&units=metric"
    try:
        response =requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(data['main']['temp'])
    except requests.exceptions.RequestException as e:
        print(e)
city=input("Enter City name:")
weather_data(city)
