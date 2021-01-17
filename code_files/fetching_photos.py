import requests


def fetch_photos_of_topic(url, given_id, given_number, given_page):
    photo_fetching_url = url.format(given_id=given_id,
                                    given_number=given_number,
                                    given_page=given_page)
    response = requests.get(photo_fetching_url).json()
    list_of_photos = [photo for photo in response]
    return list_of_photos
