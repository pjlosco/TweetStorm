import unittest
import responses

from twitter.models import Tweet
from twitter.twitter import TwitterClient


class TwitterCientTests(unittest.TestCase):

    @responses.activate
    def test_sample_stream(self):
        token = 'TEST_TOKEN'
        url = TwitterClient._url('/tweets/sample/stream')
        responses.add(responses.GET, url,
                      json={
                          'data': {
                              'geo': {
                                  'place_id': 'e36dc663145db75c'
                              },
                              'id': '1487199673546903554',
                              'text': '@HistoryLivesDet One of the greats!!!'
                          },
                          'includes': {
                              'places': [{
                                  'full_name': 'Clawson, MI',
                                  'id': 'e36dc663145db75c'}]
                          }
                      }, status=200, content_type='application/json')

        tweet = TwitterClient(token).get_stream_locations(1)
        assert isinstance(tweet[0], Tweet)


if __name__ == '__main__':
    unittest.main()
