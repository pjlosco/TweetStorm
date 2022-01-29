import logging
from typing import List, Optional
import requests
import json

from twitter.models import Tweet


class TwitterAuth:
    def __init__(self, token: str):
        self.bearer_token = token
        self.logger = logging.getLogger(__name__)

    def __call__(self, r):
        # modify and return the request
        r.headers['Authorization'] = f"Bearer {self.bearer_token}"
        r.headers['User-Agent'] = "v2FilteredStreamPython"
        return r


class TwitterClient:
    """

    """
    def __init__(self, token: str):
        self.twitter_auth = TwitterAuth(token)
        self.logger = logging.getLogger(__name__)

    @staticmethod
    def _url(path) -> str:
        """
        Helps format url with correct prefix
        :param path:
        :return:
        """
        return 'https://api.twitter.com/2{}'.format(path)

    def get_stream_locations(self, num_of_tweets: int) -> List[Tweet]:
        endpoint = '/tweets/sample/stream'
        params = {'expansions': 'geo.place_id',
                  # 'place.fields': 'geo',
                  'tweet.fields': 'geo'}

        response = requests.get(
            url=self._url(endpoint), auth=self.twitter_auth, stream=True, params=params
        )
        print(response.status_code)
        if response.status_code != 200:
            raise Exception(
                "Cannot get stream (HTTP {}): {}".format(
                    response.status_code, response.text
                )
            )
        stream_stack = []
        for response_line in response.iter_lines():
            if response_line:
                json_response = json.loads(response_line)
                if len(json_response['data']['geo']) != 0:
                    tweet = Tweet(json_response)
                    stream_stack.append(tweet)
                    self.logger.info("Adding tweet:" + json.dumps(json_response, indent=4, sort_keys=True))

                if len(stream_stack) >= num_of_tweets:
                    return stream_stack

