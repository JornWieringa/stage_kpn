import requests

from models.models import Flights


class SchipholApiClient:
    def __init__(self, config) -> Flights:
        self.url = config.schiphol_base_url
        self.end_point = "public-flights/flights"
        app_id = config.schiphol_app_id
        api_key = config.schiphol_api_key
        self.headers = {
            "Accept": "application/json",
            "app_id": app_id,
            "app_key": api_key,
            "ResourceVersion": "v4",
        }

    def get_flights(self) -> dict:
        flights = requests.get(
            url=self.url + self.end_point, headers=self.headers, timeout=5
        )
        flight_data = flights.json()
        result = Flights(**flight_data)

        return result.flights
