import requests
import logging

from weather.models import WeatherResult


class WeatherClient:

    def __init__(self, token: str):
        self.API_KEY = token
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def _url(path) -> str:
        """
        Helps format url with correct prefix
        :param path:
        :return:
        """
        return 'https://api.weatherapi.com/v1{}'.format(path)

    def current_weather(self, location) -> WeatherResult:
        params = {'key': self.API_KEY,
                  'q': location}
        endpoint = '/current.json'
        response = self.make_request(endpoint, params)
        return WeatherResult(response.json())

    def history(self, location, date):
        params = {'key': self.API_KEY,
                  'q': location,
                  'dt': date}
        endpoint = '/history.json'
        response = self.make_request(endpoint, params)
        return WeatherResult(response.json())

    def make_request(self, endpoint, params):
        response = requests.get(
            url=self._url(endpoint), params=params
        )
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(
                "Cannot get request (HTTP {}): {}".format(
                    response.status_code, response.text
                )
            )
        return response
