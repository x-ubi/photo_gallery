import requests


def get_topics(url):
    """Receive the list of topics present on the server."""
    response = requests.get(url).json()
    list_of_topics = [Topic(topic) for topic in response]
    return list_of_topics


class Topic:
    """
    Every object of the Topic class stores:
    an id,
    a title,
    the number of photos in it.
    """
    def __init__(self, data):
        self._id = data['id']
        self._title = data['title']
        self._nr_of_photos = data['total_photos']

    def __str__(self):
        return self._title

    def id(self):
        """Return the id of the topic."""
        return self._id

    def title(self):
        """Return the title of the topic."""
        return self._title

    def nr_of_photos(self):
        """Return the number of photos in the topic."""
        return self._nr_of_photos
