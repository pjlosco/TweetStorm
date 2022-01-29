import argparse
import datetime
import logging
import logging.config
from twitter.twitter import TwitterClient
from weather.weather import WeatherClient


# 2 files, one for the stream of temperatures in fahrenheit and 1 file for the stream of the sliding averages


def run(arguments):
    number_of_streams = int(arguments.n)
    twitter_token = str(arguments.twitter_token)
    weather_token = str(arguments.weather_token)

    logging.config.fileConfig('logging.conf')
    logger = logging.getLogger(__name__)
    logger.info("Collecting twitter sample stream with locations")
    twitter_stream = TwitterClient(twitter_token).get_stream_locations(number_of_streams)
    weather_client = WeatherClient(weather_token)
    temperatures_file = open('temperatures.txt', 'w')
    sliding_averages_file = open('sliding_averages.txt', 'w')
    for tweet in twitter_stream:
        location = tweet.includes.places[0]["full_name"]
        current_weather = weather_client.current_weather(location)
        temperatures_file.write(str(current_weather.current.temp_f) + '\n')

        index = 0
        sum_of_temps = 0
        while index < 5:
            date = datetime.datetime.now()
            if index > 0:
                delta_date = datetime.timedelta(days=index)
                date = date - delta_date
            temperature = weather_client.history(location, f"{str(date.year)}-{str(date.month)}-{str(date.day)}").data['forecast']['forecastday'][0]['day']['avgtemp_f']
            sum_of_temps = sum_of_temps + temperature
            index = index + 1
        average_temp = sum_of_temps / 5
        sliding_averages_file.write(str(average_temp) + '\n')


def parse_arguments():
    """
    :return: arguments
    """
    parser = argparse.ArgumentParser(
        description='get apps',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument(
        '--n',
        help='The number of tweets to calculate the sliding average. The input value ‘n’ should be between 2 and 100',
        required=True)
    parser.add_argument(
        '--twitter_token',
        help='API token for twitter.com',
        required=True)
    parser.add_argument(
        '--weather_token',
        help='API token for weatherapi.com',
        required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    run(args)
