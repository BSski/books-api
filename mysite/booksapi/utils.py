import requests


def fetch_json_from_google_api(q: str) -> dict:
    """Returns a JSON fetched from Google Books API, based on |q| parameter."""
    url_base = "https://www.googleapis.com/books/v1/volumes?q={}"
    url = url_base.format(q)
    response = requests.get(url)
    return response.json()
