import requests
import json
from fetching_photos import fetch_photos_of_topic


def test_response():
    with open('api.json') as file:
        data = json.load(file)
        url = data['photo-fetching-url']
        response = requests.get(url.format(given_id='wallpapers',
                                           given_number=10,
                                           given_page=1))
        assert response.status_code == 200


def test_fetch_photos():
    with open('api.json') as file:
        data = json.load(file)
        url = data['photo-fetching-url']
        list_of_photos = fetch_photos_of_topic(url, 'wallpapers', 10, 1)
        assert len(list_of_photos) == 10
