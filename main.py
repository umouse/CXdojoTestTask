from process_response import process_response
from yelp_request import yelp_request


response = yelp_request(
    term="vegan cafe",
    location="San Francisco",
    limit=50
)

process_response(response)
