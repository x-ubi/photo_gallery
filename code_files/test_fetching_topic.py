import requests
import fetching_topic
import json


def test_response():
    with open('api.json') as file:
        data = json.load(file)
        url = data['url']
        response = requests.get(url)
        assert response.status_code == 200


def test_get_topics():
    with open('api.json') as file:
        data = json.load(file)
        url = data['url']
        list_of_topics = fetching_topic.get_topics(url)
        assert list_of_topics == []
