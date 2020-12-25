import requests
import json


def get_topics(url, page_nr):
    formatted_url = url.format(page_nr=page_nr)
    response = requests.get(formatted_url).json()
    list_of_topics = [Topic(topic) for topic in response]
    return list_of_topics


class Topic:
    def __init__(self, data):
        self._id = data['id']
        self._title = data['title']
        self._nr_of_photos = data['total_photos']

    def id(self):
        return self._id

    def title(self):
        return self._title

    def nr_of_photos(self):
        return self._nr_of_photos


with open("api.json") as file:
    data = json.load(file)
    get_topics(data['url'], "1")
