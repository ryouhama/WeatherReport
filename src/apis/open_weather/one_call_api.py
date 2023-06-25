import requests
from typing import Any
from pydantic import Field, BaseModel


class OneCallApiParams(BaseModel):
    lat: float = Field(..., description='lat')
    lon: float = Field(..., description='lon')

    def __post_init__(self) -> None:
        self.lat = round(self.lat, 2)
        self.lon = round(self.lon, 2)

    def to_param(self) -> str:
        params = [
            f"lat={self.lat}",
            f"lon={self.lon}",
            "exclude=minutely,hourly,daily,alerts",
            "units=standard",
            "lang=ja"
        ]
        return "&".join(params)


class OneCallApi:
    api_key: str
    url = "https://api.openweathermap.org/data/3.0/onecall"

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def get(self, params: OneCallApiParams) -> dict[str, Any]:
        response = requests.get(
            f"{self.url}?{params.to_param()}&appid={self.api_key}"
        )
        return response.json()
