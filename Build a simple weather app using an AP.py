
import requests



def get_weather(city, api_key):

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)

    data = response.json()

    if response.status_code == 200:

        weather_info = {

            'city': data['name'],

            'temperature': data['main']['temp'],

            'description': data['weather'][0]['description'],

            'humidity': data['main']['humidity'],

            'wind_speed': data['wind']['speed'],

        }

        return weather_info

    else:

        print("Failed to retrieve weather data.")

        return None



def main():

    city = input("Enter the city name: ")

    api_key = 'YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key

    weather_data = get_weather(city, api_key)

    if weather_data:

        print(f"Weather in {weather_data['city']}:")

        print(f"Temperature: {weather_data['temperature']}°C")

        print(f"Description: {weather_data['description']}")

        print(f"Humidity: {weather_data['humidity']}%")

        print(f"Wind Speed: {weather_data['wind_speed']} m/s")

    else:

        print("Weather data not available.")



if __name__ == "__main__":

    main()



