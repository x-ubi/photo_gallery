import requests
# import json


def get_topics(url):
    """
    This function receives the list of topics present on the server.
    """
    response = requests.get(url).json()
    list_of_topics = [Topic(topic) for topic in response]
    return list_of_topics


class Topic:
    """
    Every object of the Topic class stores:
    an id,
    a title,
    the number of photos in it.
    TODO:
    1. When GUI implemented, also store a link to a thumbnail for the topic.
    """
    def __init__(self, data):
        self._id = data['id']
        self._title = data['title']
        self._nr_of_photos = data['total_photos']

    def __str__(self):
        return self._title

    def id(self):
        return self._id

    def title(self):
        return self._title

    def nr_of_photos(self):
        return self._nr_of_photos
