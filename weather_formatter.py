from weather_api_service import Weather


def format_weather(weather : Weather) -> str:
    """ Formats weather data in string """
    return f"Сейчас в {weather.city} {weather.weather_type}, " \
            f"температура {weather.temperature}, закат в " \
            f"{weather.sunrice.strftime('%H:%M:%S')} " \
            f"восход в {weather.sunset.strftime('%H:%M:%S')}"

