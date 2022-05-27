import requests

_API_VERSION = 1
_API_BASE_URL = f"https://www.googleapis.com/books/v1"


def get_volume(volume_id, params=None):
    '''
    https://developers.google.com/books/docs/v1/using#RetrievingVolume
    '''
    endpoint = f"{_API_BASE_URL}/volumes/{volume_id}"
    response = requests.get(endpoint, params=params)
    response.raise_for_status()
    return response.json()


def list_books(query, params=None):
    '''
    https://developers.google.com/books/docs/v1/using#PerformingSearch
    '''
    endpoint = f"https://www.googleapis.com/books/v1/volumes"
    if not params:
        params = {}
    response = requests.get(endpoint, params={'q': query, **params})
    response.raise_for_status()
    return response.json()

