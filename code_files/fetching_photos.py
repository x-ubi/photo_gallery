import requests
import json


def fetch_photos_of_topic(url, given_id):
    formatted_url = url.format(given_id=given_id)
    response = requests.get(formatted_url).json()
    list_of_photos = [photo for photo in response]
    return list_of_photos


with open("api.json") as file:
    data = json.load(file)
    photos = fetch_photos_of_topic(data["photo-fetching-url"], "bo8jQKTaE0Y")
