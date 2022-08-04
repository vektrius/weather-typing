from gps_coordinates import get_coordinates
from weather_api_service import get_weather
from weather_formatter import format_weather
from exceptions import CantGetCoordinates, APIWeatherException

def Weather(city : str):
    try:
        coordinates = get_coordinates(city=city)
    except CantGetCoordinates:
        print('Ошибка в координатах')
        exit(1)
    try:
        weather = get_weather(coordinates)
    except:
        print('Ошибка в погоде')
        exit(1)
    print(format_weather(weather).format(weather))


if __name__ == '__main__':
    city = input("Введите название города:")
    Weather(city=city)

