import requests
from models.models import Flights


class SchipholApiClient:
    def __init__(self, config):
        app_id = config.application_id
        api_key = config.application_key
        self.url = config.api_url
        self.headers = {
            "Accept": "application/json",
            "app_id": app_id,
            "app_key": api_key,
            "ResourceVersion": "v4",
        }

    def get_flights(self) -> Flights:
        flights = requests.get(url=self.url + "public-flights/flights", headers=self.headers, timeout=5)
        flight_data = flights.json()
        result = Flights(**flight_data)

        return result
