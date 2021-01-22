import requests
from fetching_topic import get_topics
import json


def test_response():
    with open('api.json') as file:
        data = json.load(file)
        url = data['topic-fetching-url']
        response = requests.get(url)
        assert response.status_code == 200


def test_get_topics():
    with open('api.json') as file:
        data = json.load(file)
        url = data['topic-fetching-url']
        list_of_topics = get_topics(url)
        assert len(list_of_topics) == 25
