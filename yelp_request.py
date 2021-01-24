import requests

from config import YELP_KEY

URL = "https://api.yelp.com/v3/businesses/search"


def yelp_request(term, limit, location):
  response = requests.request(
    "GET",
    url=f"{URL}?term={term}&limit={limit}&location={location}",
    headers={
        'Authorization': f'Bearer {YELP_KEY}'
    }
  )
  return response.json()




