from typing import List


class TweetData(object):
    def __init__(self, kwargs):
        self.data = kwargs

    @property
    def id(self) -> str:
        return self.data.get('id')

    @property
    def text(self) -> float:
        return self.data.get('text')


class Place(object):
    def __init__(self, kwargs):
        self.data = kwargs

    @property
    def id(self) -> str:
        return self.data.get('id')

    @property
    def full_name(self) -> str:
        return self.data.get('full_name')


class Includes(object):
    def __init__(self, kwargs):
        self.data = kwargs

    @property
    def places(self) -> List[Place]:
        return self.data.get('places')


class Tweet(object):
    def __init__(self, kwargs):
        self.data = kwargs

    @property
    def data_block(self) -> TweetData:
        return TweetData(self.data.get('data'))

    @property
    def includes(self) -> Includes:
        return Includes(self.data.get('includes'))

