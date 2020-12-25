import requests


def get_photos_of_selected_topic(url, topic):
    formatted_url = url.format(id_or_slug=topic)
    response = requests.get(formatted_url).json()
    list_of_photos = [response]
    return list_of_photos
