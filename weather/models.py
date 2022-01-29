from datetime import datetime
from enum import Enum
from typing import List


class Location(object):

    def __init__(self, kwargs):
        self.data = kwargs

    @property
    def name(self) -> str:
        return self.data.get('name')

    @property
    def region(self) -> str:
        return self.data.get('region')

    @property
    def country(self) -> str:
        return self.data.get('country')

    @property
    def lat(self) -> float:
        return self.data.get('lat')

    @property
    def lon(self) -> float:
        return self.data.get('lon')

    @property
    def tz_id(self) -> str:
        return self.data.get('tz_id')

    @property
    def localtime_epoch(self) -> int:
        return self.data.get('localtime_epoch')

    @property
    def localtime(self) -> datetime:
        return self.data.get('localtime')


class Current(object):

    def __init__(self, kwargs):
        self.data = kwargs

    @property
    def temp_c(self) -> str:
        return self.data.get('temp_c')

    @property
    def temp_f(self) -> float:
        return self.data.get('temp_f')


class WeatherResult(object):

    def __init__(self, kwargs):
        self.data = kwargs

    @property
    def current(self) -> Current:
        return Current(self.data.get('current'))

    @property
    def location(self) -> Location:
        return Location(self.data.get('location'))
