import requests

def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=230094d58d2c08cfd60d3bb1ad2e9754&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(data['main'],['temp'])
    except requests.exceptions.RequestException as e:
        print(e)
city = input("enter the city name: ")
weather_data(city)