import requests
from config import GOOGLE_KEY

URL = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"


def google_request(name, latitude, longitude):
    response = requests.request(
        "GET",
        f"{URL}?inputtype=textquery&fields=rating&key={GOOGLE_KEY}&input={name}"
        f"&locationbias=circle:1000@{latitude},{longitude}"
    )
    json_response = response.json()
    if len(json_response["candidates"]) > 0:
        return json_response["candidates"][0]["rating"]
    else:
        return None
