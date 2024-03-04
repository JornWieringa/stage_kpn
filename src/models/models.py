from typing import Literal, Optional

import airportsdata
from pydantic import BaseModel, Field, field_validator


class Route(BaseModel):
    destinations: list[str]
    eu: str
    visa: bool

    @field_validator("destinations")
    def replace_with_city_names(cls, value):
        airport_data = airportsdata.load("IATA")
        return [airport_data.get(iata, {}).get("city", iata) for iata in value]


class Flight(BaseModel):
    flight_direction: Optional[Literal["A", "D"]] = Field("A", alias="flightDirection")
    flight_name: Optional[str] = Field(None, alias="flightName")
    schedule_date_time: Optional[str] = Field(None, alias="scheduleDateTime")
    estimated_landing_time: Optional[str] = Field(None, alias="estimatedLandingTime")
    actual_landing_time: Optional[str] = Field(None, alias="actualLandingTime")
    terminal: Optional[int] = None
    route: Route


class Flights(BaseModel):
    flights: list[Flight]


# flight_data = {"flightDirection": "A", "FlightName": "HV6888", "landing_time": "20:00"}

# try:
#     validated_flight = Flight(**flight_data)
#     print("Flight data is valid:", validated_flight)
# except Exception as e:
#     print("Validation failed:", e)
