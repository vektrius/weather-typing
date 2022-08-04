from datetime import datetime
from enum import Enum
from typing import NamedTuple, Literal

import requests as requests

import config
from exceptions import APIWeatherException
from gps_coordinates import Coordinates, get_coordinates

Celsius = int


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: str
    sunrice: datetime
    sunset: datetime
    city: str


def get_weather(coordinate: Coordinates) -> Weather:
    """ Request weather in OpenWeather API and returns it"""
    response = _get_openweather_response(latitude=coordinate.latitude,
                                         longitude=coordinate.longitude)
    weather = _parse_openweather_response(response)
    return weather


def _get_openweather_response(latitude: float, longitude: float) -> dict:
    res = requests.get(config.WEATHER_URL.format(latitude=latitude, longitude=longitude))
    if res.status_code == 400:
        raise APIWeatherException
    return res.json()


def _parse_openweather_response(openweather_response: dict) -> Weather:
    return Weather(temperature=_temperature_parse(openweather_response),
                   weather_type=_weather_type_parse_response(openweather_response),
                   sunrice=_sun_time_parse(openweather_response, "sunrise"),
                   sunset=_sun_time_parse(openweather_response, "sunset"),
                   city=_city_parse(openweather_response))


def _temperature_parse(openweather_response: dict) -> Celsius:
    try:
        return openweather_response['main']['temp']
    except:
        raise APIWeatherException


def _weather_type_parse_response(openweather_response: dict) -> str:
    try:
        return openweather_response['weather'][0]['description']
    except:
        raise APIWeatherException


def _sun_time_parse(openweather_response: dict, time: Literal["sunrise"] | Literal["sunset"]) -> datetime:
    try:
        return datetime.fromtimestamp(openweather_response['sys'][time])
    except:
        raise APIWeatherException


def _city_parse(openweather_response: dict) -> str:
    try:
        return openweather_response['name']
    except:
        raise APIWeatherException


