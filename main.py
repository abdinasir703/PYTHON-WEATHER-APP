#weather app

import requests

API_KEY = "29b66f6baff4588a6d3a531871690038"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    parameters = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=parameters,
            timeout=10
        )

        if response.status_code == 404:
            print("\nCity not found. Please try again.")
            return

        response.raise_for_status()
        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print("\n" + "=" * 35)
        print(f" WEATHER REPORT: {city_name}, {country}")
        print("=" * 35)
        print(f"Temperature : {temperature}°C")
        print(f"Feels like  : {feels_like}°C")
        print(f"Condition   : {description.title()}")
        print(f"Humidity    : {humidity}%")
        print(f"Wind speed  : {wind_speed} m/s")
        print("=" * 35)

    except requests.exceptions.Timeout:
        print("\nRequest timed out. Try again.")

    except requests.exceptions.HTTPError:
        print("\nAPI request failed. Check your API key or API access.")

    except requests.exceptions.ConnectionError:
        print("\nNo internet connection. Please check your network.")

    except (KeyError, ValueError):
        print("\nUnable to read the weather data.")

    except requests.exceptions.RequestException:
        print("\nSomething went wrong while fetching the weather.")


def main():
    print("=" * 35)
    print("       PYTHON WEATHER APP")
    print("=" * 35)

    while True:
        city = input(
            "\nEnter a city name (or 'q' to quit): "
        ).strip()

        if city.lower() == "q":
            print("\nThank you for using the Weather App!")
            break

        if not city:
            print("Please enter a city name.")
            continue

        get_weather(city)


if __name__ == "__main__":
    main()

