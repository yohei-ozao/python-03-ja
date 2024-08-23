import requests

API_KEY = '88b59ab67a70f17ad789446862393c94'

def search_city(query):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]  # 最初の一致する都市を返す
        else:
            return None
    else:
        return None

# 他の関数はそのまま
from datetime import datetime

def weather_forecast(lat, lon):
    url = f'http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units=metric&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        forecasts = []
        for forecast in data['list']:
            date = datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d')
            temp = forecast['main']['temp']
            weather = forecast['weather'][0]['description']
            forecasts.append({
                'date': date,
                'temp': temp,
                'weather': weather
            })
            if len(forecasts) >= 5:
                break
        return forecasts
    else:
        return None

def main():
    while True:
        try:
            city = input("City?\n> ")
            city_data = search_city(city)
            if not city_data:
                print("City not found. Please try again.")
                continue

            lat = city_data['lat']
            lon = city_data['lon']
            forecasts = weather_forecast(lat, lon)
            if forecasts:
                print(f"Here's the weather in {city_data['name']}")
                for forecast in forecasts:
                    print(f"{forecast['date']}: {forecast['weather']} {forecast['temp']}°C")
            else:
                print("Failed to retrieve weather data. Please try again.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()