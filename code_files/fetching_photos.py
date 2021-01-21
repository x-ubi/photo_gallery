import requests


def fetch_photos_of_topic(url, given_id, given_number, given_page):
    """Get photos from a server into a list and return the list.
    Keyword arguments:
    url -- link to the server where the photos' info is going from
    given_id -- client id, acts as authentication for the server
    given_number -- number of photos to be fetched
    given_page -- page number of photos from selected topic to fetch
    """
    photo_fetching_url = url.format(given_id=given_id,
                                    given_number=given_number,
                                    given_page=given_page)
    response = requests.get(photo_fetching_url).json()
    list_of_photos = [photo for photo in response]
    return list_of_photos
