import unittest
import responses

from weather.models import WeatherResult
from weather.weather import WeatherClient


class WeatherClientTests(unittest.TestCase):

    @responses.activate
    def test_current_weather(self):
        token = 'TEST_TOKEN'
        url = WeatherClient._url(f"/current.json?key={token}&q=London")
        responses.add(responses.GET, url,
                      json={
                          "location": {
                              "name": "London",
                              "region": "City of London, Greater London",
                              "country": "United Kingdom",
                              "lat": 51.52,
                              "lon": -0.11,
                              "tz_id": "Europe/London",
                              "localtime_epoch": 1643318052,
                              "localtime": "2022-01-27 21:14"
                          },
                          "current": {
                              "last_updated_epoch": 1643313600,
                              "last_updated": "2022-01-27 20:00",
                              "temp_c": 6.0,
                              "temp_f": 42.8,
                              "is_day": 0,
                              "condition": {
                                  "text": "Clear",
                                  "icon": "//cdn.weatherapi.com/weather/64x64/night/113.png",
                                  "code": 1000
                              },
                              "wind_mph": 4.3, "wind_kph": 6.8, "wind_degree": 240, "wind_dir": "WSW",
                              "pressure_mb": 1032.0, "pressure_in": 30.47, "precip_mm": 0.0, "precip_in": 0.0,
                              "humidity": 75, "cloud": 0, "feelslike_c": 3.4, "feelslike_f": 38.2,
                              "vis_km": 10.0, "vis_miles": 6.0, "uv": 1.0, "gust_mph": 12.8, "gust_kph": 20.5
                          }
                      }, status=200, content_type='application/json')
        weather = WeatherClient(token).current_weather('London')
        assert isinstance(weather, WeatherResult)


if __name__ == '__main__':
    unittest.main()
